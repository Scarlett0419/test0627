# Overton Policy Impact Dashboard: plan and draft proposal

**For:** Prof. Steffen Böhm, Director of Research, Sustainable Futures (Department of Management, University of Exeter Business School)
**From:** Scarlett Whitthread
**Status:** Trial built with sample data. Waiting on Overton API access to load real figures.

---

## 1. What the dashboard answers

| Question | How it is shown |
|---|---|
| How often is each colleague mentioned or cited in policy? | KPI tiles: total, cited and named mentions |
| How much does it matter? | **Impact score** (weighted, see §4) and the share of mentions from government or IGO sources |
| What are they known for? | Topic-area bar chart (Health, Security, Food & Agriculture, Climate & Energy, Circular Economy, …) |
| Who cites us most? | Top policy outlets table with source type, country and latest date |
| Where is our work read and used? | World map and top-geographies table (IGO and EU listed separately) |
| Which policy bodies engage with us? | Source classification: Government / IGO / Think tank / NGO / Other |
| How has it changed over time? | Timeline by year, split into *research cited* and *named in text* |
| What is new? | Most recent mentions, linked to the source document |
| Each person on their own | A selectable profile with headshot opens that person's dashboard |
| The department as a whole | "Everyone" view and a staff summary table, scoped to Sustainable Futures or the whole Department of Management |

Filters: period (all, 5 years, 3 years, 12 months) and mention type. Every view can also be exported to Excel (`overton_mentions.xlsx`: a Summary sheet and a Mentions sheet).

## 2. How a "mention" is found

Overton's API (`https://app.overton.io/`, key-based JSON API) supports two complementary routes:

1. **Research cited.** We collect each person's DOIs from OpenAlex (via ORCID) or from a supplied list, turn them into an Overton ID set (`generate_id_set.php`), and ask for every policy document that cites any of them (`documents.php?plain_dois_cited=set:…`). This is the strongest and least ambiguous signal.
2. **Named in text.** A full-text search for every spelling of the name (`"Steffen Böhm" OR "Steffen Boehm" OR "Steffen Bohm"`) finds documents that name the person without formally citing a paper, such as evidence submissions, quotes and committee lists.

If a document both cites and names someone, it is counted once, as *cited*.

**Disambiguation.** Common names can produce false positives on the *named* route. For the full roll-out we spot-check a sample per person, and where needed we add an affiliation term (e.g. `Exeter`) or use Overton's `people.php` endpoint. The *cited* route is unaffected because DOIs are unique.

## 3. Architecture

```
staff.csv ──► build_dataset.py ──► dashboard/data/dashboard_data.json (+ .js, + .xlsx)
   │              │  overton_client.py  (rate-limited: ≤1 req/s, 429 back-off, pagination)
   │              │  classify.py        (source type, country/region, topic areas)
   │              └─ OpenAlex (ORCID → DOIs)
   └─ names, spelling variants, role, group, ORCID, headshot
dashboard/index.html  ── static page, no server needed; can be hosted on the university's SharePoint or web space
```

* The API key stays in an environment variable on the machine that runs the refresh. It is never placed in the dashboard.
* Refresh: run `build_dataset.py` monthly by hand, or on a schedule.
* At 1 request/second, 250 staff × (≈2 queries + pagination) takes roughly 15–40 minutes per full refresh.

## 4. Impact score (transparent and adjustable)

```
score = Σ over mentions of  source_weight × mention_weight × recency
source_weight:  Government 3 · IGO 3 · Think tank 2 · NGO 1.5 · Other 1
mention_weight: cited 1.0 · named 0.75
recency:        ≤3 yrs 1.0 · 3–6 yrs 0.6 · older 0.3
```

This is a *relative* indicator for comparing within the department, not a REF metric. The weights are a starting point to agree with you.

## 5. Phases

| Phase | Output | Effort |
|---|---|---|
| 0. Trial (done) | Working dashboard and Excel for Steffen Böhm and Stefano Pascucci on sample data; API client and pipeline | — |
| 1. Real-data pilot | API access enabled. Real data for the two pilot staff. Disambiguation check. Agree weights and topic list. | 2–3 days |
| 2. Sustainable Futures (≈20 staff) | Roster with ORCIDs and headshots. Full refresh. Branding finalised. Hosted page and Excel. Short handover guide. | 5–7 days |
| 3. Whole department (≈250 staff) | Bulk ORCID/DOI collection. Disambiguation QA at scale. Group and department roll-ups. Scheduled refresh. | 12–18 days |
| Optional: grey-literature analysis | Download and AI-review thousands of policy documents (themes, how our work is used: supportive, critical or descriptive). Scope agreed separately, subject to Overton's licensing terms on full text. | quote on request |
| Optional: staff chatbot | "Ask the database" search tool for staff. | quote on request |

## 6. Draft quote (to adjust before sending)

Indicative day rate: **£[RATE]/day** (placeholder, e.g. £250–£400).

| Scope | Days | Indicative cost |
|---|---|---|
| Real-data pilot (2 staff) | 2–3 | £[RATE × 2–3] |
| Sustainable Futures (≈20 staff), including pilot | 7–10 | £[RATE × 7–10] |
| Department of Management (≈250 staff), including the above | 19–28 | £[RATE × 19–28] |
| Ongoing monthly refresh and support | 0.5/month | £[RATE × 0.5]/month |

Not included: the Overton subscription and API access, which the university licence covers. API access must be enabled by Overton support (support@overton.io) and is not available on trial accounts.

## 7. What is needed from the department

1. **Overton API access** on the university licence, with a key issued to the person who runs the refresh.
2. **Staff list:** name, all spellings, group, role, ORCID (if any) and headshot (or permission to use the staff-profile photo).
3. The **brand toolkit**: official logo file and colour values (the colours in the page are placeholders).
4. Agreement on **where it is hosted** and who can see it. It names individuals, so internal access is recommended.
5. A data-protection check that staff are told about the dashboard (it uses only public policy documents, but it profiles named staff).

## 8. Open questions for Steffen

* Should "named" mentions count in the headline number, or appear only as a secondary figure?
* Are the topic areas right? (health, security, food, climate, circular economy, land, finance, governance, work and society)
* Should doctoral researchers and emeritus staff be included in the 250?
* Is a WhatsApp booking link for consultation sessions wanted? It was on the ideas list. This is separate from the dashboard; a simple `wa.me` link or a Calendly page would do.
