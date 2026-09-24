#!/usr/bin/env python3
"""Detecte la config de l'API Affiliate AliExpress, ou interroge un produit.

Usage :
  python3 aliexpress_api.py --check
  python3 aliexpress_api.py --query "stainless steel hoop earrings"
  python3 aliexpress_api.py --detail PRODUCT_ID

Credentials attendus :
  ~/.claude/skills/etsy-automate/.aliexpress_credentials.json
  { "app_key", "app_secret", "tracking_id" }

Si non configure, le skill retombe sur navigateur reel + WebSearch.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import time
from pathlib import Path

try:
    import urllib.request
    import urllib.error
    import urllib.parse
except ImportError:
    urllib = None

CRED_PATH = Path.home() / ".claude" / "skills" / "etsy-automate" / ".aliexpress_credentials.json"
API_GATEWAY = "https://api-sg.aliexpress.com/sync"


def load_creds() -> dict | None:
    if not CRED_PATH.exists():
        return None
    try:
        data = json.loads(CRED_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    required = {"app_key", "app_secret"}
    if not required.issubset(data.keys()):
        return None
    return data


def check() -> int:
    creds = load_creds()
    if creds is None:
        print("NON_CONFIGURE")
        print("Credentials absents ou incomplets. Voir references/aliexpress-api-setup.md")
        print("Fallback : navigateur reel + WebSearch.")
        return 1
    print("CONFIGURE")
    print("app_key : configured")
    return 0


def sign(params: dict, secret: str) -> str:
    """Signature TOP/AliExpress : HMAC-SHA256 sur les params tries, en majuscules hex."""
    ordered = "".join(f"{k}{params[k]}" for k in sorted(params))
    digest = hmac.new(secret.encode(), ordered.encode(), hashlib.sha256).hexdigest()
    return digest.upper()


def call(method: str, creds: dict, extra: dict) -> dict:
    params = {
        "app_key": creds["app_key"],
        "method": method,
        "sign_method": "sha256",
        "timestamp": str(int(time.time() * 1000)),
        "v": "2.0",
    }
    params.update({k: str(v) for k, v in extra.items()})
    params["sign"] = sign(params, creds["app_secret"])
    url = f"{API_GATEWAY}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read().decode("utf-8"))


def query(term: str) -> int:
    creds = load_creds()
    if creds is None:
        print("NON_CONFIGURE")
        return 1
    extra = {"keywords": term, "target_currency": "EUR", "page_size": "20"}
    tracking = creds.get("tracking_id")
    if tracking:
        extra["tracking_id"] = tracking
    try:
        result = call("aliexpress.affiliate.product.query", creds, extra)
    except urllib.error.HTTPError as exc:
        print(f"ERREUR API : {exc.code}. Fallback navigateur reel + WebSearch.")
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


def detail(product_id: str) -> int:
    creds = load_creds()
    if creds is None:
        print("NON_CONFIGURE")
        return 1
    extra = {"product_ids": product_id, "target_currency": "EUR"}
    tracking = creds.get("tracking_id")
    if tracking:
        extra["tracking_id"] = tracking
    try:
        result = call("aliexpress.affiliate.productdetail.get", creds, extra)
    except urllib.error.HTTPError as exc:
        print(f"ERREUR API : {exc.code}. Fallback navigateur reel + WebSearch.")
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Verifie la config.")
    parser.add_argument("--query", help="Recherche produits par mots-cles.")
    parser.add_argument("--detail", help="Detail d'un produit par ID.")
    args = parser.parse_args()

    if args.check:
        return check()
    if args.query:
        return query(args.query)
    if args.detail:
        return detail(args.detail)
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
