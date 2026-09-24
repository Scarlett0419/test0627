#!/usr/bin/env python3
"""Récupère les stats de performance des listings Etsy via API v3.

Usage :
  python3 etsy_stats.py --listing 4533096986
  python3 etsy_stats.py --listing 4533096986 --days 30
  python3 etsy_stats.py --all --days 7
  python3 etsy_stats.py --report --days 30
  python3 etsy_stats.py --report --days 30 --export csv
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

CRED_PATH = Path.home() / ".claude" / "skills" / "etsy-automate" / ".etsy_credentials.json"
API_BASE  = "https://api.etsy.com/v3/application"
TOKEN_URL = "https://api.etsy.com/v3/public/oauth/token"


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


def _do_request(req: urllib.request.Request, creds: dict, retry: bool = True) -> dict:
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


def api_get(path: str, creds: dict, params: dict | None = None) -> dict:
    url = f"{API_BASE}{path}"
    if params:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{url}?{query}"
    req = urllib.request.Request(url, method="GET")
    req.add_header("x-api-key", api_key_header(creds))
    req.add_header("Authorization", f"Bearer {creds['access_token']}")
    return _do_request(req, creds)


def date_range(days: int) -> tuple[int, int]:
    now = datetime.now(timezone.utc)
    end = int(now.timestamp())
    start = int((now - timedelta(days=days)).timestamp())
    return start, end


def get_listing_stats(listing_id: str, creds: dict, days: int) -> dict:
    start, end = date_range(days)
    try:
        return api_get(
            f"/shops/{creds['shop_id']}/listings/{listing_id}/stats",
            creds,
            {"start_date": start, "end_date": end, "granularity": "day"},
        )
    except SystemExit:
        return {}


def get_listing_info(listing_id: str, creds: dict) -> dict:
    try:
        return api_get(f"/listings/{listing_id}", creds)
    except SystemExit:
        return {}


def get_all_listings(creds: dict) -> list[dict]:
    result = api_get(
        f"/shops/{creds['shop_id']}/listings",
        creds,
        {"state": "active", "limit": 100},
    )
    return result.get("results", [])


def format_title(title: str, length: int = 40) -> str:
    return (title[:length] + "...") if len(title) > length else title


def cmd_listing(listing_id: str, days: int) -> int:
    creds = load_creds()
    info  = get_listing_info(listing_id, creds)
    stats = get_listing_stats(listing_id, creds, days)

    title = info.get("title", "?")
    views  = stats.get("views", 0)
    visits = stats.get("visits", 0)

    print(f"\nListing {listing_id} — {days} derniers jours")
    print(f"Titre    : {format_title(title, 60)}")
    print(f"Views    : {views}")
    print(f"Visits   : {visits}")

    if views and not stats.get("transactions"):
        print("\nSIGNAL : views mais 0 ventes. Revoir photo principale ou prix.")
    return 0


def cmd_report(days: int, export_csv: bool) -> int:
    creds    = load_creds()
    listings = get_all_listings(creds)

    if not listings:
        print("Aucun listing actif trouvé.")
        return 0

    rows = []
    for lst in listings:
        lid   = str(lst["listing_id"])
        stats = get_listing_stats(lid, creds, days)
        rows.append({
            "listing_id": lid,
            "title":      lst.get("title", ""),
            "views":      stats.get("views", 0),
            "visits":     stats.get("visits", 0),
            "price":      lst.get("price", {}).get("amount", 0),
            "state":      lst.get("state", ""),
        })

    rows.sort(key=lambda r: r["views"], reverse=True)

    start_dt = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    end_dt   = datetime.now().strftime("%Y-%m-%d")
    print(f"\nRAPPORT PERFORMANCE — {days} derniers jours")
    print(f"Boutique : {creds['shop_id']}")
    print(f"Période  : {start_dt} → {end_dt}\n")
    print(f"{'listing_id':<14} {'titre':<42} {'views':>6} {'visits':>7} {'prix':>6}")
    print("-" * 80)
    for r in rows:
        title = format_title(r["title"])
        print(f"{r['listing_id']:<14} {title:<42} {r['views']:>6} {r['visits']:>7} {r['price']:>6}")

    if export_csv:
        fname = f"etsy-stats-{end_dt}.csv"
        with open(fname, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["listing_id", "title", "views", "visits", "price", "state"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nExporté : {fname}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Stats de performance Etsy via API v3.")
    parser.add_argument("--listing", metavar="ID",   help="Stats d'un listing spécifique.")
    parser.add_argument("--all",     action="store_true", help="Stats de tous les listings actifs.")
    parser.add_argument("--report",  action="store_true", help="Rapport comparatif trié par views.")
    parser.add_argument("--days",    type=int, default=7,  help="Période en jours (défaut : 7).")
    parser.add_argument("--export",  metavar="FORMAT", choices=["csv"], help="Exporter en CSV.")
    args = parser.parse_args()

    if args.listing:
        return cmd_listing(args.listing, args.days)
    if args.all or args.report:
        return cmd_report(args.days, args.export == "csv")

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
