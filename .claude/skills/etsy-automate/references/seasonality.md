# Seasonality

Ajuste les tags et l'angle selon la période de l'année. Auto, intégré au Listing Generator.

## Principe

Un produit a des tags permanents (« gold hoops », « stainless steel ») et des tags saisonniers (« christmas gift », « valentines gift »). Les saisonniers boostent la visibilité au bon moment et encombrent le reste de l'année.

Règle : maximum 2-3 tags saisonniers sur les 13. Ils remplacent les tags les plus faibles, jamais les mots-clés principaux.

## Calendrier de déclencheurs

| Période | Tags à activer | Intensité |
|---------|----------------|-----------|
| Début nov. | christmas gift, holiday gift, stocking stuffer, secret santa gift | Fort |
| Nov-Déc | christmas gift, gift for her, gift for him, holiday home decor | Très fort |
| Janvier | new year gift, self care gift, resolution, fresh start | Moyen |
| Mi-janv. | valentines gift, gift for girlfriend, anniversary gift | Fort |
| Février | valentines day gift, romantic gift, gift for couple | Fort |
| Mars | spring home decor, easter gift, mothers day gift | Moyen |
| Avril-mai | mothers day, graduation gift, wedding gift | Fort |
| Juin | fathers day gift, summer gift, bridesmaid gift, wedding favor | Moyen |
| Juil-août | summer decor, vacation, beach gift | Faible (creux Etsy) |
| Sept-oct. | fall decor, halloween, back to school | Moyen |

**Anticipation** : les acheteurs cherchent les cadeaux 3-6 semaines avant la fête. Activer les tags saisonniers 4 semaines avant le pic.

## Tags par niche produit

### Bijoux / Accessoires

**Permanents forts** : dainty jewelry, minimalist necklace, gold filled earrings, stacking ring, personalized jewelry

**Saisonniers** :
- Nov-Déc : christmas jewelry gift, holiday earrings, stocking stuffer jewelry, gift for teen girl
- Fév : valentines gift for her, romantic jewelry, love necklace
- Mai : mothers day jewelry, graduation necklace, gift for mom
- Juin : bridesmaid jewelry gift, wedding earrings, summer jewelry

**Tags à éviter** (sur-utilisés, peu de volume) : "cute jewelry", "pretty necklace", "nice earrings"

---

### Bougies / Parfums d'intérieur

**Permanents forts** : soy candle, hand poured candle, natural candle, wood wick candle, scented candle gift

**Saisonniers** :
- Nov-Déc : christmas candle, holiday scent, cozy home gift, winter candle
- Fév : valentines candle, romantic candle, couples gift
- Mars-Avr : spring candle, floral scent candle, easter home gift
- Oct : halloween candle, fall candle, pumpkin spice candle, cozy fall decor

**Tags à éviter** : "nice candle", "good smell candle" (non-specifiques, volume nul)

---

### Déco intérieure / Linge de maison

**Permanents forts** : housewarming gift, home decor gift, minimalist decor, cozy home, aesthetic room decor

**Saisonniers** :
- Nov-Déc : christmas home decor, holiday table decor, cozy winter home, gift for homeowner
- Janv-Fév : valentines home decor, romantic bedroom decor
- Mars-Avr : spring home refresh, easter table decor
- Oct : fall home decor, autumn aesthetic, cozy fall home

**Tags à éviter** : "nice decoration", "pretty room" (trop vagues, zéro intent d'achat)

---

### Papeterie / Prints / Art mural

**Permanents forts** : printable wall art, digital download, gallery wall print, minimalist poster, boho art print

**Saisonniers** :
- Nov-Déc : christmas printable, holiday print, winter wall art, xmas decor print
- Fév : valentines printable, love quote print, romantic wall art
- Mai : mothers day printable, new home print, graduation gift print
- Sept-Oct : back to school printable, fall wall art, autumn print

---

### Soins / Bien-être / Bath & Body

**Permanents forts** : natural skincare gift, self care gift set, spa gift for her, bath set gift, organic beauty gift

**Saisonniers** :
- Nov-Déc : christmas spa gift, holiday pamper set, stocking stuffer spa, gift for mom christmas
- Fév : valentines spa gift, pamper gift for her, self care valentines
- Mai : mothers day spa gift, pamper set for mom
- Tout l'année (faible saison) : self care sunday, relaxation gift, stress relief gift

---

### Cuisine / Epicerie fine / Food gifts

**Permanents forts** : gourmet food gift, artisan food, hostess gift, housewarming food gift, foodie gift

**Saisonniers** :
- Nov-Déc : christmas food gift, holiday treat, christmas hamper, gift basket christmas
- Fév : valentines chocolate, romantic dinner gift, couples food gift
- Juin : fathers day food gift, bbq gift, summer picnic gift
- Oct : halloween treat, fall baking gift, pumpkin spice

---

## Application dans le Listing Generator

1. Regarde la date du jour.
2. Identifie la niche du produit.
3. Sélectionne 1-3 tags saisonniers pertinents pour la période ET cohérents avec le produit.
4. Remplace les tags permanents les plus faibles (pas les mots-clés ancres).
5. Note dans `fiche.md` quels tags sont saisonniers avec la date de rotation suggérée.

Format dans `fiche.md` :
```
TAGS SAISONNIERS (à permuter) :
- "christmas gift" → retirer après le 26 déc.
- "holiday home decor" → retirer après le 26 déc.
Remplacer par : "new year gift", "winter home decor"
```

## Tags saisonniers universels (toutes niches)

Ces tags fonctionnent sur presque tous les produits physiques cadeaux :

| Tag | Période | Note |
|-----|---------|------|
| christmas gift | Nov 1 → Déc 26 | Volume très fort |
| stocking stuffer | Nov 1 → Déc 20 | Produits < 30 USD surtout |
| valentines gift | Jan 15 → Fév 14 | Fort pour bijoux, bougies, spa |
| mothers day gift | Avr 15 → Mai 12 | Très fort toutes niches |
| gift for her | Toute l'année | Semi-saisonnier, pic Nov-Mai |
| housewarming gift | Toute l'année | Stable, pic déménagements |

## Tags à ne jamais mettre (volume nul ou pénalisés)

- Tags d'un seul mot : "gift", "cute", "pretty", "nice", "cool" → trop vague, algorithme Etsy les ignore
- Répétition de la même idée : si "bath towel set" est en titre, ne pas mettre "towel set" en tag (doublon inutile)
- Tags sans intention d'achat : "relaxing", "soft feel", "beautiful" → descriptifs non recherchés
