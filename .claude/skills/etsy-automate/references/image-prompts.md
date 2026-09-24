# Image Prompts Generator

Système de génération de prompts pour transformer les images AliExpress sans modifier le produit. Le **produit reste intact**, seul le **fond, la présentation et l'angle** changent. Chaque shot type a un **angle de caméra obligatoirement différent** pour donner 6 vues complémentaires.

## Note : templates par catégorie

Les templates ci-dessous sont validés sur le cas **linge de maison / serviettes** (test [NomBoutique], juin 2026). Pour d'autres catégories, adapter les shot types et les éléments de décor :

| Catégorie | Hero | Lifestyle | Macro | Flatlay | Profile | Gift |
|-----------|------|-----------|-------|---------|---------|------|
| Linge de maison | pile pliée | draped on rack | tissu au macro | à plat sur lin | vue latérale pile | attaché lien + eucalyptus |
| Bijoux | porté sur main/oreille | lifestyle casual | détail métal/pierre | à plat sur marbre | vue profil portée | dans écrin + ruban |
| Bougies | bougie allumée | lifestyle table | surface de la cire | à plat avec fleurs séchées | vue latérale pot | avec allumettes + kraft |
| Décoration | in situ dans une pièce | lifestyle pièce | détail texture/matière | à plat sur surface assortie | vue côté/profil | emballé cadeau |

Les variables `{product}`, `{positioning}`, `{color_palette}`, `{mood}`, `{visual_references}` fonctionnent pour toutes les catégories — seul le contenu change.

## 3 règles dures non négociables

1. **PRÉSERVER LE PRODUIT EXACTEMENT.** Même couleur, même forme, mêmes proportions, même texture. Le produit dans la photo finale = le produit dans la source AliExpress, pixel-fidèle. Aucune création.

2. **6 ANGLES DIFFÉRENTS OBLIGATOIRES.** Pas deux shots avec le même point de vue caméra. Chaque image apporte une perspective unique pour donner à l'acheteur une vraie compréhension du produit.

3. **STYLE COHÉRENT AVEC LA BOUTIQUE.** Tous les prompts héritent automatiquement de la Shop Identity Card (positionnement, palette, mood, références culturelles). Une serviette [NomBoutique] n'aura jamais le même fond qu'une serviette d'une boutique budget.

## Étape préalable obligatoire : Shop Identity Card complète

Avant de générer le moindre prompt, vérifier que `shop-identity.md` du dossier boutique contient :

| Champ | Exemple [NomBoutique] | Si manquant |
|---|---|---|
| Positionnement | luxury accessible | DEMANDER |
| Palette couleurs | tons dorés, neutres chauds (crème, beige, lin) | DEMANDER |
| Mood | lumière douce et naturelle, ambiance spa et rituel | DEMANDER |
| Références visuelles | esthétique hôtel-spa, French Riviera, daily ritual | DEMANDER |
| Géographie / contexte culturel | Cannes, French Riviera, méditerranéen | DEMANDER |
| Acheteur type | adulte 30-50, soigne son rituel quotidien | DEMANDER |
| Phrases à utiliser / éviter | "elevate your daily ritual" / pas "cheap" | DEMANDER |

**Si un de ces champs manque, NE PAS LANCER le pipeline image.** Poser les questions à l'utilisateur, mettre à jour `shop-identity.md`, puis générer les prompts.

## Variables de remplacement automatique

Le skill remplace dans les templates :

| Variable | Source |
|---|---|
| `{positioning}` | shop-identity.md > Positionnement |
| `{color_palette}` | shop-identity.md > Palette couleurs |
| `{mood}` | shop-identity.md > Mood des images |
| `{visual_references}` | shop-identity.md > Références |
| `{geography}` | shop-identity.md > Géographie |
| `{product}` | Listing : description courte du produit (ex: "stack of 3 premium cotton bath towels in graphite, white, stone blue") |
| `{material_focus}` | Listing : matière à mettre en avant (ex: "terry cotton weave") |

## Les 6 angles obligatoires (un par shot type)

Chaque image a un angle de caméra différent, défini par le shot type. **Ne jamais en sauter ou doubler.** Si une image foire, on la refait avec le même angle.

