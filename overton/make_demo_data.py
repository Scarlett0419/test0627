"""Generate SAMPLE data in the real dashboard schema so the layout can be reviewed before
API access is set up. Every record is invented. The dashboard shows a 'Sample data' banner.

    python make_demo_data.py
"""
from __future__ import annotations

import random
from pathlib import Path

from build_dataset import load_staff, write_outputs
from classify import REGIONS

HERE = Path(__file__).parent

SOURCES = [
    ("UK government department (sample)", "Government", "United Kingdom"),
    ("UK parliamentary committee (sample)", "Government", "United Kingdom"),
    ("Scottish government (sample)", "Government", "United Kingdom"),
    ("German federal ministry (sample)", "Government", "Germany"),
    ("Dutch government agency (sample)", "Government", "Netherlands"),
    ("Italian ministry (sample)", "Government", "Italy"),
    ("European Commission DG (sample)", "Government", "European Union"),
    ("UN food & agriculture body (sample)", "Intergovernmental (IGO)", "International (IGO)"),
    ("UN environment body (sample)", "Intergovernmental (IGO)", "International (IGO)"),
    ("OECD directorate (sample)", "Intergovernmental (IGO)", "International (IGO)"),
    ("London policy think tank (sample)", "Think tank", "United Kingdom"),
    ("Brussels think tank (sample)", "Think tank", "Belgium"),
    ("US research institute (sample)", "Think tank", "United States of America"),
    ("Canadian policy institute (sample)", "Think tank", "Canada"),
    ("Brazilian policy centre (sample)", "Think tank", "Brazil"),
    ("Kenyan development NGO (sample)", "NGO / civil society", "Kenya"),
    ("Indian research foundation (sample)", "Think tank", "India"),
    ("Australian government agency (sample)", "Government", "Australia"),
    ("South African think tank (sample)", "Think tank", "South Africa"),
    ("International NGO (sample)", "NGO / civil society", "International (IGO)"),
]

TITLES = {
    "steffen-bohm": [
        ("Carbon markets and offsetting: options for reform", ["Climate & Energy", "Finance & Business"]),
        ("Land use, nature and the just transition", ["Land & Biodiversity", "Work & Society"]),
        ("Governing voluntary carbon credits", ["Climate & Energy", "Governance & Policy"]),
        ("Corporate accountability in climate policy", ["Governance & Policy", "Finance & Business"]),
        ("Community land ownership and rural resilience", ["Land & Biodiversity", "Security"]),
        ("Alternative organisations for sustainability", ["Work & Society"]),
        ("Biofuels, land and food security", ["Food & Agriculture", "Security", "Land & Biodiversity"]),
    ],
    "stefano-pascucci": [
        ("Circular food systems: a roadmap", ["Circular Economy", "Food & Agriculture"]),
        ("Reducing food waste across supply chains", ["Circular Economy", "Food & Agriculture"]),
        ("Agri-food cooperatives and rural development", ["Food & Agriculture", "Work & Society"]),
        ("Business models for the circular bioeconomy", ["Circular Economy", "Finance & Business"]),
        ("Short food supply chains and public health", ["Food & Agriculture", "Health"]),
        ("Food system resilience after the pandemic", ["Food & Agriculture", "Security", "Health"]),
        ("Packaging, waste and extended producer responsibility", ["Circular Economy", "Governance & Policy"]),
    ],
}

COUNTS = {"steffen-bohm": 64, "stefano-pascucci": 91}


def main() -> None:
    rng = random.Random(42)
    staff = load_staff(HERE / "staff.csv")
    mentions = []
    for p in staff:
        titles = TITLES.get(p["id"], TITLES["steffen-bohm"])
        for i in range(COUNTS.get(p["id"], 30)):
            src, stype, country = rng.choice(SOURCES)
            title, topics = rng.choice(titles)
            year = rng.choices(range(2014, 2027), weights=[1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 6])[0]
            month = rng.randint(1, 10 if year == 2026 else 12)
            kind = rng.choices(["cited", "named"], weights=[3, 1])[0]
            mentions.append({
                "staff_id": p["id"],
                "policy_document_id": f"sample-{p['id']}-{i}",
                "title": f"{title} (sample {i + 1})",
                "source_title": src,
                "source_type": stype,
                "country": country,
                "region": REGIONS.get(country, "Other"),
                "published_on": f"{year}-{month:02d}-{rng.randint(1, 28):02d}",
                "topics": topics,
                "mention_type": kind,
                "cited_doi": "10.0000/sample" if kind == "cited" else None,
                "snippet": "Sample text: this is where the passage that names or cites the staff member appears.",
                "document_url": None,
            })
    write_outputs(staff, mentions, HERE / "dashboard" / "data", demo=True)
    print(f"Wrote {len(mentions)} sample mentions")


if __name__ == "__main__":
    main()
