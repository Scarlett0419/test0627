# Listing Generator

Coeur du skill. Prend les sorties des 3 agents (sourcing, concurrence, reviews) et fabrique la fiche complète. Full auto, pas de validation utilisateur sur le texte. S'appuie sur les skills `etsy-seo`, `etsy-keyword-research`, `etsy-product-description`.

## Inputs requis

- Sourcing AliExpress (prix, vendeur)
- Concurrence Etsy (fourchette prix, tags dominants, mots-clés)
- Review mining (power words, objections)
- Shop Identity Card (positionnement, ton, langue)

Si un input manque (module lancé seul), va le chercher en direct ou demande.

## Titre (140 chars max)

Structure éprouvée :

```
[Mot-clé principal] + [Attributs] + [Matière/Style] + [Usage/Occasion]
```

Exemple :
```
Gold Hoop Earrings Stainless Steel, Minimalist Chunky Hoops, Waterproof Jewelry Gift for Her
```

Règles :
- Mot-clé principal en premier (poids SEO).
- Intègre les power words du review mining et les mots-clés dominants de la concurrence.
- Pas de mots vides (« beautiful », « nice »). Concret.
- Langue = marché cible de la Shop Identity Card.

## Description (6000 chars max)

Structure :

1. **Accroche** (premiers 160 chars critiques pour le SEO et l'aperçu) : bénéfice principal + mot-clé.
2. **Bénéfices** : ce que les avis positifs confirment, formulé pour l'acheteur.
3. **Specs** : dimensions exactes, matière, poids. Contre les objections du review mining ici (ex : « se ternit » → « acier inoxydable, ne noircit pas »).
4. **FAQ** : 3-5 questions tirées des objections.
5. **CTA** : clair, dans le ton de la boutique.

Ton = celui de la Shop Identity Card. Densité mot-clé naturelle (principal 3-5 fois, secondaires 1-2 fois). Pas de tiret cadratin. Appliquer `humanizer` et `caveman`.

## Règle dure : jamais de spec non vérifiée

**N'invente jamais une spec technique (GSM, grammage, densité de fils, dimensions exactes, certifications) qui n'est pas confirmée par la fiche produit du vendeur.** Si la spec n'est pas accessible, deux options :
- Mets `[À VÉRIFIER auprès du vendeur]` dans la fiche, l'utilisateur la complète avant publication.
- Reformule sans la spec chiffrée (ex : "heavyweight cotton" au lieu de "700 GSM cotton").

Annoncer un GSM faux = avis négatif garanti à la première mesure d'un acheteur. Sur Etsy un avis 1 étoile vaut très cher en début de boutique.

## Unités et specs adaptées au marché

Les acheteurs lisent dans LEUR unité, pas dans la tienne. Toujours convertir et adapter selon le marché cible.

| Marché | Dimensions | Poids | Specs techniques |
|--------|-----------|-------|------------------|
| US / international | pouces ET cm (les deux, pouces en premier) | oz ET grammes | GSM (utilisé) mais TOUJOURS expliqué la 1ère fois |
| FR / EU | cm | grammes | g/m² (équivalent francais de GSM) |
| UK | cm ET pouces (cm en premier) | grammes | GSM expliqué |

**Pour le jargon technique (GSM, plush, peshtemal, etc.) :** 1ère mention = explication courte entre parenthèses ou en glose. Ex : "700 GSM (the dense hotel-spa weight)" plutôt que "700 GSM" seul.

Pour les serviettes spécifiquement :
- GSM = grams per square meter, mesure de densité standard. 400-500 standard, 600-700 premium, 800+ luxe.
- Toujours convertir 70x140 cm → "70 x 140 cm (27.5 x 55 in)".

L'angle de vente (Désir / Preuve / Contre-intuitif) n'est ajouté QUE si l'utilisateur le demande (voir `sales-angles.md`). Par défaut, version neutre bénéfices.

## Awareness level

Adapte le ton selon le niveau de conscience du marché (déduit de la concurrence) :

| Niveau | Ton description |
|--------|-----------------|
| Problem aware | Explique d'abord pourquoi ce type de produit résout un problème |
| Solution aware | Mets en avant pourquoi CE produit vs les autres |
| Product aware / Most aware | Va direct au bénéfice et à l'offre, l'acheteur connait déjà |

## 13 tags

Règles Etsy : max 13 tags, max 20 caractères chacun, phrases multi-mots autorisées.

Stratégie :
- Long-tail (« waterproof gold hoops » mieux que « hoops »).
- Synonymes et variantes.
- Attributs (matière, couleur, taille).
- Occasion (« birthday gift », « gift for her »).
- Tags des concurrents qui marchent.
- Tags saisonniers selon la période (voir `seasonality.md`).

## Prix

Calcul via script :

```bash
python3 ~/.claude/skills/etsy-automate/scripts/margin_calc.py --cost 2.30 --shipping 0 --market-avg 22
```

Affiche les 3 scénarios de marge (30/50/70%) et recommande selon le positionnement de la boutique. Montre la justification : prix AliExpress, frais Etsy, marge nette, prix moyen concurrence.

## Variantes

Si le produit a des variantes (tailles, couleurs), un seul listing avec les options listées, pas une fiche par variante.

## Format de fiche.md (output final)

```markdown
# [Nom du produit]

## Titre Etsy
[titre 140 chars]

## Description
[description complète]

## Tags (13)
tag1 | tag2 | ... | tag13

## Prix
Recommandé : XX.XX [devise]
- Coût AliExpress : X.XX
- Frais Etsy estimés : X.XX
- Marge nette : X.XX (XX%)
- Prix moyen concurrence : XX.XX
- Positionnement : [vs marché]

## Variantes
[si applicable]

## Vendeur AliExpress recommandé
1. [Nom] — prix — note — commandes — délai — [lien]
2. ...
3. ...

## Analyse concurrence
[résumé : vs qui, fourchette prix, différenciation]

## Brief images
1. Hero — [angle, fond, pourquoi]
2. Lifestyle — ...
[un par image]

## Statut
Fiche générée le [date]. Images : [validées / en attente]. Publication : [local / draft Etsy].
```
