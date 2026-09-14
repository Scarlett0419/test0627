# Bulk image generation

Automates "take every image in a folder, pair it with a prompt, get back a
new generated image" using OpenAI's Images API (`gpt-image-1`). Every image
is sent as its own independent, stateless API request — no shared
conversation state carries between images, same effect as "a new chat each
time" but without driving a browser against ChatGPT's consumer web UI
(which is against OpenAI's Terms of Service for automated/bot access and
risks the account being flagged or banned, especially at bulk volume).

## Setup

```bash
pip install -r scripts/requirements.txt
export OPENAI_API_KEY=sk-...   # https://platform.openai.com/api-keys
```

## Usage

Put your source images in a folder (default expected: `images/`), then:

**Same prompt for every image:**

```bash
python scripts/bulk_generate.py \
    --input-dir images \
    --output-dir outputs \
    --prompt "Turn this into a watercolor painting"
```

**A different prompt per image** — either drop a same-named `.txt` file
next to each image (`cat.png` + `cat.txt`), or use a CSV:

```bash
python scripts/bulk_generate.py \
    --input-dir images \
    --output-dir outputs \
    --prompts-csv scripts/prompts.example.csv
```

(Copy `scripts/prompts.example.csv` and edit it, or generate a real one to
fit your own filenames.)

**Preview what would happen without spending any API calls:**

```bash
python scripts/bulk_generate.py --input-dir images --output-dir outputs \
    --prompt "..." --dry-run
```

## Behavior

- Supported source formats: PNG, WEBP, JPG (under 25MB each).
- Prompt resolution order per image: `--prompts-csv` row → sidecar `.txt`
  file → `--prompt` fallback. An image with none of those is skipped.
- Output is written to `<output-dir>/<name>_generated.png`.
- Already-generated outputs are skipped on re-run unless `--overwrite` is
  passed — safe to interrupt and resume a big batch.
- Rate limits and transient (5xx) errors are retried with exponential
  backoff; a failure on one image is logged and the run continues with the
  rest.
- Tune `--size` (e.g. `1024x1024`, `1536x1024`) and `--quality`
  (`auto`/`low`/`medium`/`high`) to control cost vs fidelity — see the
  [Images API reference](https://platform.openai.com/docs/api-reference/images/createEdit).

## Cost

Every image processed is a billed API call against your OpenAI account
(pricing depends on `--size`/`--quality`). There's no bypass for that with
this approach — but it's the only sanctioned way to automate this, and
`--dry-run` lets you sanity-check a batch (file list, resolved prompts)
before spending anything.
