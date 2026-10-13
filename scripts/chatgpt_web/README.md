# ChatGPT web bulk sender (Playwright, no API key)

Drives a real, logged-in browser against **chatgpt.com** to send an image +
prompt pair and get a generated image back, opening a **brand-new chat for
every pair** — for people who only have a ChatGPT Plus/Free login and don't
want to pay per-call for the API.

## Read this first

Automating the consumer ChatGPT web UI like this is against OpenAI's Terms
of Service (they require the API for programmatic/bot access), and OpenAI
can flag, rate-limit, or ban an account for it — more likely the larger the
batch and the faster it runs. This script paces requests with randomized
delays and runs a visible (non-headless) browser to look as close to manual
use as possible, but that reduces the risk, it doesn't remove it. Use it on
your own account, at your own risk, for a batch size you're comfortable
losing access over. If that trade-off doesn't sit right, use
`scripts/bulk_generate.py` in this repo instead — same "new chat every
image" behavior, but through OpenAI's actual Images API, billed per call
and fully within ToS.

Also: ChatGPT's web UI changes fairly often, and this script depends on its
DOM structure (button labels, test ids). If a step stops working, see
[If selectors break](#if-selectors-break) below.

## Setup

```bash
cd scripts/chatgpt_web
npm install
npx playwright install chromium
```

## 1. Log in once

```bash
node login.js
```

A real Chromium window opens on chatgpt.com. Log in by hand (password,
2FA, whatever your account needs), then come back to the terminal and
press Enter. Your session is saved to `./chatgpt-profile/` (a Chromium
user-data dir with cookies) and reused by `send_batch.js` — you shouldn't
need to log in again unless the session expires or you log out.

**Never commit `chatgpt-profile/`** — it's your live login session. It's
already excluded via the repo's `.gitignore`.

## 2. Put images + prompts in place

Same convention as `scripts/bulk_generate.py`:

- Drop images in `images/` (repo root) — PNG/WEBP/JPG.
- Give each one a prompt via **one** of:
  - a same-named sidecar text file (`cat.png` + `cat.txt`), or
  - a two-column CSV (`filename,prompt`) — see `scripts/prompts.example.csv`, or
  - one `--prompt` used as the fallback for every image without the above.

## 3. Run the batch

```bash
node send_batch.js \
  --input-dir ../../images \
  --output-dir ../../outputs \
  --prompt "Turn this into a watercolor painting"
```

or with per-image prompts:

```bash
node send_batch.js \
  --input-dir ../../images \
  --output-dir ../../outputs \
  --prompts-csv ../prompts.example.csv
```

Preview what would run without touching the browser:

```bash
node send_batch.js --input-dir ../../images --output-dir ../../outputs --prompt "..." --dry-run
```

### What it does, per image

1. Navigates to a fresh `chatgpt.com` chat (no shared history with the
   previous image — this is the "new chat every time" part).
2. Attaches the image and types the prompt into the composer.
3. Sends it and waits for the reply to finish generating.
4. Saves the assistant's text to `outputs/<name>_response.txt` and any
   generated image(s) to `outputs/<name>_chatgpt.png` (`_1`, `_2`, ... if
   there's more than one).
5. Waits a randomized delay (`--min-delay`/`--max-delay` seconds, default
   8–20s) before the next image.

Already-processed images (an existing `<name>_response.txt`) are skipped
on re-run unless you pass `--overwrite` — safe to interrupt and resume.

### Options

| Flag | Default | Meaning |
|---|---|---|
| `--input-dir` | `../../images` | Folder of source images |
| `--output-dir` | `../../outputs` | Folder for responses/generated images |
| `--profile-dir` | `./chatgpt-profile` | Where the logged-in session lives |
| `--prompt` | — | Fallback prompt for images with no sidecar/CSV entry |
| `--prompts-csv` | — | `filename,prompt` CSV, takes priority over sidecar files |
| `--overwrite` | off | Redo images that already have a saved response |
| `--dry-run` | off | List what would be sent, no browser launched |
| `--headless` | `false` | Run without a visible window (more detectable, not recommended for large batches) |
| `--min-delay` / `--max-delay` | `8` / `20` | Random pause (seconds) between images |
| `--timeout` | `240000` | Max ms to wait for one reply to finish generating |

## If selectors break

ChatGPT's frontend changes its DOM/test-ids periodically, which can break
one of the CSS selectors near the top of `send_batch.js` (`SELECTORS`).
Symptoms look like "Composer not found", "Could not find the attach/plus
button", or a hang waiting for a reply. To fix:

1. Run `PWDEBUG=1 node send_batch.js ...` — this opens the Playwright
   Inspector alongside the browser so you can step through and see exactly
   where it's stuck.
2. Right-click the element that the failing step needs (the composer box,
   the "+" attach button, the send button, ...) in the actual browser →
   Inspect → note its `data-testid`/`aria-label`.
3. Add that as a new entry in the relevant array in `SELECTORS` (existing
   ones are tried first, in order) — no other code changes needed.