| # | Shot type | Angle de caméra | Distance | Composition |
|---|-----------|-----------------|----------|-------------|
| 1 | **Hero** | 3/4 face légèrement en hauteur (15-30°) | 80% du cadre rempli | Centré, fond soigné |
| 2 | **Lifestyle** | Eye level, lointain | Produit + environnement | Règle des tiers, contexte visible |
| 3 | **Detail / Macro** | Très rapproché, parallèle au tissu | Macro (texture) | Plein cadre texture |
| 4 | **Top-down / Flat lay** | 90° au-dessus | Produit à plat | Composition géométrique stricte |
| 5 | **Side / Profile** | 90° latéral pur | Profil complet | Silhouette du produit pure |
| 6 | **Lifestyle alternatif OU Packaging** | Eye level proche, légère plongée 10° | Cadrage moyen, mise en scène | Mise en situation cadeau / utilisation |

Le shot 6 peut basculer entre "packaging cadeau" et "produit en utilisation" selon la catégorie de produit (ex: bijoux → porté, serviettes → empilées avec accessoires, bougies → allumées).

## Templates par shot type

Chaque template termine par `preserve the exact product from the source image, only change background, lighting, and angle of view`. **Ne pas retirer cette ligne.**

### 1. Hero — 3/4 face en hauteur

```
{product}, hero product shot, three-quarter view from slightly above (20 degrees high angle),
product centered and fills 75 percent of the frame,
{positioning} brand aesthetic,
warm neutral palette {color_palette}, {mood},
soft natural light from the left, gentle drop shadow,
premium editorial composition, shallow depth of field,
inspired by {visual_references},
preserve the exact product from the source image: same color, same shape,
same proportions, same texture. Only change background, surface, lighting and angle of view.
Shot on Hasselblad medium format, 4:5 ratio, magazine quality.
```

### 2. Lifestyle — eye level, contexte

```
{product} placed in a {geography} interior setting,
eye-level camera angle, looking across the room at the product in context,
product visible but not centered (rule of thirds, lower-right or lower-left),
{positioning} interior design, {color_palette}, {mood},
warm afternoon natural light through a window, lived-in but pristine,
authentic premium home, {visual_references},
preserve the exact product details (same shape, color, material) from the source image,
only change the room, the surface it sits on, and the ambient lighting.
Editorial lifestyle photography, 4:5 ratio.
```

### 3. Detail / Macro — close-up parallèle

```
Extreme close-up macro of the {material_focus} surface of {product},
camera parallel to the fabric/material, shallow depth of field, focus on texture,
fill the entire frame with the product material,
{color_palette} subtle background bokeh,
{mood}, soft directional lighting highlighting weave and craftsmanship,
preserve the exact texture, color, weave pattern from the source image,
only change the background blur and the lighting direction.
Commercial product photography, sharp foreground detail, 1:1 ratio.
```

### 4. Top-down / Flat lay — 90° au-dessus

```
Top-down flat lay of {product}, camera directly overhead at 90 degrees,
product centered on a neutral premium surface,
{positioning} flat-lay composition with strict geometric arrangement,
{color_palette} surface (linen, marble, light wood according to the palette),
{mood}, soft even overhead light, minimal soft shadow,
2 to 3 supporting props maximum (eucalyptus branch, small ceramic, folded linen)
arranged around the product to support {visual_references} aesthetic,
preserve the exact product from the source image: same color, exact shape,
exact proportions. Only change the surface and styling around it.
Editorial flat-lay, 1:1 ratio.
```

### 5. Side / Profile — 90° latéral

```
Pure side profile of {product}, camera at 90 degrees lateral angle, eye level,
showing the silhouette and depth of the product clearly,
{color_palette} clean gradient or fabric background, no clutter,
{positioning} aesthetic, {mood},
soft single-source side light to define edges and shape,
preserve the exact product profile from the source image (proportions, color, contour),
only change the background and the lighting setup.
Clean editorial product photography, 1:1 ratio.
```

### 6a. Packaging / cadeau (si pertinent)

```
{product} styled as a gift, wrapped or in premium packaging,
eye-level camera angle, slight 10-degree downward tilt, medium close shot,
{positioning} gift presentation, {color_palette}, 
ribbon or natural twine, complementary props (small card, eucalyptus sprig),
{visual_references} mood, intimate framing,
soft window light, lived-in luxury,
preserve the visible product exactly as in the source image,
only change the wrapping context, accessories and lighting.
Editorial gift photography, 4:5 ratio.
```

