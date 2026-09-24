# Shop Identity Card

Créée une seule fois par boutique. Toutes les fiches et images générées ensuite en héritent. Sans elle, 50 fiches auront 50 tons différents.

## Quand la créer

Au premier lancement si `shop-identity.md` n'existe pas. Une fois remplie, ne plus jamais reposer les questions.

## Questions à poser (groupées, une seule fois)

Utilise `AskUserQuestion`. Demande :

1. **Nom de la boutique**
2. **Positionnement** : budget / mid-range / luxury
3. **Style visuel** : ex « minimaliste épuré », « bohème chic », « ZARA Home aesthetic », « artisanal cozy »
4. **Marché cible** : géographie (FR, US, UK, international) et donc langue des fiches
5. **Type d'acheteur** : qui achète (âge, contexte, occasion type)
6. **Marge cible par défaut** : 30% / 50% / 70%

## Ce que tu en déduis et stockes

Écris `shop-identity.md` avec :

```markdown
# Shop Identity Card — [Nom]

## Positionnement
[budget / mid / luxury]

## Marché cible
Géographie :
Langue des fiches :
Acheteur type :

## Ton de voix
3 adjectifs : [ex: chaleureux, précis, rassurant]
Phrases à utiliser : [exemples concrets]
Phrases à éviter : [exemples concrets]

## Style visuel
Palette couleurs : [hex ou description]
Mood des images : [ex: lumière naturelle, fond marbré, ambiance cosy]
Références visuelles : [boutiques, esthétiques ou styles inspirants — alimente la variable {visual_references} des prompts image]

## Marge cible
[30 / 50 / 70 %]
```

## Cohérence positionnement → tout le reste

Le positionnement pilote tout :

| Positionnement | Prix | Images | Ton description |
|----------------|------|--------|-----------------|
| Budget | Bas, agressif | Fond blanc clean, simple | Direct, axé prix et praticité |
| Mid-range | Aligné marché | Lifestyle lumineux | Équilibré, bénéfices + qualité |
| Luxury | Haut, premium | Fond marbre/lin, éditorial | Soigné, axé exclusivité et matière |

Rappelle ce tableau à chaque génération de fiche et d'image pour garder la cohérence.
