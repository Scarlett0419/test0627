# etsy-automate

Claude Code skill for building an Etsy dropshipping shop from scratch — product research to published draft, mostly automated.

**Core function**: automated product listing creation. Given a product idea (or a niche to explore), the skill runs parallel agents to source from AliExpress, analyze competition, mine buyer reviews, write an SEO-optimized listing, and transform source photos into original visuals.

Human validation is required only for images. Everything else (SEO, title, tags, pricing, description) is generated automatically.

---

## What it does

- **Niche research** — finds profitable niches with real demand and manageable competition
- **Product sourcing** — identifies AliExpress suppliers with 1000+ orders, calculates margin at 3 price scenarios
- **Competitor analysis** — scrapes top 15 Etsy listings, extracts pricing patterns, SEO gaps, visual angles
- **Review mining** — extracts buyer language from real reviews to use in listings
- **SEO-optimized listing** — title front-loaded with the anchor keyword, all 13 tags filled, attributes set, description with first-160-chars meta
- **Image pipeline** — transforms AliExpress product photos via FLUX Kontext (WaveSpeedAI API) into original visuals with different backgrounds and lighting
- **Etsy draft posting** — posts the listing as a draft via Etsy API v3 (publication stays manual in the Etsy dashboard)
- **Performance tracking** — retrieves listing stats (views, favorites, sales) via API

---

## Setup

### Requirements

- Python 3.10+
- Claude Code (to run the skill itself)
- Etsy developer account (free) — for draft posting
- WaveSpeedAI account — for image transformation ($0.04/image, FLUX Kontext Pro)

### Image transformation: two options

**Option A — WaveSpeedAI (recommended, automated)**
Pay-per-use API. ~$0.04/image. Fully automated via `scripts/wavespeed_transform.py`. No subscription needed. Sign up at wavespeed.ai, get an API key, store it in `.wavespeed_credentials.json`.

**Option B — Higgsfield (manual alternative)**
Subscription required (~$19/month Basic). Use the web app at app.higgsfield.ai for manual control over each transformation. Higher visual quality ceiling but requires human operation for each image. Not automatable via API in the current skill version.

### Install

```bash
# Clone the skill
git clone https://github.com/your-username/etsy-automate ~/.claude/skills/etsy-automate

# Run from Claude Code
/etsy-automate
```

### Etsy API (optional, for draft posting)

1. Create an app at etsy.com/developers
2. Add callback URL: `http://lvh.me:3003/callback`
3. Run OAuth. Recommended: environment variables, so the secret never appears in argv, shell history, or `ps`:
   ```bash
   export ETSY_KEYSTRING=YOUR_KEY
   export ETSY_SHARED_SECRET=YOUR_SECRET
   python3 scripts/etsy_oauth.py --shop-id YOUR_SHOP_ID
   ```
   If the env vars are not set, the script prompts for them interactively with a masked (getpass) input.
   `--keystring`/`--secret` CLI flags still work for backward compatibility, but avoid them: any argument on the command line is visible to other local users via `ps aux` while the process runs, not just in shell history.
4. Credentials saved to `~/.claude/skills/etsy-automate/.etsy_credentials.json` (gitignored)

See `references/etsy-api-setup.md` for the full setup guide.

### WaveSpeedAI API

Store credentials in `~/.claude/skills/etsy-automate/.wavespeed_credentials.json`:
```json
{
  "api_key": "your_wavespeed_api_key"
}
```
See `references/wavespeed-setup.md` for the full setup guide.

---

## Usage

Invoke from Claude Code:

```
/etsy-automate
```

Three entry modes:
- **Mode A** — full shop from scratch (niche → identity → product → listing)
- **Mode B** — audit an existing shop, create new listings for it
- **Mode C** — direct listing creation (you provide the product, skip niche research)

The skill handles everything sequentially. One product at a time — no batch mode.

---

## Scripts

| Script | What it does |
|--------|-------------|
| `create_workspace.py` | Creates the product folder structure on Desktop |
| `margin_calc.py` | Calculates margin at 3 price scenarios with Etsy fees |
| `wavespeed_transform.py` | Transforms source photos via WaveSpeedAI FLUX Kontext |
| `etsy_oauth.py` | OAuth PKCE flow to get Etsy API credentials |
| `etsy_draft.py` | Posts/deletes drafts, uploads images, sets attributes |
| `etsy_stats.py` | Retrieves listing performance stats |
| `aliexpress_api.py` | AliExpress Affiliate API integration (optional) |

---

## Key decisions (non-obvious)

**Why `i_did` + `made_to_order` instead of `someone_else`?**
Etsy rejects `who_made: "someone_else"` via API (returns 400). Using `i_did` + `when_made: "made_to_order"` is the only way to post a draft programmatically. Publication remains the user's responsibility.

**Why lvh.me for OAuth?**
Etsy refuses `localhost` and IP addresses as OAuth callback URLs. `lvh.me` is a public domain that resolves to `127.0.0.1`, satisfying Etsy's domain requirement while keeping the OAuth flow entirely local.

**Why WaveSpeedAI over direct Higgsfield API?**
Higgsfield's MCP does not expose a `get_job_result` tool, making asynchronous job retrieval impossible via the MCP. WaveSpeedAI wraps the same Higgsfield Soul model with a proper async API (POST job → poll result → download).

**Why no batch/multi-product mode?**
Intentional. Each product needs human review of sourcing choices, margin, visual style, and image validation. Batching creates unreviewed listings. The tool is a workflow assistant, not a factory.

---

## Compliance note

**Read this before using.**

Etsy's Terms of Service prohibit raw resale of items the seller did not make, design, or significantly modify. Listing AliExpress products as-is violates this policy and may result in shop suspension.

**`who_made` field**: this tool sets `who_made: "i_did"` in draft listings because the Etsy API rejects `"someone_else"` with a 400 error. This is a technical workaround for the API — it does NOT mean you are telling the truth about production. **You are solely responsible for how you represent your products to buyers and to Etsy.** Publishing a listing with false claims about its origin is your decision and your liability, not the tool's.

This skill creates draft listings only. Nothing is published automatically. The publish button is yours.

Recommended path to stay compliant: print-on-demand (Printful, Printify) — you design, a partner produces. The full pipeline (SEO, images, listing) works identically for POD. See `references/compliance.md`.

---

## License

MIT — see LICENSE file.

This software is provided "as is", without warranty of any kind. The authors are not liable for any claim, damages, or consequences arising from use of this tool, including but not limited to Etsy account suspension, API policy violations, or misrepresentation of products. Use at your own risk.
