#!/usr/bin/env python3
"""Transforme les images sources via WaveSpeedAI (FLUX Kontext Pro image editing).

Usage :
  python3 wavespeed_transform.py --check
  python3 wavespeed_transform.py --product /path/to/produit-dir

Le dossier produit doit contenir :
  produit-dir/
    photos/source/    -> images sources (jpg/png)
    prompts.json      -> format objet par image source :
      {
        "source_1.jpg": {
          "prompt": "hero shot, ...",
          "output": "hero.jpg",
          "shot_type": "hero",
          "aspect_ratio": "3:4"
        },
        ...
      }

Le script :
  1. Lit prompts.json
  2. Pour chaque image source : encode en base64 + appel FLUX Kontext Pro + polling + download
  3. Sauvegarde les resultats dans produit-dir/photos/ avec les noms finaux (output)

Credentials attendus :
  ~/.claude/skills/etsy-automate/.wavespeed_credentials.json
  { "api_key": "wsk_..." }

Prix : $0.04/image (FLUX Kontext Pro).
Polling : status "completed" sous ~30-45 sec/image en general.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

CRED_PATH = Path.home() / ".claude" / "skills" / "etsy-automate" / ".wavespeed_credentials.json"
ENDPOINT = "https://api.wavespeed.ai/api/v3/wavespeed-ai/flux-kontext-pro"
POLL_BASE = "https://api.wavespeed.ai/api/v3/predictions"
POLL_INTERVAL = 3
MAX_POLL = 90  # 90 * 3s = 4.5 min max


def load_creds() -> dict | None:
    if not CRED_PATH.exists():
        return None
    try:
        data = json.loads(CRED_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    if not data.get("api_key"):
        return None
    return data


def check() -> int:
    creds = load_creds()
    if creds is None:
        print("NON_CONFIGURE")
        print(f"Credentials attendus : {CRED_PATH}")
        print("Format : { \"api_key\": \"wsk_...\" }")
        print("Voir references/wavespeed-setup.md pour obtenir une cle API.")
        return 1
    print("CONFIGURE")
    print("api_key : configured")
    return 0


def safe_target(base_dir: Path, name: str) -> Path | None:
    """Valide qu'un nom de fichier (source ou output venant de prompts.json)
    reste dans base_dir. Rejette tout nom contenant un separateur de chemin
    ou une remontee de repertoire (path traversal), et verifie que le
    chemin resolu final reste bien a l'interieur de base_dir."""
    if not name:
        return None
    if Path(name).name != name:
        return None
    base_resolved = base_dir.resolve()
    candidate = (base_dir / name).resolve()
    try:
        candidate.relative_to(base_resolved)
    except ValueError:
        return None
    return candidate


def image_to_data_url(path: Path) -> str:
    """Convertit une image locale en data URL base64."""
    mime, _ = mimetypes.guess_type(str(path))
    if mime is None:
        mime = "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def submit_job(api_key: str, prompt: str, image_data_url: str,
               aspect_ratio: str = "1:1", guidance_scale: float = 3.5) -> str:
    payload = {
        "prompt": prompt,
        "image": image_data_url,
        "aspect_ratio": aspect_ratio,
        "guidance_scale": guidance_scale,
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(ENDPOINT, data=data, method="POST")
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.loads(resp.read())
    return body["data"]["id"]


def poll_result(api_key: str, request_id: str) -> str:
    url = f"{POLL_BASE}/{request_id}/result"
    for attempt in range(MAX_POLL):
        req = urllib.request.Request(url)
        req.add_header("Authorization", f"Bearer {api_key}")
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                body = json.loads(resp.read())
        except urllib.error.HTTPError as exc:
            print(f"    poll error {exc.code}, retry...")
            time.sleep(POLL_INTERVAL)
            continue
        status = body.get("data", {}).get("status", "unknown")
        if status == "completed":
            outputs = body["data"].get("outputs", [])
            if outputs:
                result_url = outputs[0]
                if urllib.parse.urlparse(result_url).scheme != "https":
                    raise RuntimeError(
                        f"URL de resultat refusee (scheme non https, possible SSRF/file://) : {result_url[:80]}"
                    )
                return result_url
            raise RuntimeError("completed mais aucun output")
        if status == "failed":
            raise RuntimeError(f"job failed : {body['data'].get('error')}")
        time.sleep(POLL_INTERVAL)
    raise RuntimeError(f"timeout apres {MAX_POLL * POLL_INTERVAL}s")


def download(url: str, dst: Path) -> int:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https":
        raise RuntimeError(
            f"URL de resultat refusee (scheme non https, possible SSRF/file://) : {url[:80]}"
        )
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=60) as resp:
        dst.write_bytes(resp.read())
    return dst.stat().st_size


