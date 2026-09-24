# Q4 2026 Etsy scan — first pass

Date: 2026-09-24. Source: EtsyHunt best-seller lists (top 10 per category,
ranked by estimated weekly sales, data dated 2026-09-01), 14 categories, 140
listings. Raw data: `etsyhunt-2026-09-01.json`.

Etsy itself blocks this cloud browser, so these are third-party *estimates*,
not Etsy's on-page numbers. No favorites, listing age, badges or basket counts
yet. Treat everything below as a shortlist to validate, not a verdict.

**Freshness signal:** weekly sales ÷ total sales. A high ratio means most of a
listing's lifetime sales happened in the last week, i.e. new and already hot
(the funnel's "new but popular" filter).

## Shortlist (recurring patterns, not one-off listings)

| # | Pattern | Evidence (weekly / total sales) | Type | Read |
|---|---|---|---|---|
| 1 | **Personalized gingerbread-letter name ornaments / stocking tags** | AnitaDesignArt 187 / 852 · PITTMOON 48 / 258 · svgmilocom 35 / 1,652 · TheSquidAtelier 32 / 12,871 | Physical (laser-cut wood/acrylic) or digital SVG cut file | 4 listings in 2 categories, two of them new and hot. Best Christmas candidate; peaks Nov–Dec, so launch now. |
| 2 | **Christmas crochet patterns (PDF)** | Wreath pattern 47 / 118 · Snowy tree ornament 27 / 3,210 · Halloween equivalents very strong: ghost granny-square blanket 291 / 1,072, 3D pumpkin coaster set 327 / 2,582, ghost keychain 140 / 464 | Digital | Halloween crochet patterns are the hottest cluster in the data, but Halloween is too late to launch. The same buyers move on to Christmas patterns, so this is the digital pick. |
| 3 | **Personalized embroidered knit Christmas stockings** | 10+ listings; RobertSeCo 126 / 91,222 · new entrant StitchStoryTell 79 / 255 · velvet-bow variant 24 / 502 | Physical (POD/supplier) | Huge, proven demand, but crowded. Enter only with a different angle (velvet, pet, bow). |
| 4 | **Personalized kids' name corduroy backpack / purse** | SonaMade 292 / 5,060 · TheCozyStudioCraft 204 / 2,368 | Physical | Strong gift item all year that Christmas lifts further. Two shops share the pattern. |
| 5 | **Engraved bridesmaid compact mirror** | ForeverYourGiftStore 170 / 619 (new) · TheVinc 151 / 11,917 | Physical | New entrant is winning against an established seller; wedding plus stocking-stuffer demand. |

## Listing links

Listing URLs for every row are in `etsyhunt-listing-ids-2026-09-01.json`
(EtsyHunt product IDs are Etsy listing IDs: `https://www.etsy.com/listing/<id>`).
Not opened from here, since Etsy blocks this environment. Higher IDs are newer
listings: 44xx–45xx million were created recently, 17xx–18xx million are older.

## Excluded

- Trademark/IP risk: Lord of the Rings map, Winnie the Pooh patterns, Disney
  shirts, Ghostface/Scream print, "F1 colours" keyring.
- Likely resold mega-bundles ("20,000+ amigurumi patterns"): copyright risk.
- Services mis-categorized as products (custom logo shirts, embroidery
  digitizing).

## Next steps to validate (needs Etsy data)

1. Get the Etsy API key working (see the session chat for setup) or add
   EverBee login to the environment.
2. For #1, #2 and #5: pull favorites, views, listing age and shop age for the
   top ~50 listings of each keyword and apply the funnel's filters (listing age
   ≤ 3 mo, shop age ≤ 6 mo, favorites vs age).
3. Rate keyword difficulty (etsy-seller) and profit after Etsy fees
   (amazon-product-research scoring, Etsy fees) for the survivors, then give
   go / hold / no-go (sealeap-etsy-product-selection).
