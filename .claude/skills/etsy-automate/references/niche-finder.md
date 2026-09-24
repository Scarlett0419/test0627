# Niche Finder

Trouve des niches Etsy rentables avant de créer le moindre produit. Invoqué en Mode A ou seul sur demande.

## Objectif

Sortir un classement de 5 à 10 niches notées par score d'opportunité. Une niche gagne quand elle combine : volume de recherche correct + faible concurrence + marge élevée (gros écart prix AliExpress vs prix Etsy).

## Process

Lance plusieurs sous-agents en parallèle, un par axe de recherche.

### Agent 1 — Tendances

- WebSearch des catégories Etsy qui montent (« etsy trending products 2025/2026 », « etsy best sellers [catégorie] »).
- Google Trends pour les requêtes liées (croissance 6-12 mois).
- Repère les pics saisonniers.

### Agent 2 — Volume et demande

- Pour chaque piste de niche, estime le volume via l'autocomplete Etsy (taper le mot-clé, noter les suggestions = ce que les gens cherchent vraiment).
- WebSearch « etsy [niche] » pour voir le nombre de résultats (proxy de demande et de concurrence).

### Agent 3 — Concurrence et saturation

- Nombre de boutiques actives sur la niche.
- Ancienneté et force des top shops (beaucoup d'avis = établis et durs à déloger).
- Niveau de différenciation possible.

### Agent 4 — Marge

- Prix moyen du produit sur Etsy dans la niche.
- Prix du même type de produit sur AliExpress.
- Écart = marge brute potentielle. Plus l'écart est gros, mieux c'est.

## Scoring

Pour chaque niche, note de 0 à 10 sur :

| Critère | Poids |
|---------|-------|
| Volume de recherche | 25% |
| Faible concurrence | 30% |
| Marge potentielle | 30% |
| Tendance (montante vs déclin) | 15% |

Score global = moyenne pondérée.

## Output

Tableau classé, du meilleur au pire :

```
| Rang | Niche | Volume | Concurrence | Marge est. | Tendance | Score |
|------|-------|--------|-------------|------------|----------|-------|
| 1    | ...   | ...    | ...         | x5         | montante | 8.4   |
```

Plus une recommandation finale : la niche que tu choisirais et pourquoi en 2-3 phrases.

Sauvegarde dans `niche-research.md`.

## Fallback

Si l'accès aux pages Etsy est bloqué, utilise WebSearch sur Google avec `site:etsy.com [niche]` et les snippets de résultats. Labellise les chiffres comme estimations.
