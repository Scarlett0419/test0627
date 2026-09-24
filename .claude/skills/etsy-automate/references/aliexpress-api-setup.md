# AliExpress API Setup

Optionnel. Donne un accès propre aux prix, images et infos produit, sans anti-bot. Si non configuré, le skill utilise navigateur réel + WebSearch.

## Quelle API

**AliExpress Affiliate API (Portals)** — la plus accessible. Gratuite. Demande de rejoindre le programme affilié AliExpress et d'être approuvé (quelques jours).

Avantages :
- Données fiables et stables (prix, images haute réso, notes, commandes).
- Pas de blocage anti-bot.
- Bonus : commission affilié sur tes propres achats fournisseur.

L'alternative (AliExpress Dropshipping API, Open Platform) est plus lourde à obtenir. À éviter sauf besoin avancé.

## Setup (une fois)

1. Rejoindre le programme affilié AliExpress (AliExpress Portals / affiliate.aliexpress.com).
2. Créer une app dans la console développeur AliExpress Open Platform.
3. Récupérer **App Key** et **App Secret**.
4. Récupérer un **tracking ID** (pour les liens affiliés).

## Stockage des credentials

Hors des dossiers livrés, jamais dans un output :

```
~/.claude/skills/etsy-automate/.aliexpress_credentials.json
```

Format :
```json
{
  "app_key": "...",
  "app_secret": "...",
  "tracking_id": "..."
}
```

Gitignored. Ne jamais afficher.

## Détection

```bash
python3 ~/.claude/skills/etsy-automate/scripts/aliexpress_api.py --check
```

Renvoie CONFIGURE ou NON_CONFIGURE. Le SKILL.md l'appelle avant de choisir entre API et cascade scraping.

## Endpoints utiles

- Recherche produits : `aliexpress.affiliate.product.query`
- Détail produit : `aliexpress.affiliate.productdetail.get`
- Ces endpoints renvoient prix, images, volume de commandes, note.

## Limites

- Quotas d'appels selon ton niveau affilié.
- Signature des requêtes requise (HMAC avec l'App Secret).
- Si l'appel échoue, fallback sur navigateur réel + WebSearch, et signale-le.
