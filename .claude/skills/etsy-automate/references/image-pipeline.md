# Image Pipeline

Transforme les photos AliExpress du produit en visuels Etsy originaux, adaptés à l'identité de la boutique. Part de vraies photos, jamais de génération produit from scratch. Réaliste avant tout.

## Principe

1. On valide un produit AliExpress.
2. On récupère SES photos (celles du vendeur).
3. On analyse les visuels des concurrents Etsy de la même niche.
4. On s'inspire fortement de ce qui convertit, on se différencie si saturé.
5. On retravaille les photos AliExpress via WaveSpeedAI FLUX Kontext Pro avec un prompt généré dynamiquement depuis la Shop Identity Card.
6. On valide les résultats avec l'utilisateur.

Pourquoi : reposter les photos AliExpress brutes = pénalisé par Etsy (reverse-image detection) et zéro différenciation marque. Les transformations WaveSpeedAI / FLUX Kontext Pro + style adapté à la boutique = images originales, alignées marque, conformes Etsy.

## Setup requis pour les vraies transformations IA

**Limite découverte au test [NomBoutique] (2026-06-23) :** le MCP Higgsfield exposé via Claude n'expose pas de tool de récupération de résultat de job (`get_job_result` manquant). Donc transformation automatique 100% via MCP impossible. Solution : passer par l'API WaveSpeedAI avec le modèle FLUX Kontext Pro.

### Solution principale : WaveSpeedAI API + FLUX Kontext Pro (pay-per-use, automatique)

**C'est la méthode par défaut du skill.** Validée sur le test [NomBoutique] juin 2026 : 6/6 succès, produit préservé, décor changé. Voir `references/wavespeed-setup.md` pour le setup complet.

- Inscription gratuite sur https://wavespeed.ai (5 min)
- Recharge libre Stripe (~$5-10 pour démarrer)
- API key Bearer token (format `wsk_...`)
- Prix : **$0.04/image** (FLUX Kontext Pro)
- Pour 6 images : **~$0.24**
- Endpoint : `POST api.wavespeed.ai/api/v3/wavespeed-ai/flux-kontext-pro` + polling `GET /predictions/{id}/result`
- Automatique via le script `scripts/wavespeed_transform.py`

Paramètres FLUX Kontext Pro :
- `aspect_ratio` : "3:4" pour hero/lifestyle/gift, "1:1" pour macro/flatlay/profile
- `guidance_scale` : 3.5 par défaut, 4.0 si le modèle dévie trop
- **Ne PAS utiliser** `strength`, `size`, `quality` (paramètres Soul, rejetés par Kontext)

⚠️ **Règle sourcing image critique** : FLUX Kontext hérite du nombre d'objets de l'image source. Si la source montre 4 serviettes, la sortie en montrera 4 même si le prompt dit 3. Pour un flatlay de 3 articles → choisir une source qui montre 3 articles (pas la pile globale).

Workflow auto :
1. Skill génère les 6 prompts adaptés à la boutique (voir `image-prompts.md`)
2. Skill range les 6 images sources dans `photos/source/`
3. Skill crée `prompts.json` qui mappe chaque image source → prompt + nom final
4. Lance `python3 wavespeed_transform.py --product /path/to/produit-dir`
5. Le script encode les images en base64, lance les jobs, poll les résultats, télécharge dans `photos/`
6. Skill reprend pour validation et publication

**Quand l'utiliser** : par défaut, toujours. WaveSpeed est moins cher que Higgsfield jusqu'à ~135 fiches/mois.

### Solution alternative : Higgsfield abonnement web (manuel, non automatisable)

Si l'utilisateur préfère le contrôle visuel manuel ou veut tester des modèles video :

**Plan Starter à €19/mois** (prix juin 2026).
- 270 crédits/mois ≈ 135 images Nano Banana Pro
- "Access to selected models only" (vérifier si FLUX Kontext inclus)
- Non automatisable via script (MCP ne permet pas de récupérer les résultats)

Si scaling > 135 fiches/mois → **Plan Plus à €47/mois** (1200 crédits ≈ 600 images).

URL : https://higgsfield.ai/pricing

Workflow manuel :
1. Skill génère les 6 prompts adaptés à la boutique
2. Skill range les sources dans `photos/source/`
3. L'utilisateur va sur https://app.higgsfield.ai, ouvre le modèle image-to-image disponible (pas Soul — voir section apprentissages)
4. Pour chaque image source : upload + colle prompt + lance + télécharge
5. L'utilisateur place les résultats dans `photos/` avec noms finaux
6. Skill reprend pour validation et publication

