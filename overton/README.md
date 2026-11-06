# Overton policy impact dashboard

This folder holds a Python client for the [Overton API](https://app.overton.io/swagger.php), a pipeline that maps staff mentions and citations in policy documents, and a static dashboard. See [PLAN.md](PLAN.md) for the plan and the draft proposal.

## Quick start

```bash
cd overton
python make_demo_data.py              # sample data, no key needed
open dashboard/index.html             # or double-click it
```

With API access (no third-party packages are needed; `openpyxl` adds the Excel export):

```bash
export OVERTON_API_KEY=...            # Overton → Export → "Generate API call" shows your key
python build_dataset.py --only steffen-bohm stefano-pascucci --max-pages 3   # trial
python build_dataset.py                                                      # everyone in staff.csv
```

Extra Overton filters (copy them from a "Generate API call" URL) can be passed through:
`--param source_country=UK`.

## Files

| File | Purpose |
|---|---|
| `overton_client.py` | API client: auth, ≤1 req/s throttle, 429/5xx back-off, pagination, `documents.php`, `people.php`, `articles.php`, `generate_id_set.php` |
| `classify.py` | Normalises results: source type, country/region, topic areas |
| `build_dataset.py` | Per staff member, finds "named" mentions (name variants) and "cited" mentions (DOIs via ORCID/OpenAlex or `dois/<id>.txt`), then writes JSON, JS and XLSX |
| `staff.csv` | Roster: `name_variants` separated by `\|`, `orcid`, `headshot` path |
| `make_demo_data.py` | Sample data in the same schema (the dashboard shows a banner) |
| `dashboard/index.html` | The dashboard. Add `assets/logo.svg` and `assets/headshots/<id>.jpg` |
| `tests/` | `python -m unittest discover -s tests` |

The API key is read from the environment only. Do not commit it or put it in the dashboard.
