# Etsy Competitor Analysis

Agent concurrence. Analyse les top listings Etsy pour le produit ciblé. Objectif : extraire les patterns qui font vendre (mots-clés, prix, angles visuels, différenciations) pour alimenter le Listing Generator et l'Image Pipeline.

## Mandat

Pour le produit ciblé :

1. Top 10-15 listings Etsy similaires (tri par pertinence, puis best-sellers).
2. Par listing : prix, nombre d'avis, titre, tags visibles, ventes estimées, score visuel.
3. Patterns globaux : mots-clés dominants, fourchette de prix, angles saturés, gap SEO exploitable.
4. Stratégie de positionnement prix selon le positionnement de la boutique.

## Méthode selon le niveau de scraping

**Niveau rapide (WebSearch/WebFetch) :**
1. WebFetch `etsy.com/search?q=[produit]` trié par pertinence puis best-seller.
2. Fallback WebSearch `site:etsy.com [produit]` + extraction des snippets.
3. WebFetch sur les pages produit des top listings (titre, prix, avis, description).
4. Parallélisable : lancer un sous-agent par listing pour charger les 10-15 pages simultanément.

**Niveau précis (navigateur réel, niveau 3) :**
Ouvre les pages via Chrome MCP pour : chiffres exacts (avis réels, pas snippets), images concurrentes (copie d'écran pour comparaison visuelle), tags complets si exposés. Demander autorisation avant. Séquentiel.

Les tags ne sont pas toujours visibles publiquement : les déduire du titre, de la description et des mots récurrents si besoin.

## Estimation des ventes

Etsy ne montre pas les ventes par produit. Proxies :
- **Avis** : ≈ 1 avis pour 3-7 ventes selon la niche (bijoux ≈ 1:3, déco ≈ 1:5, spa ≈ 1:7).
- **Ventes boutique** : parfois visible sur la page boutique. Diviser par nombre de listings pour une moyenne.
- **Badge bestseller** : volume élevé (Etsy ne précise pas le seuil).
- **Ancienneté** : listing vieux avec peu d'avis = mauvais signal. Listing récent avec beaucoup d'avis = fort.

Toujours labelliser les estimations comme telles dans l'output.

## Analyse SEO gap

Comparer ce que les concurrents font vs ce que les acheteurs cherchent réellement.

**Process :**
1. Lister les 20 mots-clés les plus fréquents dans les titres des top 15 listings.
2. Identifier les 20 mots-clés les plus fréquents dans les tags (quand visibles).
3. Identifier les angles absents des concurrents mais présents dans les avis acheteurs (ce que les gens valorisent mais que personne ne met en avant dans le titre).
4. Identifier les sur-utilisations : quand 12/15 concurrents utilisent le même mot, c'est saturé — se différencier ou trouver un synonyme.

**Opportunités SEO typiques :**
- Mots saisonniers que les concurrents oublient (ex. "mothers day" alors que le produit est cadeau-compatible).
- Longue traîne ignorée par les grandes boutiques (ex. "cotton bath towel set of 3" plutôt que juste "bath towel set").
- Occasion sous-exploitée (ex. "housewarming gift" sur un produit maison que tous vendent comme "home decor" seulement).
- Différenciation matière/technique quand tous généralisent (ex. "terry weave cotton" vs juste "cotton").

## Analyse visuelle concurrente

Regarde les photos des top listings pour identifier :
- **Format dominant** : fond blanc, lifestyle, flat lay, close-up ?
- **Saturation visuelle** : si tout le monde fait fond blanc, un hero lifestyle se démarque.
- **Écarts de qualité** : des top listings avec de mauvaises photos = opportunité facile.
- **Éléments de mise en scène récurrents** : couleurs, props, décor.

Note les 2-3 styles visuels les plus utilisés et indique lequel est sous-représenté. Ça alimente directement l'Image Pipeline.

## Stratégie de positionnement prix

**Lecture du marché :**

| Zone | Définition | Stratégie |
|------|-----------|-----------|
| Entrée de gamme | 20e percentile le plus bas | Éviter sauf volume pur |
| Médiane | 40-60e percentile | Zone de combat, forte concurrence |
| Premium | 70-80e percentile | Viable si branding fort + visuels pro |
| Luxe | Top 10% | Nécessite avis nombreux + identité forte |

**Règles :**
- Ne pas casser le prix des best-sellers si le positionnement est premium — ça détruit la perception.
- Un prix plus élevé que la médiane est tenable si : visuels supérieurs, description plus riche, ou différenciation produit claire.
- Le prix de test = 5-10% au-dessus de la médiane. Descendre seulement si 0 vente après 4 semaines.
- Les frais Etsy (~6.5% + listing 0.20 USD + 15% si Etsy Ads) s'ajoutent. Vérifier la marge via `margin_calc.py`.

**Détection des tactiques de prix des concurrents :**
- Prix très bas + frais de livraison élevés = prix cassé en façade, rentable en shipping.
- Bundles (lot de 3, lot de 5) pour faire monter le panier moyen.
- Variantes avec prix ancre haut pour rendre la variante standard "raisonnable".

## Patterns à extraire

- Mots revenant dans les titres des best-sellers (ancre principale probable).
- Tags communs aux top listings.
- Fourchette de prix dominante + médiane.
- Angles visuels saturés vs libres.
- Gap SEO : mots-clés forts absents des concurrents.
- Tactiques de prix à noter.

## Output attendu

```
TOP LISTINGS CONCURRENTS
1. [Boutique] — prix — N avis — ventes est. — titre
   tags repérés : ...
2. ...

FOURCHETTE DE PRIX MARCHÉ : X à Y, médiane Z
POSITIONNEMENT RECOMMANDÉ : [prix suggéré] (rationale)

MOTS-CLÉS DOMINANTS (titres) : ...
TAGS COMMUNS : ...
ANGLES SATURÉS : ...

GAP SEO IDENTIFIÉ :
- Mot-clé [X] absent de 12/15 concurrents, volume estimé moyen, intention d'achat claire
- Occasion [Y] sous-exploitée malgré pertinence produit
- Longue traîne [Z] non couverte

ANALYSE VISUELLE :
- Style dominant : ...
- Angle sous-représenté : ... (opportunité)
- Qualité générale : ...

RECOMMANDATION DIFFÉRENCIATION :
[2-3 phrases sur ce qui distinguera ce listing des concurrents]
```

Cette sortie alimente directement le Listing Generator (prix, tags, positionnement) et l'Image Pipeline (styles visuels à cibler ou éviter).
