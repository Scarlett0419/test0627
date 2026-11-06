"""Pull Overton data for every staff member in staff.csv and write the dashboard dataset.

Two kinds of mention per person:
  * named  - the person's name (any spelling variant) appears in a policy document's full text
  * cited  - a policy document cites one of their DOIs (DOIs from OpenAlex via ORCID, or a dois/<id>.txt file)

Usage:
    export OVERTON_API_KEY=...
    python build_dataset.py --staff staff.csv --out dashboard/data
    python build_dataset.py --only steffen-bohm --max-pages 3       # quick trial
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from classify import to_mention
from overton_client import OvertonClient, name_query

HERE = Path(__file__).parent


def load_staff(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["name_variants"] = [v.strip() for v in r["name_variants"].split("|") if v.strip()] or [r["name"]]
    return rows


def staff_dois(person: dict) -> list[str]:
    """DOIs from dois/<id>.txt if present, else OpenAlex works for the ORCID (free, no key)."""
    local = HERE / "dois" / f"{person['id']}.txt"
    if local.exists():
        return [l.strip() for l in local.read_text().splitlines() if l.strip()]
    orcid = (person.get("orcid") or "").strip()
    if not orcid:
        return []
    dois, cursor = [], "*"
    while cursor:
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(
            {"filter": f"author.orcid:{orcid}", "per-page": 200, "cursor": cursor, "select": "doi"})
        with urllib.request.urlopen(url, timeout=60) as r:
            data = json.load(r)
        dois += [w["doi"].replace("https://doi.org/", "") for w in data["results"] if w.get("doi")]
        cursor = data["meta"].get("next_cursor") if data["results"] else None
    return dois


def collect(client: OvertonClient, person: dict, max_pages: int | None, extra: dict) -> list[dict]:
    seen: dict[str, dict] = {}
    for doc in client.iter_documents(name_query(person["name_variants"]), max_pages=max_pages, sort="date", **extra):
        m = to_mention(doc, person["id"], "named")
        seen[m["policy_document_id"]] = m
    dois = staff_dois(person)
    if dois:
        set_id = client.generate_id_set(dois)
        for doc in client.documents_citing(set_id, max_pages=max_pages, sort="date", **extra):
            m = to_mention(doc, person["id"], "cited")
            key = m["policy_document_id"]
            # A document that both names and cites someone counts once, as a citation (stronger signal).
            seen[key] = m
    return list(seen.values())


def write_outputs(staff: list[dict], mentions: list[dict], out: Path, demo: bool = False) -> None:
    out.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "demo": demo,
        "staff": [{k: p.get(k) for k in ("id", "name", "name_variants", "role", "group", "department", "orcid", "headshot")} for p in staff],
        "mentions": mentions,
    }
    (out / "dashboard_data.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    # .js copy so dashboard/index.html works when opened straight from disk (file://).
    (out / "dashboard_data.js").write_text("window.DASHBOARD_DATA = " + json.dumps(payload, ensure_ascii=False) + ";\n", encoding="utf-8")
    write_excel(payload, out / "overton_mentions.xlsx")


def write_excel(payload: dict, path: Path) -> None:
    try:
        from openpyxl import Workbook
    except ImportError:
        print("openpyxl not installed; skipping Excel export", file=sys.stderr)
        return
    names = {p["id"]: p["name"] for p in payload["staff"]}
    wb = Workbook()
    ws = wb.active
    ws.title = "Summary"
    ws.append(["Staff member", "Total mentions", "Cited", "Named", "Countries", "Most recent"])
    for p in payload["staff"]:
        ms = [m for m in payload["mentions"] if m["staff_id"] == p["id"]]
        ws.append([p["name"], len(ms), sum(m["mention_type"] == "cited" for m in ms),
                   sum(m["mention_type"] == "named" for m in ms), len({m["country"] for m in ms}),
                   max((m["published_on"] for m in ms), default="")])
    ws2 = wb.create_sheet("Mentions")
    cols = ["staff", "published_on", "title", "source_title", "source_type", "country", "region",
            "topics", "mention_type", "cited_doi", "document_url"]
    ws2.append(cols)
    for m in sorted(payload["mentions"], key=lambda m: m["published_on"], reverse=True):
        ws2.append([names.get(m["staff_id"]), m["published_on"], m["title"], m["source_title"], m["source_type"],
                    m["country"], m["region"], "; ".join(m["topics"]), m["mention_type"], m.get("cited_doi"),
                    m.get("document_url")])
    wb.save(path)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--staff", type=Path, default=HERE / "staff.csv")
    ap.add_argument("--out", type=Path, default=HERE / "dashboard" / "data")
    ap.add_argument("--only", nargs="*", help="staff ids to include")
    ap.add_argument("--max-pages", type=int, default=None, help="cap pages per query (20 results/page)")
    ap.add_argument("--param", action="append", default=[], metavar="KEY=VALUE",
                    help="extra Overton filter copied from 'Generate API call', e.g. --param source_country=UK")
    args = ap.parse_args()

    extra = dict(p.split("=", 1) for p in args.param)
    staff = load_staff(args.staff)
    if args.only:
        staff = [p for p in staff if p["id"] in args.only]
    client = OvertonClient()
    mentions: list[dict] = []
    for p in staff:
        got = collect(client, p, args.max_pages, extra)
        print(f"{p['name']}: {len(got)} documents", file=sys.stderr)
        mentions += got
    write_outputs(staff, mentions, args.out)
    print(f"Wrote {len(mentions)} mentions to {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
