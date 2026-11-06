"""Turn raw Overton results into normalised mention rows for the dashboard."""
from __future__ import annotations

import re

# Topic areas from the brief (health, security, food, ...). Keyword matching on title/snippet,
# used only when Overton itself does not return topic/SDG tags for a document.
TOPICS: dict[str, list[str]] = {
    "Climate & Energy": ["climate", "carbon", "emission", "net zero", "energy", "decarboni", "fossil"],
    "Food & Agriculture": ["food", "agri", "farm", "crop", "diet", "nutrition", "fisher"],
    "Land & Biodiversity": ["land", "forest", "biodiversity", "nature", "ecosystem", "soil", "deforest"],
    "Circular Economy": ["circular", "waste", "recycl", "reuse", "resource efficien", "packaging"],
    "Health": ["health", "disease", "pandemic", "medical", "wellbeing", "obesity"],
    "Security": ["security", "conflict", "defence", "defense", "resilien", "migration"],
    "Finance & Business": ["finance", "business", "corporate", "investment", "market", "trade", "supply chain"],
    "Governance & Policy": ["governance", "regulat", "policy", "law", "democra", "accountab"],
    "Work & Society": ["labour", "labor", "employment", "inequality", "community", "social", "gender"],
}

SOURCE_TYPES = {
    "government": "Government",
    "igo": "Intergovernmental (IGO)",
    "think tank": "Think tank",
    "thinktank": "Think tank",
    "ngo": "NGO / civil society",
    "other": "Other",
}

# Overton country labels -> names used by the world-atlas topojson in the dashboard map.
COUNTRY_NAMES = {
    "UK": "United Kingdom", "USA": "United States of America", "US": "United States of America",
    "EU": "European Union", "IGO": "International (IGO)", "UAE": "United Arab Emirates",
    "South Korea": "South Korea", "Czech Republic": "Czechia",
}

REGIONS = {
    "United Kingdom": "Europe", "Germany": "Europe", "France": "Europe", "Netherlands": "Europe",
    "Italy": "Europe", "Spain": "Europe", "Ireland": "Europe", "Belgium": "Europe", "Sweden": "Europe",
    "Denmark": "Europe", "Norway": "Europe", "Finland": "Europe", "Switzerland": "Europe",
    "Austria": "Europe", "Poland": "Europe", "Portugal": "Europe", "European Union": "Europe",
    "United States of America": "North America", "Canada": "North America", "Mexico": "Latin America",
    "Brazil": "Latin America", "Argentina": "Latin America", "Chile": "Latin America", "Colombia": "Latin America",
    "Australia": "Oceania", "New Zealand": "Oceania",
    "India": "Asia", "China": "Asia", "Japan": "Asia", "South Korea": "Asia", "Indonesia": "Asia",
    "South Africa": "Africa", "Kenya": "Africa", "Nigeria": "Africa", "Ghana": "Africa", "Ethiopia": "Africa",
    "International (IGO)": "International",
}

# Weights for the impact score. Documented in PLAN.md so the score is explainable.
SOURCE_WEIGHT = {"Government": 3.0, "Intergovernmental (IGO)": 3.0, "Think tank": 2.0, "NGO / civil society": 1.5, "Other": 1.0}
MENTION_WEIGHT = {"cited": 1.0, "named": 0.75}


def first(d: dict, *keys, default=None):
    for k in keys:
        v = d.get(k)
        if v not in (None, "", []):
            return v
    return default


def source_type(raw: str | None) -> str:
    return SOURCE_TYPES.get((raw or "other").strip().lower(), "Other")


def country_name(raw: str | None) -> str:
    raw = (raw or "Unknown").strip()
    return COUNTRY_NAMES.get(raw, raw)


def topics_for(doc: dict, text: str) -> list[str]:
    tagged = first(doc, "topics", "sdg_categories", "sdgs", "classifications")
    if tagged:
        return [t if isinstance(t, str) else str(first(t, "name", "title", "label", default=t)) for t in tagged][:5]
    low = text.lower()
    hits = [topic for topic, kws in TOPICS.items() if any(k in low for k in kws)]
    return hits or ["Other"]


def to_mention(doc: dict, staff_id: str, mention_type: str, cited_doi: str | None = None) -> dict:
    src = doc.get("source") or {}
    title = first(doc, "translated_title", "title", default="Untitled")
    snippet = first(doc, "snippet", "highlight", "snippets", default="")
    if isinstance(snippet, list):
        snippet = " … ".join(map(str, snippet))
    snippet = re.sub(r"<[^>]+>", "", str(snippet))
    country = country_name(first(src, "country", default=first(doc, "country")))
    return {
        "staff_id": staff_id,
        "policy_document_id": first(doc, "policy_document_id", "pdf_document_id"),
        "title": title,
        "source_title": first(src, "title", default="Unknown source"),
        "source_type": source_type(first(src, "type")),
        "country": country,
        "region": REGIONS.get(country, "Other"),
        "published_on": str(first(doc, "published_on", "published_date", "date", default=""))[:10],
        "topics": topics_for(doc, f"{title} {snippet}"),
        "mention_type": mention_type,
        "cited_doi": cited_doi,
        "snippet": snippet[:400],
        "document_url": first(doc, "document_url", "pdf_url"),
    }
