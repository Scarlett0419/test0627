# Performance Tracking

Module de suivi automatique des métriques de listing Etsy via API v3. S'appuie sur les endpoints Stats d'Etsy pour mesurer la performance des fiches créées par le skill.

## Ce que ça mesure

Par listing, par période :
- **Views** : affichages de la fiche (listing page views).
- **Visits** : sessions uniques ayant vu la fiche.
- **CTR implicite** : views / impressions dans les recherches (non accessible directement via API, proxy via stats).
- **Transactions** : ventes (si l'accès transactions est accordé).
- **Favoris** : nombre de fois où la fiche a été mise en favoris.

## Accès API

Endpoint : `GET /v3/application/shops/{shop_id}/listings/{listing_id}/stats`

Params :
- `start_date` : timestamp UNIX début de période
- `end_date` : timestamp UNIX fin de période
- `granularity` : `day` (par jour) ou `week` ou `month`

Scopes requis : `listings_r` (déjà dans l'OAuth par défaut).

## Script : `scripts/etsy_stats.py`

```python
#!/usr/bin/env python3
"""Récupère les stats de performance d'un ou plusieurs listings Etsy.

Usage :
  python3 etsy_stats.py --listing 4533096986
  python3 etsy_stats.py --listing 4533096986 --days 30
  python3 etsy_stats.py --all --days 7
  python3 etsy_stats.py --report --days 30
"""
```

### Commandes disponibles

| Commande | Description |
|----------|-------------|
| `--listing ID [--days N]` | Stats d'un listing sur N jours (défaut : 7) |
| `--all [--days N]` | Stats de tous les listings actifs de la boutique |
| `--report [--days N]` | Rapport comparatif : tous les listings triés par views |
| `--export csv` | Exporte le rapport en CSV dans le dossier courant |

### Output exemple

```
RAPPORT PERFORMANCE — 30 derniers jours
Boutique : [shop_id]
Période : 2026-06-06 → 2026-07-06

listing_id  titre (40 chars)               views  visits  favs  ventes
4533096986  Bath Towel Set, 3 Piece...        142      89    12       0
4526336412  [BROUILLON]                         0       0     0       0

SIGNAUX :
- 4533096986 : 142 views, 0 ventes → CTR ok, taux de conversion nul.
  Cause probable : prix, photos, ou description à revoir.
  Action : A/B test photo principale ou baisse de prix de 10%.
```

## Interprétation des métriques

| Signal | Interprétation | Action |
|--------|---------------|--------|
| Views faibles < 50/7j | Mauvais référencement SEO | Retravailler titre + tags |
| Views ok, 0 vente | Prix ou photos | A/B test photo principale, revoir le prix |
| Views ok, favoris élevés, 0 vente | Prix trop haut | Baisser de 10-15%, tester |
| Ventes sans favoris | Acheteurs directs, peu d'hésitation | Produit fort, scaler les images |
| Pic de views puis chute | Tag saisonnier expiré | Permuter les tags saisonniers |

## Seuils de décision

| Période | Views seuil "ok" | Views seuil "alerte" |
|---------|-----------------|---------------------|
| 7 jours | > 30 | < 10 |
| 30 jours | > 150 | < 40 |
| 90 jours | > 500 | < 120 |

Ces seuils varient fortement selon la niche. Les catégories haute demande (bijoux, vêtements) ont des seuils 3-5x plus élevés. Les niches de niche (déco très spécifique, produits B2B) peuvent performer avec des volumes moindres.

## Rapport hebdomadaire automatique

Pour lancer chaque lundi matin via cron ou manuellement :

```bash
python3 scripts/etsy_stats.py --report --days 7 --export csv
```

Le CSV est exporté dans `~/Desktop/etsy-stats-YYYY-MM-DD.csv`.

## Intégration avec le skill

Quand le skill crée une fiche, il note le `listing_id` dans `fiche.md`. Le script `etsy_stats.py` peut être lancé sur ce listing à J+7 pour un premier bilan.

Format dans `fiche.md` :
```
SUIVI PERFORMANCE :
- listing_id : 4533096986
- Posté le : 2026-07-05
- Premier bilan : lancer python3 etsy_stats.py --listing 4533096986 --days 7 après le 2026-07-12
```

## Limitations API

- Les stats Etsy ont un délai de ~24-48h (les views d'hier apparaissent après-demain).
- Pas de données d'impressions dans les résultats de recherche (ça, c'est dans Etsy Seller Analytics uniquement, pas via API).
- Les transactions requièrent le scope `transactions_r` (ajouter à l'OAuth si besoin).