**Quand l'utiliser** : pour les fiches héros premium où chaque pixel compte, ou si l'utilisateur préfère un contrôle visuel total.

## Récupération des photos source

Toujours en haute résolution. Trois voies, par ordre de préférence :

1. **API Affiliate AliExpress** si configurée : renvoie les URLs images propres.
2. **Navigateur réel** (Chrome MCP / computer-use) : ouvre la page produit, télécharge les vraies photos. Par défaut pour la récupération images.
3. **L'utilisateur colle le lien ou dépose les images** : si zéro scraping souhaité.

Demande l'autorisation avant d'ouvrir le navigateur réel.

## Étape 1 — Analyse concurrence visuelle

Avant de produire, regarde les images des top listings Etsy (sortie de l'agent concurrence) :
- Quels fonds dominent (blanc, lifestyle, marbre) ?
- Quels angles ?
- Qu'est-ce qui se ressemble trop (à éviter) ?
- Qu'est-ce qui sort du lot et convertit (à reprendre) ?

## Règles dures (non négociables, vérifier AVANT chaque génération)

1. **Préserver le produit exactement.** Le pipeline modifie le fond, la présentation, l'éclairage et l'angle de vue. **Jamais le produit lui-même** (couleur, forme, proportions, texture restent identiques à l'image source AliExpress). Chaque prompt termine par "preserve the exact product from the source image, only change background, lighting and angle of view".
2. **6 angles de caméra obligatoirement différents.** Une image par shot type, jamais deux shots avec le même point de vue. Cf. `image-prompts.md` section "Les 6 angles obligatoires".
3. **Style cohérent avec la boutique.** Si Shop Identity Card incomplète → DEMANDER avant de générer. Pas de pipeline image sans positionnement + palette + mood + références culturelles définis.

## Étape 2 — Définir l'ambiance (héritée Shop Identity)

L'ambiance vient du positionnement de la Shop Identity Card :

| Positionnement | Fond | Lumière | Mood | Références culturelles |
|----------------|------|---------|------|------------------------|
| Budget | Blanc propre | Neutre, claire | Simple, lisible | E-commerce direct |
| Mid-range | Lifestyle accessible | Naturelle | Lumineux, relatable | Scandi, casual chic |
| Luxury / Premium | Marbre / lin / éditorial | Douce, directionnelle | Premium, matière | Hôtel-spa, French Riviera, Japandi |

Ambiance IDENTIQUE sur toutes les images d'un même produit. Palette cohérente.

## Étape 3 — Générer les prompts (via `image-prompts.md`)

Voir `references/image-prompts.md` pour le système complet de génération.

Pour chaque shot type (hero, lifestyle, detail, variantes, dimensions, packaging), le skill compose automatiquement un prompt en remplaçant les variables `{positioning}`, `{color_palette}`, `{mood}`, `{visual_references}`, `{geography}`, `{product}` depuis la Shop Identity Card.

**Le prompt est en anglais** (FLUX Kontext Pro donne de meilleurs résultats en EN). La description de la boutique reste en français si le marché cible est francophone, mais les prompts d'image transformation = EN.

Présente les 6 prompts à l'utilisateur. Il peut éditer avant lancement.

## Étape 4 — 6 images, 6 angles de caméra différents OBLIGATOIRES

Les 6 shots définis dans `image-prompts.md`, **avec chacun un angle unique** :

| # | Shot type | Angle de caméra |
|---|-----------|-----------------|
| 1 | Hero | 3/4 face légèrement en hauteur (20°) |
| 2 | Lifestyle | Eye level, contextuel |
| 3 | Detail / Macro | Macro parallèle au matériau |
| 4 | Top-down / Flat lay | 90° au-dessus |
| 5 | Side / Profile | 90° latéral pur |
| 6 | Packaging / Lifestyle alt | Eye level, légère plongée 10° |

**Vérification avant lancement :** confirmer que les 6 prompts utilisent 6 angles caméra distincts. Si deux prompts ont le même angle → corriger avant lancer WaveSpeedAI.

Ambiance, palette, mood : IDENTIQUES (cohérence marque). Seuls les angles, fonds et lighting varient.

Le shot 7 optionnel (échelle/dimensions infographie) est créé séparément en design propre (sans IA), si la catégorie le justifie (mesures importantes, dimensions critiques pour l'acheteur).

## Étape 5 — Outils Higgsfield (workflow manuel + MCP partiel)

### Workflow manuel principal (app.higgsfield.ai)

Le skill prépare tout, l'utilisateur exécute :

1. Le skill génère les 6 prompts adaptés à la boutique (voir `image-prompts.md`).
2. Le skill range les 6 images sources dans `photos/source/`.
3. Le skill affiche un récap : prompts + chemin des images sources.
4. L'utilisateur va sur https://app.higgsfield.ai
5. Pour chaque image source :
   - Ouvre le modèle image-to-image disponible (pas Soul)
   - Upload l'image source
   - Colle le prompt généré
   - Lance (~30 sec par image)
   - Télécharge le résultat
6. Place les fichiers téléchargés dans `photos/` avec les noms finaux (`hero.jpg`, `lifestyle.jpg`, etc.)
7. Le skill reprend pour validation et publication.

### Tools MCP Higgsfield (usage limité)

Les tools MCP suivants restent utilisables pour des opérations atomiques quand le résultat est binaire (succès/échec) sans besoin de récupérer l'image :

- `media_import_url` : charger une URL dans Higgsfield (utilisable mais résultat non récupérable)
- `remove_background` : enlever le fond (résultat non récupérable via MCP, à éviter)
- `outpaint_image` : étendre l'image (idem)
- `upscale_image` : upscale 2K/4K (idem)

⚠️ Tant que le MCP n'expose pas `get_job_result`, ces tools sont peu utiles en production. Ne pas en lancer "pour voir" → consomme des crédits sans rendre les fichiers.

### Fallback PIL local (modifications cosmétiques)

Si l'utilisateur ne veut PAS d'abonnement Higgsfield, fallback en local via Python PIL :
- Ajustement colorimétrique (saturation, tons chauds selon positionnement)
- Vignette éditoriale légère
- Nettoyage métadonnées EXIF
- Crop léger

Ces modifs ne changent PAS le décor, mais différencient suffisamment les fichiers pour passer la détection reverse-image basique d'Etsy + alignent le ton couleur sur la marque. Voir script de transformation dans le workspace produit.

## Étape 6 — Réalisme

- Garde le produit réel intact (couleur, forme, matière fidèles à l'original).
- Évite les rendus plastique/IA : ombres cohérentes, reflets réalistes, textures préservées.
- Si une image fait trop IA, refais-la avec un prompt plus précis ou "preserve product exactly" plus fort.

## Étape 7 — Validation (bloquant)

Présente les 5-7 images avec un label court chacune. Demande lesquelles garder, lesquelles refaire.

- Validées → `fiches/[produit]/photos/` avec noms clairs (hero.jpg, lifestyle.jpg, detail.jpg...).
- Non validées → **supprimées**. Pas d'accumulation.
- Refais celles demandées avec un prompt ajusté.

## Format Etsy

- Carré 2000x2000 px minimum, ou 4:5 vertical (1600x2000).
- Première image = hero (la plus importante pour le clic).
- Max 10 images par listing Etsy. On en livre 5-7, plus si variantes.
- FLUX Kontext Pro génère en haute résolution selon l'aspect_ratio. Upscale via Higgsfield MCP si besoin pour zoom Etsy.

## Coûts par fiche (estimation)

| Setup | Coût par fiche (6 images) | Volume max/mois |
|---|---|---|
| PIL local seul (sans abonnement) | 0€ | illimité (mais qualité limitée) |
| Higgsfield Basic abonnement | inclus jusqu'à ~30-50 fiches | 30-50 fiches |
| Higgsfield Plus abonnement | inclus jusqu'à ~150 fiches | 150 fiches |
| WaveSpeedAI FLUX Kontext Pro (pay-per-use) | ~$0.24 (6 images × $0.04) | illimité (selon budget) |

## Apprentissages du test [NomBoutique] (2026-06-23/28)

- MCP Higgsfield n'expose pas `get_job_result` → impossible d'automatiser via MCP seul.
- **Higgsfield Soul = mauvais modèle pour les produits.** Entraine sur les portraits humains, voit des humains dans toutes les textures. Résultats : créatures humaines sorties des serviettes. Ne jamais utiliser Soul pour des produits non-humains.
- **FLUX Kontext Pro = bon modèle.** Conçu pour l'édition d'image avec préservation du sujet. Test [NomBoutique] : 6/6 succès, produit préservé, décor changé, ambiance boutique respectée.
- Le prompt en EN est essentiel (résultats meilleurs qu'en FR).
- La Shop Identity Card est la source de vérité pour le style. Sans elle, les prompts sont génériques.
- **Centrage produit** : ajouter "product fills 70 percent of the frame" dans chaque prompt. Sans ça, le modèle noie le produit dans le décor.
- **Règle du compte d'objets** : FLUX Kontext hérite du nombre d'objets de la source. Pour contrôler le nombre d'articles dans l'image finale, choisir la bonne image source (ex: pour flatlay 3 articles → source avec 3 articles, pas la pile complète).
