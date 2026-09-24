# WaveSpeedAI Setup

WaveSpeedAI = passerelle API qui donne accès à **FLUX Kontext Pro** (et autres modèles IA) **en pay-per-use**, sans abonnement mensuel. C'est la solution principale du skill pour transformer les photos AliExpress en visuels alignés à la marque.

**Modèle validé : FLUX Kontext Pro.** Test [NomBoutique] juin 2026 : 6/6 succès, produit préservé, décor changé, $0.24 total.
Ne PAS utiliser Higgsfield Soul pour les produits (entraine sur portraits humains, génère des créatures sur les textures).

## Pourquoi WaveSpeedAI plutôt que Higgsfield direct

| Critère | Higgsfield Starter (€19/mois) | WaveSpeedAI FLUX Kontext |
|---|---|---|
| Type | Abonnement mensuel | Pay-per-use (recharge libre) |
| Coût pour 22 fiches × 6 images/mois | €19 (limite atteinte) | ~$5.30 |
| Coût pour 5 fiches × 6 images/mois | €19 | ~$1.20 |
| Auto via script | Non (web manuel) | Oui (`wavespeed_transform.py`) |
| Engagement | mensuel ou annuel | Aucun |

WaveSpeed gagne jusqu'à ~135 fiches/mois. Au-delà, Higgsfield Plus (€47/mois) devient plus rentable.

## Setup (5 minutes)

1. Va sur https://wavespeed.ai
2. Crée un compte (email ou Google)
3. Dans le dashboard, va dans **API Keys**
4. Génère une clé API (format `wsk_xxxxxxxxxxxx`)
5. Ajoute des crédits initiaux (~$5-10 suffit pour démarrer, recharge libre Stripe)
6. Sauvegarde la clé dans :

```
~/.claude/skills/etsy-automate/.wavespeed_credentials.json
```

Format :
```json
{
  "api_key": "wsk_xxxxxxxxxxxxxxxx"
}
```

7. Vérifie :
```bash
python3 ~/.claude/skills/etsy-automate/scripts/wavespeed_transform.py --check
```

Doit afficher `CONFIGURE` + 8 premiers caractères de la clé.

## Prix exacts (juin 2026)

| Modèle | Prix par image | Use case |
|---|---|---|
| **FLUX Kontext Pro** | **$0.04 / ~€0.037** | Édition image produit, préservation sujet |
| FLUX Kontext Max | $0.08 | Qualité supérieure si nécessaire |

**Estimation budget mensuel** :
- 5 fiches/mois × 6 images = $1.20/mois
- 22 fiches/mois × 6 images = $5.30/mois
- 50 fiches/mois × 6 images = $12/mois

## Endpoint utilisé

- POST `https://api.wavespeed.ai/api/v3/wavespeed-ai/flux-kontext-pro`
- Body JSON :
```json
{
  "prompt": "...",
  "image": "data:image/jpeg;base64,...",
  "aspect_ratio": "3:4",
  "guidance_scale": 3.5
}
```
- Auth : `Authorization: Bearer $API_KEY`
- Polling : GET `https://api.wavespeed.ai/api/v3/predictions/{id}/result`
- Status `completed` → résultat dans `data.outputs[0]`
- Temps moyen : ~10-15 sec par image

Paramètres FLUX Kontext Pro :
- `aspect_ratio` : "3:4" (hero/lifestyle/gift), "1:1" (macro/flatlay/profile), "16:9" si besoin
- `guidance_scale` : 3.5 par défaut, 4.0 si le modèle dévie trop de la source
- **Ne pas utiliser** : `quality`, `size`, `strength` (paramètres Soul, rejetés par Kontext)

L'image source est envoyée en **base64 data URL** (pas besoin d'upload public séparé). Le script `wavespeed_transform.py` gère ça automatiquement.

## Limites

- Pay-per-use strict, chaque image coûte $0.04.
- Si le job échoue (prompt rejeté, timeout serveur), pas de remboursement automatique.
- L'image source doit être < 10 MB en base64 (donc < ~7 MB en JPG).
- Rate limit : ~10 jobs concurrents.

## Sécurité

- Le fichier `.wavespeed_credentials.json` est dans `.gitignore` du skill.
- Ne jamais commit ni partager la clé.
- Si la clé fuit, la révoquer dans le dashboard WaveSpeed et en générer une nouvelle.

## Fallback si WaveSpeedAI down

1. Réessayer plus tard (service stable, downtime rare)
2. Basculer sur Higgsfield web manuel (app.higgsfield.ai)
3. Garder les images PIL modifiées (fallback gratuit, qualité limitée)
