# AliExpress Sourcing

Agent de sourcing. Trouve le produit au meilleur rapport prix/qualité et recommande 3 vendeurs.

## Mandat

Pour un produit donné (lien ou description) :

1. Prix min / max / moyenne / médiane sur le marché AliExpress.
2. 3 vendeurs recommandés avec scoring.
3. Liens directs.
4. Images du produit (pour le pipeline image plus tard).

## Méthode de récupération

### Option prioritaire : API Affiliate (si configurée)

Vérifie d'abord :

```bash
python3 ~/.claude/skills/etsy-automate/scripts/aliexpress_api.py --check
```

Si configurée, utilise-la : prix, images, infos produit propres, sans anti-bot. C'est le plus fiable. Voir `aliexpress-api-setup.md`.

### Sinon : cascade selon le niveau choisi

Le niveau de précision est demandé au lancement du pipeline (voir SKILL.md).

**Niveau rapide (1 et 2) :**
1. **WebFetch direct** sur la page produit ou recherche AliExpress.
2. **WebSearch Google** : `site:aliexpress.com "[produit]"` puis extraire prix et notes des snippets.
3. **Google Shopping** : `[produit] aliexpress prix` pour une fourchette.

Sans état, donc parallélisable : lance un sous-agent par vendeur candidat pour charger plusieurs pages d'un coup.

**Niveau précis (3) — navigateur réel :**
Ouvre les vraies pages AliExpress via Chrome MCP ou computer-use. Lis les prix exacts, les avis, récupère les images haute résolution. Séquentiel (un seul navigateur partagé). Demande l'autorisation à l'utilisateur avant.

Labellise toujours si les données viennent d'un fallback estimé (« estimation via Google, page inaccessible »).

## Scoring vendeur

Pour chaque vendeur candidat, note :

| Critère | Seuil minimum | Idéal |
|---------|---------------|-------|
| Note vendeur | ≥ 4.5 / 5 | ≥ 4.7 |
| Nombre de commandes | **≥ 1000** (produit testé en volume) | ≥ 5000 |
| Avis récents | Majorité positifs sur 6 derniers mois | Tendance stable |
| Délai de livraison | ≤ 30 jours | ≤ 15 jours |
| Prix | Cohérent avec la qualité | Sweet spot prix/qualité |

**Règle par défaut : ne pas recommander un vendeur sous 1000 commandes pour une boutique premium.** Le risque de mauvais avis client sur Etsy est trop élevé si le produit n'a pas été testé en volume.

**Dérogation possible** sur la règle des 1000 si les 3 conditions suivantes sont réunies :
1. Note vendeur ≥ 4.5 / 5
2. Badge AliExpress "qualité premium" ou "Le plus vendu sur AliExpress" visible sur la page produit
3. Avis vérifiés existants spécifiquement pour la variante 70x140 (ou la variante cible)

Dans ce cas, accepter entre 700 et 1000 commandes, mais le justifier explicitement dans le sourcing output. Exemple : "800 vendus, dérogation acceptée : 4.6/5 + badge premium + 229 avis vérifiés sur taille cible."

Si tu ne trouves pas de vendeur au-dessus du seuil en mode rapide, dis-le clairement et suggère de passer en mode navigateur réel pour creuser.

Recommande celui qui équilibre prix et fiabilité, pas juste le moins cher. Un produit à 1.90 avec 4.3/5 et 200 commandes est plus risqué qu'un à 2.30 avec 4.7/5 et 8000 commandes. Dis-le.

## Toujours proposer 2 stratégies, pas 1

À la fin du sourcing, présente deux options à l'utilisateur :

**Option A - Marge max** : source le moins cher acceptable, marge élevée mais qualité possiblement moyenne.
**Option B - Premium aligné marque** : source plus cher mais qualité 4.7+ et 1000+ commandes, marge réduite mais réputation protégée.

Le choix dépend du positionnement de la Shop Identity Card :
- Boutique budget/mid-range → Option A souvent OK.
- Boutique luxury/premium → Option B fortement recommandée. Les premiers avis font la réputation, un avis 3 étoiles sur une marque premium coûte cher.

Donne ton avis tranché, ne fais pas le neutre.

## Output

```
PRIX MARCHÉ ALIEXPRESS
Min : X | Max : Y | Moyenne : Z | Médiane : W

3 VENDEURS RECOMMANDÉS
1. [Nom] — prix — note/5 — N commandes — délai Nj — [lien]
2. ...
3. ...

RECOMMANDATION : vendeur N, parce que [raison équilibre prix/fiabilité]

IMAGES RÉCUPÉRÉES : [liste des URLs ou note si non accessibles]
```

Sauvegarde dans la section sourcing de `fiche.md` du produit.

## Changement de fournisseur

Si le fournisseur actuel tombe en rupture ou est remplacé par un meilleur, voici le protocole :

1. **Vérifier le stock** : ouvrir la page produit en navigateur réel. "Seulement N restants" (N < 10) = alerte rupture imminente. AliExpress dé-rank les articles en rupture → ils disparaissent des recherches.
2. **Trouver un remplaçant** : relancer le sourcing avec les mêmes critères. Navigateur réel recommandé.
3. **Mettre à jour `fiche.md`** :
   - Section "Vendeur AliExpress recommandé" : barrer l'ancien avec `~~texte~~`, ajouter le nouveau.
   - Section "Prix" : recalculer la marge avec le nouveau coût.
   - Section "Variantes" : vérifier que les couleurs disponibles correspondent encore à la palette boutique.
   - Section "Statut" : marquer "Photos source à renouveler".
4. **Nouvelles photos source** : les photos de l'ancien fournisseur ne correspondent plus. Récupérer les images haute résolution du nouveau produit (navigateur réel, réseau Chrome MCP).
5. **Relancer le pipeline image** : nouvelles sources → nouveaux prompts si nécessaire → FLUX Kontext ou Higgsfield → validation.
6. **Mettre à jour le brouillon Etsy** : remplacer les images via `etsy_draft.py` ou manuellement.

**Règle : ne jamais publier des photos du fournisseur A avec un lien vers le fournisseur B.** Les photos doivent correspondre au produit effectivement expédié.
