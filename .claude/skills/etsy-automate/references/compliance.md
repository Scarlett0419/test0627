# Compliance Etsy

À lire et à signaler à l'utilisateur. Ne jamais cacher ce risque.

## Le point dur : dropshipping AliExpress interdit

Etsy interdit la revente de produits AliExpress génériques. Règle officielle : les articles doivent être faits main, conçus par le vendeur, ou vintage. Revendre un produit AliExpress tel quel = motif de **suspension de boutique**.

Source : politique Etsy « Does Etsy Allow Drop Shipping or Reselling ».

Seule exception : Craft and Party Supplies (fournitures créatives et de fête).

## Ce que le skill doit faire

1. **Avertir l'utilisateur** dès qu'il source de l'AliExpress pour revente Etsy. Une fois, clairement, sans dramatiser ni cacher.
2. **Proposer les modèles conformes** (voir plus bas).
3. Ne jamais prétendre que l'automatisation rend la chose conforme. L'API automatise le dépôt, pas la conformité.
4. Laisser l'utilisateur décider en connaissance de cause.

## Modèles conformes (gardent le pipeline)

| Modèle | Conforme ? | Ce qui change |
|--------|-----------|---------------|
| Print-on-demand (Printful/Printify) | Oui, si tu déclares le partenaire de production | Tu conçois le design, le partenaire imprime. Pipeline SEO/images/fiches identique. |
| AliExpress + conception ajoutée | Zone grise | Gravure, personnalisation, bundle conçu par toi. Moins risqué que la revente pure, pas garanti. |
| Vintage (20 ans et +) | Oui | Sourcing différent, pas AliExpress neuf. |
| Craft/Party supplies AliExpress | Oui (exception) | Seule catégorie où le dropshipping pur passe. |
| Revente AliExpress brute | Non | Risque de suspension. |

## Pour le POD (recommandé)

Si l'utilisateur bascule sur POD, le skill garde tout sauf le sourcing AliExpress :
- Niche Finder : identique.
- Listing Generator : identique.
- Image Pipeline : génère les mockups POD au lieu de retravailler des photos AliExpress.
- Sourcing : remplacé par le choix du produit POD et du design.
- Déclarer le partenaire de production dans la section « À propos » de la boutique (obligatoire Etsy).

## Le piège who_made dans l'API

L'API Etsy v3 rejette `who_made: "someone_else"` avec une erreur 400. Ce skill utilise donc `who_made: "i_did"` comme valeur par défaut pour que le brouillon passe. C'est une contrainte technique de l'API, pas une déclaration de vérité.

**L'utilisateur est seul responsable** de la valeur qu'il choisit de publier et de ce qu'elle signifie vis-à-vis des CGU Etsy. Le skill génère un brouillon, pas une publication.

## Règles API en plus

- Accès personnel : jusqu'à 5 boutiques. Au-delà, accès commercial à faire valider par Etsy.
- Header x-api-key au format `keystring:shared_secret` depuis le 9 février 2026.
- Créer les listings en `draft` (recommandé par Etsy, évite les frais avant publication).
- Respecter les rate limits et la politique de cache.

Source API : politique API Etsy et documentation v3.
