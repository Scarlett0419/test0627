#!/usr/bin/env python3
"""Cree un workspace EtsyAutomate sur le Bureau."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "boutique"


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shop", required=True, help="Nom de la boutique.")
    parser.add_argument(
        "--desktop",
        default=str(Path.home() / "Desktop"),
        help="Chemin du Bureau. Defaut ~/Desktop.",
    )
    args = parser.parse_args()

    slug = slugify(args.shop)
    root = Path(args.desktop).expanduser() / f"EtsyAutomate-{slug}"
    today = date.today().isoformat()

    (root / "fiches").mkdir(parents=True, exist_ok=True)

    write_if_missing(
        root / "shop-identity.md",
        f"""# Shop Identity Card — {args.shop}

Cree le {today}. A remplir une seule fois.

## Positionnement
[ ] Budget  [ ] Mid-range  [ ] Luxury

## Marche cible
Geographie :
Langue des fiches :
Acheteur type :

## Ton de voix
3 adjectifs :
Phrases a utiliser :
Phrases a eviter :

## Style visuel
Palette couleurs :
Mood des images :
References visuelles :

## Marge cible
[ ] 30%  [ ] 50%  [ ] 70%
""",
    )

    write_if_missing(
        root / "niche-research.md",
        f"# Niche Research — {args.shop}\n\nCree le {today}.\n\n",
    )

    write_if_missing(
        root / "DELIVERY-MANIFEST.md",
        f"""# Delivery Manifest — {args.shop}

Cree le {today}.

## Contenu

- shop-identity.md
- niche-research.md
- fiches/[nom-produit]/fiche.md
- fiches/[nom-produit]/photos/

## Securite

Aucune cle API, aucun token, aucun credential dans ce dossier.
""",
    )

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
