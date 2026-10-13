---
name: etsy-dropship-product-research
description: Etsy dropshipping workflow - turn a niche into profitable keywords, find new-but-winning competitor listings (EverBee), match AliExpress/private-supplier sources, log products in a sheet, and draft SEO listings in batches. Use when asked to find Etsy products/keywords to dropship, vet a competitor listing, source it, or build listing drafts. Not for general Etsy shop management, customer messages, or non-Etsy marketplaces.
---

# Etsy Dropship Product Research

Core rule: **batch by mode.** Do research in one block, listing creation in another. Never bounce between tasks. Output is a product sheet of ~10 rows, then listings.

## Cost rules (follow strictly)
- Ask for the niche only if missing; otherwise proceed. One clarifying question max.
- Don't browse or search unless the user asks for live data. Without tools, give a framework + checklist and ask the user to paste EverBee/Etsy data.
- Work from pasted data first; analyse, don't re-fetch.
- Process in batches: keywords (5-10) -> shortlist (2-3) -> products (~10). Stop at each gate and let the user choose.
- Never write long listing copy for products that haven't passed the vet step.

## Workflow

### 1. Keywords
Given a niche, produce ~10 candidate keywords as a table: keyword | demand | competition | avg price | difficulty | verdict (go / consider / skip). Flag only what the data supports; mark guesses as estimates. User picks 2-3.

### 2. Find winners (EverBee Product Analytics, user-run)
Per chosen keyword, ask user to paste top results, or screen for:
- Listing/shop young (listing ~<3 months, shop <1 year) yet strong monthly revenue = **new but already winning**
- Rising revenue graph, esp. ahead of Q4
- Good keywords, home/personalised-type categories with sales velocity
- Star Seller is fine; high-quality photos are NOT a barrier (AI mockups cover this)
Prefer personalised/customisable items - easier to differentiate and better margin.

### 3. Dropship check and source
- Confirm sourcing: reverse-image search the main photo (AliExpress "search by image" extension), compare variants/designs.
- Compare supplier price vs Etsy price. AliExpress is for validation and reference photos; recommend a **private supplier** for margin, quality and customisation.
- Reference supplier photos feed AI mockup generation (new images, new product names).

### 4. Log to sheet (mandatory, do not rely on memory)
Columns: `Supplier link` (strip tracking, keep up to `.html`) | `Rough product name` | `Competitor link` | `Est. cost` | `Competitor price` | `Title` | `Description` | `13 tags` | `Notes/status`.
Log everything as you go; also note the competitor's other listings for adjacent niches/trends and add them as new rows. Reuse the existing sheet if the user has one.

### 5. Listings (batch, after research block)
For each row generate: SEO title, description, 13 tags - modelled on the competitor's title/description/tags but **rewritten, not copied** (no copying competitor text or photos verbatim). Use supplier images as context if provided. Keep one tight prompt per product; batch several products in one response.

### 6. Volume
Goal: 10 products researched -> 10 listed, repeated daily. Volume and consistency win; test many, kill losers fast.

## Output style
Terse tables and checklists. No recap of the method unless asked. End each stage with the one next action for the user.
