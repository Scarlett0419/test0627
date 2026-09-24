#!/usr/bin/env python3
"""Flow OAuth 2.0 Etsy (PKCE) en mode manuel. Pas de serveur HTTP, pas de timeout.

Usage :
  1. Cree ton app sur https://www.etsy.com/developers (note keystring + shared secret).
  2. Dans l'app Etsy, ajoute le callback : http://lvh.me:3003/callback
  3. Lance (methode recommandee, via variables d'environnement, rien dans argv/ps) :
     export ETSY_KEYSTRING=TA_KEYSTRING
     export ETSY_SHARED_SECRET=TON_SHARED_SECRET
     python3 etsy_oauth.py --shop-id TON_SHOP_ID
     Si les variables ne sont pas definies, le script les demande en saisie
     masquee (getpass). Passer --keystring/--secret en argument reste possible
     pour compatibilite mais expose le secret dans l'historique du shell ET
     dans la liste des process (ps aux) le temps de l'execution : a eviter.
  4. Le script affiche une URL Etsy. Tu la colles dans n'importe quel navigateur.
  5. Tu autorises sur Etsy.
  6. Le navigateur essaie d'aller sur lvh.me:3003/callback?code=XXX et echoue
     (c'est normal, pas de serveur). Mais l'URL dans la barre d'adresse
     contient le code.
  7. Tu copies l'URL complete depuis le navigateur et tu la colles dans le terminal.
  8. Le script extrait le code, fait l'echange et sauvegarde les credentials.

Aucune cle n'est affichee ni transmise ailleurs. Tout reste en local.
"""

from __future__ import annotations

import argparse
import base64
import getpass
import hashlib
import json
import os
import secrets
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path

CRED_PATH = Path.home() / ".claude" / "skills" / "etsy-automate" / ".etsy_credentials.json"
REDIRECT_URI = "http://lvh.me:3003/callback"
SCOPES = "listings_r listings_w listings_d shops_r shops_w"
AUTH_URL = "https://www.etsy.com/oauth/connect"
TOKEN_URL = "https://api.etsy.com/v3/public/oauth/token"


def make_pkce() -> tuple[str, str]:
    verifier = base64.urlsafe_b64encode(os.urandom(32)).rstrip(b"=").decode()
    challenge = base64.urlsafe_b64encode(
        hashlib.sha256(verifier.encode()).digest()
    ).rstrip(b"=").decode()
    return verifier, challenge


def extract_code(pasted: str, expected_state: str) -> tuple[str | None, str | None]:
    """Extrait code + state d'une URL collee ou du code brut.

    Si l'URL collee contient un state qui ne correspond pas a expected_state
    (celui genere pour cette session OAuth), on refuse : code renvoye a None
    pour forcer l'appelant a arreter (protection CSRF/state mismatch)."""
    pasted = pasted.strip()
    # Si c'est une URL complete
    if pasted.startswith("http"):
        parsed = urllib.parse.urlparse(pasted)
        params = urllib.parse.parse_qs(parsed.query)
        code = params.get("code", [None])[0]
        state = params.get("state", [None])[0]
        if state is not None and state != expected_state:
            return None, state
        return code, state
    # Sinon, on suppose que c'est le code brut (pas de state a verifier)
    return pasted, None


def exchange_code(keystring: str, code: str, verifier: str) -> dict:
    data = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "client_id": keystring,
        "redirect_uri": REDIRECT_URI,
        "code": code,
        "code_verifier": verifier,
    }).encode()
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--keystring", default=None,
                        help="App keystring (client id). Sinon lu depuis ETSY_KEYSTRING "
                             "ou demande en saisie masquee.")
    parser.add_argument("--secret", default=None,
                        help="App shared secret. Sinon lu depuis ETSY_SHARED_SECRET "
                             "ou demande en saisie masquee (getpass). Passer ce secret "
                             "en argument l'expose dans l'historique du shell et dans "
                             "ps aux : a eviter.")
    parser.add_argument("--shop-id", required=True, help="Shop ID de ta boutique.")
    args = parser.parse_args()

    # Priorite : argument explicite (compat) > variable d'environnement > prompt masque.
    keystring = args.keystring or os.environ.get("ETSY_KEYSTRING")
    if not keystring:
        keystring = getpass.getpass("App keystring (client id) : ").strip()
    if not keystring:
        print("ERREUR : keystring manquante. Arret.")
        return 1

    secret = args.secret or os.environ.get("ETSY_SHARED_SECRET")
    if not secret:
        secret = getpass.getpass("App shared secret (saisie masquee) : ").strip()
    if not secret:
        print("ERREUR : shared secret manquant. Arret.")
        return 1

    verifier, challenge = make_pkce()
    state = secrets.token_urlsafe(16)

    auth_params = urllib.parse.urlencode({
        "response_type": "code",
        "client_id": keystring,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    })
    url = f"{AUTH_URL}?{auth_params}"

    print()
    print("=" * 70)
    print("ETAPE 1 : Copie cette URL et colle-la dans Safari (ou Chrome) :")
    print("=" * 70)
    print()
    print(url)
    print()
    print("=" * 70)
    print("ETAPE 2 : Sur la page Etsy, clique 'Autoriser'.")
    print("ETAPE 3 : Le navigateur va afficher une page d'erreur (lvh.me can't")
    print("          connect ou similaire). C'est NORMAL.")
    print("ETAPE 4 : Copie l'URL COMPLETE depuis la barre d'adresse du")
    print("          navigateur et colle-la ci-dessous, puis appuie sur Entree.")
    print("=" * 70)
    print()
    pasted = input("URL ou code OAuth > ").strip()

    if not pasted:
        print("ERREUR : rien colle. Arret.")
        return 1

    code, received_state = extract_code(pasted, state)
    if not code:
        if received_state is not None:
            print("ERREUR : state OAuth invalide (securite). L'URL collee ne correspond")
            print("pas a la requete generee par ce script (mismatch CSRF possible, ou")
            print("mauvaise URL/session). Arret immediat. Relance le script pour")
            print("obtenir une nouvelle URL d'autorisation.")
        else:
            print("ERREUR : aucun code trouve dans l'URL. Verifie que tu as colle")
            print("la bonne URL (celle apres autorisation Etsy, qui contient ?code=...)")
        return 1

    print()
    print("Code recu. Echange contre les tokens Etsy...")
    try:
        tokens = exchange_code(keystring, code, verifier)
    except urllib.error.HTTPError as exc:
        print(f"ERREUR echange token : HTTP {exc.code}")
        print(exc.read().decode(errors="ignore"))
        print()
        print("Causes probables :")
        print("- Le code OAuth a expire (ils durent 5 min). Relance le script.")
        print("- La keystring ou le shared secret est incorrect.")
        print("- Le callback URL dans l'app Etsy ne correspond pas a lvh.me:3003/callback.")
        return 1

    creds = {
        "api_key": keystring,
        "shared_secret": secret,
        "access_token": tokens["access_token"],
        "refresh_token": tokens.get("refresh_token", ""),
        "shop_id": args.shop_id,
    }
    CRED_PATH.parent.mkdir(parents=True, exist_ok=True)
    CRED_PATH.write_text(json.dumps(creds, indent=2), encoding="utf-8")
    CRED_PATH.chmod(0o600)
    print()
    print("=" * 70)
    print(f"OK. Credentials sauvegardes dans {CRED_PATH}")
    print("Tu peux maintenant poster des brouillons via etsy_draft.py.")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
