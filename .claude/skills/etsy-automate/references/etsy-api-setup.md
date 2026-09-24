# Etsy API Setup

Optionnel. Permet de poster les fiches en brouillon (`state=draft`) directement sur Etsy. Si non configuré, le skill livre le dossier local et c'est tout.

## Ce que ça permet

- Créer un listing en brouillon sur Etsy (titre, description, prix, tags, quantité, catégorie, attributs).
- Uploader les images dessus.
- Tout arrive dans les brouillons du dashboard Etsy. L'utilisateur vérifie et clique Publier lui-même.

## Setup (une fois, 10-15 min)

### Étape 1 — Créer une app Etsy

1. Aller sur https://www.etsy.com/developers et créer une app.
2. Récupérer la **API Key (keystring)** et le **Shared Secret**.
3. **Ajouter le callback URL** dans l'app Etsy (obligatoire) : `http://lvh.me:3003/callback`.
   - Menu Action de l'app -> "Edit callback URLs" -> Add callback URL -> Save.
   - **Pourquoi lvh.me** : Etsy refuse `localhost` et `127.0.0.1` (politique "no IP addresses, host must be a domain name"). `lvh.me` est un domaine public qui résout vers `127.0.0.1` par DNS — ça satisfait Etsy ET garde le flow OAuth entièrement en local.
4. Récupérer le **shop_id** de la boutique (visible dans l'URL du dashboard ou via `GET /v3/application/users/me`).

### Étape 2 — Flow OAuth PKCE

Lance dans un terminal. Méthode recommandée, via variables d'environnement (le secret n'apparait ni dans l'historique du shell ni dans `ps aux`) :

```bash
export ETSY_KEYSTRING=TA_KEYSTRING
export ETSY_SHARED_SECRET=TON_SHARED_SECRET
python3 scripts/etsy_oauth.py --shop-id TON_SHOP_ID
```

Si les variables ne sont pas définies, le script les demande en saisie masquée (getpass). Les flags `--keystring`/`--secret` restent acceptés pour compatibilité mais sont à éviter : un argument de ligne de commande reste visible via `ps aux` le temps de l'exécution, pas seulement dans l'historique.

Le script :
1. Affiche une URL Etsy à coller dans un navigateur.
2. Tu autorises l'accès sur la page Etsy.
3. Le navigateur va sur `lvh.me:3003/callback?code=XXX` et affiche une erreur de connexion (normal — pas de serveur local).
4. Tu copies l'URL complète depuis la barre d'adresse et tu la colles dans le terminal.
5. Le script échange le code, obtient les tokens, et sauvegarde les credentials localement.

**Scopes requis** : `listings_r listings_w listings_d shops_r shops_w`
- `listings_d` est nécessaire pour la suppression de brouillons (`--delete`).
- Si tu veux les données de ventes dans `etsy_stats.py --report`, ajoute `transactions_r` à la liste de scopes dans `etsy_oauth.py` et relance l'OAuth.

### Étape 3 — Re-run OAuth si tu ajoutes des scopes

Si tu as déjà un token mais que tu ajoutes un scope (ex. `listings_d` ajouté après coup), il faut relancer OAuth pour obtenir un token avec les nouveaux scopes. L'ancien token ne se met pas à jour automatiquement.

```bash
# Relancer exactement comme l'étape 2 (variables d'environnement recommandées)
python3 scripts/etsy_oauth.py --shop-id ...
```

Le script écrase les credentials existants.

### Étape 4 — Vérifier la config

```bash
python3 scripts/etsy_draft.py --check
```

Affiche `CONFIGURE` et le shop_id si tout est en ordre.

## Stockage des credentials

```
~/.claude/skills/etsy-automate/.etsy_credentials.json
```

Format complet (tous les champs requis) :
```json
{
  "api_key": "keystring_de_lapp",
  "shared_secret": "shared_secret_de_lapp",
  "access_token": "token_oauth",
  "refresh_token": "refresh_token_oauth",
  "shop_id": "123456789"
}
```

Ce fichier est dans `.gitignore`. Ne jamais le versionner, ne jamais l'afficher dans un output ou dans le chat.

## Endpoints utilisés (API v3)

| Action | Endpoint |
|--------|----------|
| Créer brouillon | `POST /shops/{shop_id}/listings` |
| Upload image | `POST /shops/{shop_id}/listings/{id}/images` |
| Définir attribut | `PUT /listings/{id}/properties/{property_id}` |
| Supprimer brouillon | `DELETE /listings/{id}` |

Base URL : `https://api.etsy.com/v3/application`

Header auth depuis fév. 2026 : `x-api-key: keystring:shared_secret` (format keystring + ":" + shared_secret, pas seulement le keystring).

## Refresh automatique

L'access token expire après ~1h. Le script `etsy_draft.py` le rafraîchit automatiquement via le refresh token en cas de 401. L'utilisateur n'a rien à faire.

## Limites

- Rate limits Etsy : 5 QPS / 5 000 QPD. Ne pas spammer.
- Le brouillon créé via API est en état `draft` — la publication est manuelle dans le dashboard Etsy.
- Etsy demande `who_made: "i_did"` + `when_made: "made_to_order"` pour les produits fabriqués à la commande. `"someone_else"` est refusé (revente pure).
