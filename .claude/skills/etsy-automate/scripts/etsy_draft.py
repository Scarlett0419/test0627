#!/usr/bin/env python3
"""Gestion de fiches Etsy via API v3.

Usage :
  python3 etsy_draft.py --check
  python3 etsy_draft.py --listing path/to/listing.json
  python3 etsy_draft.py --delete 4526336412 4533080471

JSON de listing attendu :
  {
    "title": "...",
    "description": "...",
    "price": 18.90,
    "quantity": 999,
    "tags": ["tag1", "..."],          -- max 13
    "taxonomy_id": 1234,
    "who_made": "i_did",
    "when_made": "made_to_order",
    "images": ["/chemin/absolu/hero.jpg"],
    "attributes": [                   -- optionnel
      {"property_id": 200, "value_ids": [5], "values": []},
      {"property_id": 507, "value_ids": [], "values": ["Cotton"]}
    ]
  }

NOTE : who_made "someone_else" est rejeté par l'API Etsy (400). Utiliser "i_did" +
when_made "made_to_order" pour les produits sourcés/fabriqués à la commande.

Credentials : ~/.claude/skills/etsy-automate/.etsy_credentials.json
  { "api_key", "shared_secret", "access_token", "refresh_token", "shop_id" }
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

CRED_PATH = Path.home() / ".claude" / "skills" / "etsy-automate" / ".etsy_credentials.json"
API_BASE  = "https://api.etsy.com/v3/application"
TOKEN_URL = "https://api.etsy.com/v3/public/oauth/token"


# ---------------------------------------------------------------------------
# Credentials
# ---------------------------------------------------------------------------

def load_creds() -> dict:
    if not CRED_PATH.exists():
        sys.exit("ERREUR : credentials absents. Lancer etsy_oauth.py d'abord.")
    data = json.loads(CRED_PATH.read_text(encoding="utf-8"))
    required = {"api_key", "shared_secret", "access_token", "refresh_token", "shop_id"}
    missing = required - data.keys()
    if missing:
        sys.exit(f"ERREUR : champs manquants dans credentials : {missing}")
    return data


def save_creds(creds: dict) -> None:
    CRED_PATH.write_text(json.dumps(creds, indent=2), encoding="utf-8")
    CRED_PATH.chmod(0o600)


def refresh_token(creds: dict) -> dict:
    body = urllib.parse.urlencode({
        "grant_type":    "refresh_token",
        "client_id":     creds["api_key"],
        "refresh_token": creds["refresh_token"],
    }).encode()
    req = urllib.request.Request(TOKEN_URL, data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    try:
        with urllib.request.urlopen(req) as resp:
            tokens = json.loads(resp.read().decode())
        creds["access_token"] = tokens["access_token"]
        if "refresh_token" in tokens:
            creds["refresh_token"] = tokens["refresh_token"]
        save_creds(creds)
        return creds
    except urllib.error.HTTPError as exc:
        sys.exit(f"ERREUR refresh token : {exc.code} {exc.read().decode()[:200]}")


def api_key_header(creds: dict) -> str:
    return f"{creds['api_key']}:{creds['shared_secret']}"


# ---------------------------------------------------------------------------
# HTTP helpers (avec retry auto apres refresh token)
# ---------------------------------------------------------------------------

def _do_request(req: urllib.request.Request, creds: dict, retry: bool = True):
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 401 and retry:
            creds = refresh_token(creds)
            req.remove_header("Authorization")
            req.add_header("Authorization", f"Bearer {creds['access_token']}")
            return _do_request(req, creds, retry=False)
        body = exc.read().decode("utf-8", errors="ignore")
        sys.exit(f"ERREUR API Etsy {exc.code} {exc.reason} : {body[:300]}")


def api_get(path: str, creds: dict) -> dict:
    req = urllib.request.Request(f"{API_BASE}{path}", method="GET")
    req.add_header("x-api-key", api_key_header(creds))
    req.add_header("Authorization", f"Bearer {creds['access_token']}")
    return _do_request(req, creds)


def api_post(path: str, creds: dict, payload: dict) -> dict:
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
    )
    req.add_header("x-api-key", api_key_header(creds))
    req.add_header("Authorization", f"Bearer {creds['access_token']}")
    req.add_header("Content-Type", "application/json")
    return _do_request(req, creds)


def api_put(path: str, creds: dict, payload: dict) -> dict:
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=json.dumps(payload).encode("utf-8"),
        method="PUT",
    )
    req.add_header("x-api-key", api_key_header(creds))
    req.add_header("Authorization", f"Bearer {creds['access_token']}")
    req.add_header("Content-Type", "application/json")
    return _do_request(req, creds)


def api_delete(path: str, creds: dict) -> None:
    req = urllib.request.Request(f"{API_BASE}{path}", method="DELETE")
    req.add_header("x-api-key", api_key_header(creds))
    req.add_header("Authorization", f"Bearer {creds['access_token']}")
    try:
        with urllib.request.urlopen(req) as resp:
            resp.read()
    except urllib.error.HTTPError as exc:
        if exc.code == 401:
            creds = refresh_token(creds)
            req.remove_header("Authorization")
            req.add_header("Authorization", f"Bearer {creds['access_token']}")
            with urllib.request.urlopen(req) as resp:
                resp.read()
        else:
            body = exc.read().decode("utf-8", errors="ignore")
            sys.exit(f"ERREUR DELETE {exc.code} : {body[:200]}")


def post_image(listing_id: int, creds: dict, image_path: str) -> None:
    boundary = "----etsyautomateboundary"
    path = Path(image_path)
    suffix = path.suffix.lower()
    mime = "image/png" if suffix == ".png" else "image/jpeg"
    file_bytes = path.read_bytes()
    body  = f"--{boundary}\r\n".encode()
    body += f'Content-Disposition: form-data; name="image"; filename="{path.name}"\r\n'.encode()
    body += f"Content-Type: {mime}\r\n\r\n".encode()
    body += file_bytes
    body += f"\r\n--{boundary}--\r\n".encode()

    url = f"{API_BASE}/shops/{creds['shop_id']}/listings/{listing_id}/images"
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("x-api-key", api_key_header(creds))
    req.add_header("Authorization", f"Bearer {creds['access_token']}")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    _do_request(req, creds)


def set_property(listing_id: int, creds: dict, prop: dict) -> None:
    pid = prop["property_id"]
    payload = {
        "value_ids": prop.get("value_ids", []),
        "values":    prop.get("values", []),
    }
    if prop.get("scale_id"):
        payload["scale_id"] = prop["scale_id"]
    api_put(f"/listings/{listing_id}/properties/{pid}", creds, payload)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_check() -> int:
    creds = load_creds()
    print("CONFIGURE")
    print(f"shop_id : {creds['shop_id']}")
    return 0


def cmd_create(listing_path: str) -> int:
    creds = load_creds()
    listing = json.loads(Path(listing_path).read_text(encoding="utf-8"))

    payload = {
        "quantity":    listing.get("quantity", 999),
        "title":       listing["title"],
        "description": listing["description"],
        "price":       listing["price"],
        "who_made":    listing.get("who_made", "i_did"),
        "when_made":   listing.get("when_made", "made_to_order"),
        "taxonomy_id": listing["taxonomy_id"],
        "tags":        listing.get("tags", [])[:13],
        "state":       "draft",
    }
    for opt in ("shipping_profile_id", "readiness_state_id", "type"):
        if listing.get(opt):
            payload[opt] = listing[opt]

    result     = api_post(f"/shops/{creds['shop_id']}/listings", creds, payload)
    listing_id = result["listing_id"]
    print(f"Brouillon cree. listing_id={listing_id}")

    # Images
    images = listing.get("images", [])
    ok = 0
    for img in images:
        if not Path(img).exists():
            print(f"  image introuvable, ignoree : {img}")
            continue
        try:
            post_image(listing_id, creds, img)
            ok += 1
        except SystemExit as exc:
            print(f"  echec upload {img} : {exc}")
    print(f"Images uploadees : {ok}/{len(images)}")

    # Attributes
    attrs = listing.get("attributes", [])
    if attrs:
        ok_attr = 0
        for prop in attrs:
            try:
                set_property(listing_id, creds, prop)
                ok_attr += 1
            except SystemExit as exc:
                print(f"  echec attribut property_id={prop['property_id']} : {exc}")
        print(f"Attributs definis : {ok_attr}/{len(attrs)}")

    print(f"Brouillon pret. listing_id={listing_id}")
    print("Publication : a faire manuellement dans le dashboard Etsy.")
    return 0


def cmd_delete(listing_ids: list[str]) -> int:
    creds = load_creds()
    print(f"Brouillons a supprimer : {', '.join(listing_ids)}")
    confirm = input("Confirmer la suppression ? (oui/N) : ").strip().lower()
    if confirm != "oui":
        print("Annule.")
        return 0
    for lid in listing_ids:
        try:
            api_delete(f"/listings/{lid}", creds)
            print(f"Supprime : {lid}")
        except SystemExit as exc:
            print(f"Echec suppression {lid} : {exc}")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Gestion de fiches Etsy via API v3."
    )
    parser.add_argument("--check",   action="store_true",
                        help="Verifie la config.")
    parser.add_argument("--listing", metavar="PATH",
                        help="Chemin du JSON de listing a poster en draft.")
    parser.add_argument("--delete",  metavar="LISTING_ID", nargs="+",
                        help="Supprime un ou plusieurs brouillons (confirmation demandee).")
    args = parser.parse_args()

    if args.check:
        return cmd_check()

    if args.delete:
        return cmd_delete(args.delete)

    if args.listing:
        return cmd_create(args.listing)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