### 6b. Lifestyle alternatif (si pertinent à la place du packaging)

```
{product} in active use or styled context different from shot 2,
eye-level proche, slight downward angle 10 degrees, medium close shot,
{positioning} living moment, {color_palette}, {mood},
contextual props that show how the product is used in daily ritual,
{visual_references} atmosphere, golden hour light or candlelit warmth,
preserve the exact product from the source image,
only change the surrounding scene, accessories and lighting.
Editorial lifestyle photography, 4:5 ratio.
```

## Negative prompt commun (ajouter à TOUS les prompts)

```
Negative: low quality, blurry, distorted product, altered colors, altered shape,
fake plastic look, AI artifacts, oversaturated, busy clashing background,
text overlays, watermarks, logos other than the source, hands holding product,
faces in close shot 1-5, brand names visible, busy patterns, neon.
```

## Couches de raffinement selon positionnement

Ajoutées après le template principal selon Shop Identity Card.

### Budget
```
+ clean white or light gray background, e-commerce ready, no decorative props,
flat even lighting, honest direct presentation, no luxury suggestion.
```

### Mid-range
```
+ accessible lifestyle home setting, warm natural lighting,
relatable everyday luxury, neither too cheap nor too expensive.
```

### Luxury / Premium (ex: [NomBoutique])
```
+ editorial quality, hotel-spa atmosphere, marble or linen surfaces,
golden hour or soft window light, eucalyptus or olive branches as subtle accents,
designer interior, magazine-grade composition,
discrete hint of {geography} elegance.
```

## Exemple complet : prompts.json [NomBoutique] (6 angles différents)

Le skill génère ce JSON automatiquement et le sauvegarde dans le dossier produit. C'est ce que `wavespeed_transform.py` consomme.