def transform_product(product_dir: Path) -> int:
    creds = load_creds()
    if creds is None:
        print("ERREUR : credentials WaveSpeedAI absents. Lance --check.")
        return 1

    api_key = creds["api_key"]
    prompts_file = product_dir / "prompts.json"
    photos_dir = product_dir / "photos"
    source_dir = photos_dir / "source"

    if not prompts_file.exists():
        print(f"ERREUR : {prompts_file} introuvable.")
        print("Format attendu : { \"source_filename.jpg\": { \"prompt\": \"...\", \"output\": \"hero.jpg\" }, ... }")
        return 1
    if not source_dir.exists():
        print(f"ERREUR : {source_dir} introuvable.")
        return 1

    prompts = json.loads(prompts_file.read_text(encoding="utf-8"))
    photos_dir.mkdir(parents=True, exist_ok=True)

    total = len(prompts)
    cost_per = 0.04
    print(f"\n{total} transformations a lancer (FLUX Kontext Pro, ~${cost_per}/img)")
    print(f"Cout estime : ~${cost_per * total:.2f}\n")

    success = 0
    failures = []
    for i, (source_name, spec) in enumerate(prompts.items(), 1):
        output_name = spec.get("output", source_name)
        prompt = spec.get("prompt", "").strip()

        print(f"[{i}/{total}] {source_name} -> {output_name}")

        source_path = safe_target(source_dir, source_name)
        if source_path is None:
            print(f"    SKIP : nom de fichier source invalide (path traversal) : {source_name!r}")
            failures.append(source_name)
            continue
        output_path = safe_target(photos_dir, output_name)
        if output_path is None:
            print(f"    SKIP : nom de fichier de sortie invalide (path traversal) : {output_name!r}")
            failures.append(source_name)
            continue

        if not source_path.exists():
            print(f"    SKIP : source introuvable {source_path}")
            failures.append(source_name)
            continue
        if not prompt:
            print("    SKIP : prompt vide")
            failures.append(source_name)
            continue

        shot_type = spec.get("shot_type", "")
        aspect_ratio = spec.get("aspect_ratio")
        if not aspect_ratio:
            if shot_type in ("hero", "lifestyle", "packaging-gift"):
                aspect_ratio = "3:4"
            else:
                aspect_ratio = "1:1"

        guidance_scale = spec.get("guidance_scale", 3.5)

        try:
            print(f"    encode + submit (aspect_ratio={aspect_ratio}, guidance={guidance_scale})...")
            data_url = image_to_data_url(source_path)
            request_id = submit_job(api_key, prompt, data_url, aspect_ratio, guidance_scale)
            print(f"    id={request_id}, polling...")
            result_url = poll_result(api_key, request_id)
            print(f"    download {result_url[:60]}...")
            fsize = download(result_url, output_path)
            print(f"    OK : {fsize // 1024} KB -> {output_path.name}")
            success += 1
        except urllib.error.HTTPError as exc:
            err_body = exc.read().decode(errors="ignore")[:300]
            print(f"    HTTP {exc.code} : {err_body}")
            failures.append(source_name)
        except Exception as exc:  # noqa: BLE001
            print(f"    ERREUR : {exc}")
            failures.append(source_name)

    print(f"\n=== Bilan : {success}/{total} reussites ===")
    if failures:
        print(f"Echecs : {', '.join(failures)}")
    cost_real = cost_per * success
    print(f"Cout reel estime : ~${cost_real:.2f}")
    return 0 if success == total else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Verifie la config.")
    parser.add_argument("--product", help="Chemin du dossier produit.")
    args = parser.parse_args()

    if args.check:
        return check()
    if args.product:
        return transform_product(Path(args.product).expanduser())
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
