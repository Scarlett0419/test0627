# Product Brief

ÉTAPE OBLIGATOIRE avant tout sourcing AliExpress. Cadre précisément ce que veut l'utilisateur pour éviter les sourcings ratés.

## Pourquoi cette étape existe

Apprentissage du test [NomBoutique] (2026-06-18) : le pipeline a sourcé une serviette rayée à grosses bandes "design" alors que l'utilisateur voulait du classique uni ou bandes fines. Résultat : sourcing rejeté, temps perdu.

Le titre de catégorie ("serviettes premium", "boucles d'oreilles minimalistes") ne suffit pas. Il faut un brief détaillé avant de chercher.

## Quand l'appliquer

Au tout début du pipeline fiche, **avant l'étape 1** (les 3 agents de recherche). Si l'utilisateur a juste donné une catégorie ("serviettes", "bijoux", "bougies"), pose le brief produit. S'il a donné un lien AliExpress précis, saute cette étape, le produit est déjà choisi.

## Le questionnaire (à adapter par catégorie)

Utilise `AskUserQuestion`. Pose les 3 à 5 questions les plus structurantes pour le produit. Toujours inclure :

1. **Style / motif** : uni, à motifs, type de motifs acceptés ET refusés. Crucial.
2. **Couleurs / palette** : 2 à 4 familles de couleurs cibles.
3. **Matière** : la plus pertinente pour la catégorie.
4. **Format / taille** : standard, XL, set.
5. **Refus explicites** : ce que l'utilisateur ne veut SURTOUT pas (souvent oublié sans cette question).

## Adapter par catégorie

| Catégorie | Questions clés |
|-----------|----------------|
| Linge de maison (serviettes, draps) | motif, couleur, matière, taille, GSM cible si connu |
| Bijoux | matière (or, argent, acier), style (minimaliste, baroque, vintage), occasion, hypoallergénique oui/non |
| Bougies / parfums | parfum (notes), contenant (verre, céramique, métal), taille (oz), style étiquette |
| Décoration | matière, style (scandi, bohème, industriel), couleur dominante, taille |
| Vêtements | matière, coupe, couleur, taille, occasion |

## Stockage

Sauvegarde les réponses dans le dossier produit, fichier `product-brief.md`. Toutes les étapes suivantes (sourcing, listing, images) DOIVENT s'y référer pour rester cohérentes.

Format :
```markdown
# Product Brief — [nom produit]

## Style / motif
- Voulu : [liste]
- Refusé : [liste]

## Couleurs
[familles retenues]

## Matière
[la matière retenue]

## Format
[taille / set]

## Autres contraintes
[ce que l'utilisateur a précisé]
```

## Filtrage du sourcing

L'agent sourcing DOIT filtrer les résultats selon ce brief :
- Si une serviette a "grosses bandes contrastées" et l'utilisateur a refusé "imprimés flashy" → exclure.
- Si la palette voulue est "écru/blanc + pastels" → exclure les serviettes rose vif, rouge, noir.
- Si "coton 100% classique" est demandé → exclure microfibre, bambou pur.

Quand l'agent présente ses 3 candidats finaux, **il doit justifier comment chacun respecte le brief**. Pas de surprise.

## Si le brief est trop strict

Si aucun produit AliExpress 1000+ commandes ne correspond, signale-le à l'utilisateur :
> « Avec tes critères (X, Y, Z), je trouve 0 vendeur au-dessus de 1000 commandes. Soit on assouplit un critère (lequel ?), soit on accepte un volume plus faible (risque qualité). »

Ne sors jamais un produit hors brief en disant rien.
