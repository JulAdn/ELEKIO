# Plan d'indexation GSC — À EXÉCUTER PAR JULIAN (après déploiement 479d947)

Le 07/08/2026 : 27 pages connues, 7 indexées, 20 « Détectée, actuellement non indexée », 1 « page avec redirection ».
Les correctifs techniques sont déployés. Il reste à déclencher les re-crawls.

## 1. Valider l'inspection d'URL (après 48h, laisse Google recrawler)
Ouvrir chaque URL dans **Inspection d'URL** (barre du haut GSC) et cliquer **« Demander une indexation »**.
Faire d'abord les 7 pages villes prioritaires (les plus proches du top 3 local) :

1. https://www.elekio.fr/villes/electricien-lavaur
2. https://www.elekio.fr/villes/electricien-toulouse
3. https://www.elekio.fr/villes/electricien-saint-sulpice
4. https://www.elekio.fr/villes/electricien-albi
5. https://www.elekio.fr/villes/electricien-castres
6. https://www.elekio.fr/villes/electricien-montauban
7. https://www.elekio.fr/villes/electricien-gaillac

Puis la 2e vague (7 jours après) : mazamet, graulhet, lunion, balma, ramonville, castanet, saint-orens.

## 2. Vérifier que la « page avec redirection » a disparu
- Page : **Indexation → Pages → onglet « Pages avec redirection »**
- Avant : `/a-propos/` (avec slash) était listé car le sitemap pointait sur la forme avec slash qui fait 308.
- Corrigé : sitemap + canonical + og:url + JSON-LD pointent tous sur `/a-propos` (sans slash).
- Attendu : l'onglet se vide après le prochain crawl. Sinon, demander l'indexation de `https://www.elekio.fr/a-propos`.

## 3. Le sitemap
- Sitemaps → vérifier que `https://www.elekio.fr/sitemap.xml` est **« Réussi »** (pas « A une erreur »).
- Le fichier contient 24 URLs propres, sans `.html`, avec `/a-propos` sans slash.

## 4. Suivi (2-3 semaines)
- Indexation → Pages : le compteur « Détectée, actuellement non indexée » doit baisser vers 0.
- Performance : surveiller les impressions sur les pages villes (elles montaient déjà : 3 → 58 impressions fin juillet/début août).

## Ce qui a été corrigé côté site (commit 479d947)
- `/a-propos` : canonical/og/JSON-LD/sitemap alignés sans slash (levait la contradiction 308↔canonical)
- Home : title/description réorientés « Tarn 81 — Occitanie » (la page ville Saint-Sulpice reprend l'intention locale, fin de la cannibalisation)
- Maillage : chaque page ville lie maintenant les 13 autres pages villes (était 4)
- Services : liens réels vers les pages villes (étaient `href="#"`)
- HTML : 731 guillemets parasites corrigés
