---
name: etsy-ai-product-photos
description: Etsy dropshipping - vet a sourced product's profit (supplier quote -> Etsy fees -> price/margin) and plan or write AI image prompts that turn bland supplier photos into a consistent Etsy listing photo set (lifestyle, flat lay, on-body, gift/use-case, size chart). Use when asked to price a dropship product, check margin after Etsy fees, request supplier quotes, or make/prompt AI listing photos. Not for keyword/product discovery (use etsy-dropship-product-research) or general photo editing.
---

# Etsy: Profit Check + AI Product Photos

Order matters: **price first, photos second.** Don't plan photos for a product that can't be profitable.

## Cost rules
- Work from numbers/links the user gives; don't browse. Ask once for missing inputs (cost, currency, target price).
- Prompts are short and plain, not engineered. Iterate one change at a time.
- Output a shot list + ready-to-paste prompts in one response, not essays.

## 1. Supplier quote (message template)
"Can you source this [product]? [Material requirement, e.g. genuine leather, no fake]. Link: [AliExpress URL] + photos. Quote delivered to US, UK, Germany, Australia." (Those 4 cover most buyers; EU/Germany usually costs more due to import fees.) Use the highest quote as the safe cost basis.

## 2. Profit check
Inputs: landed cost (worst-case country), test price, currency (keep one throughout).
Etsy fee stack to deduct: listing fee, transaction fee, payment processing, **offsite ads 15%** (12% only if shop >$10k revenue/yr), plus any planned sale (e.g. 20% off).
Compute and show a small table: price | margin normal | margin with offsite ad | margin with sale + ad. Use the user's fee-calculator numbers if given; otherwise state fee rates as assumptions and tell them to verify current rates.
Guide: start price so margin still positive after sale + offsite ads; set list price ~20% above sale target so the sale price is the real price. Verdict: proceed / reprice / drop. Say plainly if margin is thin.

## 3. Reference research (user-run)
Search Etsy for the product; save 3-6 bestseller/Star Seller photos. Note styles that recur: real-world use, on-body, dark/ambient vs bright, home or outdoor settings.

## 4. Photo set (target ~8-10 images, 2000x2000 px square, final assembly in Canva)
Give each shot as a one-line prompt. Standard set:
1. Hero lifestyle shot replicating a bestseller reference style
2. Second angle, **same backdrop** (e.g. top-down) - consistency looks authentic
3. On-body / in-use, product must contrast with clothing so it pops as a thumbnail
4. Back/alternate view or multi-use shot
5. Gift/family use-case (target the gifting buyer: partner, parents, grandparents, teens)
6. **Size infographic**: face-on, same backdrop, dimension lines (give L x H x D); also note what fits inside
7+. Detail close-ups (zips, stitching, material), variants/colours

Prompt recipe (ChatGPT image model): upload 3+ supplier photos of the real product (close-ups, all angles) + the one reference style; say which image is the style to replicate; "2000x2000"; keep the real product exactly as-is. Say "amazing" after a good result so it follows the pattern. If refused, drop trigger words (e.g. "masculine") and describe the scene neutrally.

## 5. QA before upload (non-negotiable)
- Product matches supplier item: zips, handles, logos, colours, material - no hallucinated parts.
- No invented text, names, or personalisation.
- **Size is accurate** vs real dimensions (AI often mis-scales); fix or crop.
- Don't misrepresent materials/features; add the real dimensions to the description too.
- Same backdrop/lighting across the set; first image works at thumbnail size.
Etsy: check current policy on disclosing AI-generated imagery and follow it.

## Output style
Tables for margins, numbered list for shots, prompts in code blocks. End with the single next action.