```json
{
  "candidateB_2.jpg": {
    "output": "hero.jpg",
    "shot_type": "hero",
    "camera_angle": "three-quarter view, 20 degrees high angle",
    "prompt": "Stack of 3 premium cotton bath towels (graphite, white, stone blue), hero product shot, three-quarter view from slightly above (20 degrees high angle), product centered and fills 75 percent of the frame, luxury accessible brand aesthetic, warm neutral palette of cream, beige and linen with subtle gold accents, soft natural light from the left, gentle drop shadow, premium editorial composition, shallow depth of field, inspired by hotel-spa aesthetic, French Riviera, daily ritual. preserve the exact product from the source image: same color, same shape, same proportions, same texture. Only change background, surface, lighting and angle of view. Shot on Hasselblad medium format, 4:5 ratio, magazine quality. Editorial quality, hotel-spa atmosphere, marble or linen surface, golden hour light, eucalyptus branches as subtle accents. Negative: low quality, blurry, distorted product, altered colors, AI artifacts, busy background, watermarks, faces, brand names."
  },
  "candidateB_1.jpg": {
    "output": "lifestyle.jpg",
    "shot_type": "lifestyle",
    "camera_angle": "eye level, contextual distance",
    "prompt": "Stack of premium cotton bath towels placed in a French Riviera interior setting, eye-level camera angle, looking across the room at the product in context, product visible but not centered (rule of thirds, lower-right), luxury accessible interior design, warm neutral palette cream beige linen, soft spa ambiance with daily ritual mood, warm afternoon natural light through a window, lived-in but pristine, authentic premium Mediterranean home, hotel-spa aesthetic with golden hour subtle accents. preserve the exact product details (same shape, color, material) from the source image, only change the room, the surface it sits on, and the ambient lighting. Editorial lifestyle photography, 4:5 ratio. Negative: low quality, blurry, distorted product, AI artifacts, faces close up, brand names visible."
  },
  "candidateB_3.jpg": {
    "output": "detail-macro.jpg",
    "shot_type": "detail-macro",
    "camera_angle": "macro parallel to fabric",
    "prompt": "Extreme close-up macro of the terry cotton weave surface of the premium bath towel, camera parallel to the fabric, shallow depth of field, focus on texture, fill the entire frame with the product material, warm neutral palette cream beige linen subtle background bokeh, soft spa mood, soft directional lighting highlighting weave and craftsmanship. preserve the exact texture, color, weave pattern from the source image, only change the background blur and the lighting direction. Commercial product photography, sharp foreground detail, 1:1 ratio. Negative: AI artifacts, plastic, oversaturated, distorted weave."
  },
  "candidateB_4.jpg": {
    "output": "flatlay.jpg",
    "shot_type": "top-down-flatlay",
    "camera_angle": "directly overhead 90 degrees",
    "prompt": "Top-down flat lay of folded premium cotton bath towels (graphite, white, stone blue), camera directly overhead at 90 degrees, product centered on a neutral linen surface, luxury accessible flat-lay composition with strict geometric arrangement, cream beige linen surface, soft spa mood, soft even overhead light, minimal soft shadow, 3 supporting props maximum (eucalyptus sprig, small ceramic dish, folded linen napkin) arranged around the product to support hotel-spa French Riviera aesthetic. preserve the exact product from the source image: same color, exact shape, exact proportions. Only change the surface and styling around it. Editorial flat-lay, 1:1 ratio. Negative: AI artifacts, busy, oversaturated, faces, brand names."
  },
  "candidateB_6.jpg": {
    "output": "profile.jpg",
    "shot_type": "side-profile",
    "camera_angle": "pure 90 degrees lateral",
    "prompt": "Pure side profile of stacked premium cotton bath towels, camera at 90 degrees lateral angle, eye level, showing the silhouette and depth clearly, warm neutral palette clean gradient background no clutter, luxury accessible aesthetic, soft spa daily ritual mood, soft single-source side light from the right to define edges and folded layers. preserve the exact product profile from the source image (proportions, color, contour), only change the background and the lighting setup. Clean editorial product photography, 1:1 ratio. Negative: AI artifacts, distorted, plastic, busy."
  },
  "candidateB_5.jpg": {
    "output": "gift.jpg",
    "shot_type": "packaging-gift",
    "camera_angle": "eye level, slight downward 10 degrees",
    "prompt": "Stack of premium cotton bath towels styled as a gift, tied with natural linen twine, eye-level camera angle with slight 10-degree downward tilt, medium close shot, luxury accessible gift presentation, warm neutral palette cream beige, ribbon or natural twine, complementary props (small handwritten card, eucalyptus sprig), French Riviera hotel-spa mood, intimate framing, soft window light, lived-in luxury. preserve the visible product exactly as in the source image, only change the wrapping context, accessories and lighting. Editorial gift photography, 4:5 ratio. Negative: AI artifacts, plastic ribbon, garish colors, brand names visible, faces."
  }
}
```

Note : pour [NomBoutique], le shot 5 (infographie dimensions) du test précédent a été remplacé ici par "profile" pour respecter la règle des 6 angles différents. L'infographie dimensions peut rester en 7e image bonus si besoin, créée séparément en design propre.

## Workflow d'utilisation par le skill

1. Vérifie que `shop-identity.md` est complet. Sinon, pose les questions.
2. Identifie les 6 images sources les plus exploitables dans `photos/source/`.
3. Pour chaque source, choisit un shot type unique (1 à 6).
4. Compose le prompt avec les variables de la Shop Identity Card.
5. Ajoute la couche de raffinement selon positionnement.
6. Ajoute le negative prompt commun.
7. Sauvegarde le tout dans `prompts.json` du dossier produit.
8. Présente les 6 prompts à l'utilisateur pour validation/édition.
9. Lance `wavespeed_transform.py --product /path/to/produit-dir`.
10. Récupère les 6 résultats, présente-les à l'utilisateur pour validation visuelle.

## Anti-patterns à éviter absolument

- ❌ Générer 2 shots avec le même angle de caméra
- ❌ Oublier "preserve the exact product from the source image"
- ❌ Lancer le pipeline sans Shop Identity Card complète
- ❌ Prompter en français (résultats FLUX Kontext médiocres en FR)
- ❌ Mettre la même image dans deux shots différents
- ❌ Ajouter des noms de marques connues dans le prompt ("like Frette", "like Brooklinen") → risque légal
- ❌ Demander au modèle de "rendre le produit plus beau" → il va modifier le produit
