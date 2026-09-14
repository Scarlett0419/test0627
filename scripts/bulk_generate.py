#!/usr/bin/env python3
"""
Bulk image-to-image generation via the OpenAI Images API.

For every image in an input directory, sends that image plus a prompt to
OpenAI's images.edit endpoint (gpt-image-1) and saves the resulting image.
Each request is independent/stateless -- the equivalent of "a fresh chat
every time" -- so images can be processed in bulk with no shared state
and no risk of one prompt bleeding into the next.

Usage:
    export OPENAI_API_KEY=sk-...

    # Same prompt applied to every image in a folder
    python scripts/bulk_generate.py \
        --input-dir images \
        --output-dir outputs \
        --prompt "Turn this into a watercolor painting"

    # Per-image prompts: put a same-named .txt file next to each image
    # (cat.png -> cat.txt), or pass --prompts-csv mapping filename,prompt
    python scripts/bulk_generate.py \
        --input-dir images \
        --output-dir outputs \
        --prompts-csv prompts.csv

Notes:
    - Supported input formats for images.edit: PNG, WEBP, JPG (<25MB).
    - Set --size / --quality / --n to match what you need; see
      https://platform.openai.com/docs/api-reference/images/createEdit
    - Retries with exponential backoff on rate limits / transient errors.
    - Safe to re-run: already-generated outputs are skipped unless
      --overwrite is passed.
"""

from __future__ import annotations

import argparse
import base64
import csv
import logging
import sys
import time
from pathlib import Path

try:
    from openai import OpenAI, APIError, RateLimitError
except ImportError:
    print(
        "Missing dependency. Install it with:\n"
        "    pip install -r scripts/requirements.txt",
        file=sys.stderr,
    )
    raise

SUPPORTED_EXTS = {".png", ".webp", ".jpg", ".jpeg"}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("bulk_generate")


def load_prompt_map(prompts_csv: Path | None) -> dict[str, str]:
    """filename -> prompt, from a two-column CSV (filename,prompt)."""
    if not prompts_csv:
        return {}
    mapping: dict[str, str] = {}
    with prompts_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or len(row) < 2:
                continue
            filename, prompt = row[0].strip(), row[1].strip()
            if filename and filename.lower() != "filename":
                mapping[filename] = prompt
    return mapping


def resolve_prompt(
    image_path: Path, default_prompt: str | None, prompt_map: dict[str, str]
) -> str | None:
    # 1) explicit mapping from --prompts-csv
    if image_path.name in prompt_map:
        return prompt_map[image_path.name]
    # 2) sidecar file: cat.png -> cat.txt
    sidecar = image_path.with_suffix(".txt")
    if sidecar.exists():
        text = sidecar.read_text(encoding="utf-8").strip()
        if text:
            return text
    # 3) fallback to a single prompt for every image
    return default_prompt


def generate_one(
    client: OpenAI,
    image_path: Path,
    prompt: str,
    size: str,
    quality: str,
    max_retries: int,
) -> bytes:
    attempt = 0
    while True:
        attempt += 1
        try:
            with image_path.open("rb") as img_file:
                result = client.images.edit(
                    model="gpt-image-1",
                    image=img_file,
                    prompt=prompt,
                    size=size,
                    quality=quality,
                    n=1,
                )
            b64 = result.data[0].b64_json
            return base64.b64decode(b64)
        except RateLimitError as e:
            if attempt > max_retries:
                raise
            wait = min(2**attempt, 60)
            log.warning("Rate limited on %s, retrying in %ss (%s)", image_path.name, wait, e)
            time.sleep(wait)
        except APIError as e:
            if attempt > max_retries or getattr(e, "status_code", 500) < 500:
                raise
            wait = min(2**attempt, 60)
            log.warning("API error on %s, retrying in %ss (%s)", image_path.name, wait, e)
            time.sleep(wait)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input-dir", required=True, type=Path, help="Folder of source images")
    parser.add_argument("--output-dir", required=True, type=Path, help="Folder to write generated images")
    parser.add_argument("--prompt", help="Default prompt applied to every image lacking a more specific one")
    parser.add_argument("--prompts-csv", type=Path, help="CSV of filename,prompt overrides")
    parser.add_argument("--size", default="1024x1024", help="Output size (default 1024x1024)")
    parser.add_argument("--quality", default="auto", choices=["auto", "low", "medium", "high"])
    parser.add_argument("--max-retries", type=int, default=5)
    parser.add_argument("--overwrite", action="store_true", help="Regenerate even if output already exists")
    parser.add_argument("--dry-run", action="store_true", help="List what would be sent, without calling the API")
    args = parser.parse_args()

    if not args.input_dir.is_dir():
        parser.error(f"--input-dir {args.input_dir} is not a directory")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    prompt_map = load_prompt_map(args.prompts_csv)

    images = sorted(
        p for p in args.input_dir.iterdir() if p.suffix.lower() in SUPPORTED_EXTS
    )
    if not images:
        log.error("No supported images (%s) found in %s", ", ".join(SUPPORTED_EXTS), args.input_dir)
        return 1

    client = None if args.dry_run else OpenAI()  # reads OPENAI_API_KEY from env

    ok, skipped, failed = 0, 0, 0
    for image_path in images:
        prompt = resolve_prompt(image_path, args.prompt, prompt_map)
        out_path = args.output_dir / f"{image_path.stem}_generated.png"

        if not prompt:
            log.warning("Skipping %s: no prompt (no --prompt, no sidecar .txt, no CSV row)", image_path.name)
            skipped += 1
            continue

        if out_path.exists() and not args.overwrite:
            log.info("Skipping %s: output already exists (%s)", image_path.name, out_path.name)
            skipped += 1
            continue

        if args.dry_run:
            log.info("[dry-run] %s -> %s  | prompt: %s", image_path.name, out_path.name, prompt)
            continue

        log.info("Generating %s -> %s", image_path.name, out_path.name)
        try:
            data = generate_one(client, image_path, prompt, args.size, args.quality, args.max_retries)
            out_path.write_bytes(data)
            ok += 1
        except Exception as e:  # noqa: BLE001 - report and keep going
            log.error("Failed on %s: %s", image_path.name, e)
            failed += 1

    log.info("Done. %d generated, %d skipped, %d failed.", ok, skipped, failed)
    return 1 if failed and not ok else 0


if __name__ == "__main__":
    raise SystemExit(main())
