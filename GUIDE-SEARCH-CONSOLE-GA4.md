# 🔧 Guide de configuration — Google Search Console + GA4
## Elekio — Électricien Tarn 81
**Date :** 14 juillet 2026
**Pour :** Julian AUDOUIN

---

## ✅ Ce qui est déjà fait (hier — commit `7557a9d`)

| Élément | Statut |
|---------|--------|
| Balise meta Google Search Console (`g8RZxrg2JnI3FMPADEeKH-jYWPKXyNIrwyvGQQ_jAz8`) | ✅ Sur les 22 pages |
| Google Tag Manager (GTM) `GTM-MC2MQQ23` | ✅ Installé sur les 22 pages |
| Sitemap.xml (22 URLs) | ✅ Complet |
| Robots.txt (réf. sitemap) | ✅ OK |
| HTTPS via Cloudflare | ✅ OK |
| `www.elekio.fr` & `elekio.fr` | ✅ Les deux répondent 200 |

---

## 🔴 ÉTAPE 1 — Finaliser Google Search Console

### 1.1 Aller sur Google Search Console
👉 https://search.google.com/search-console

### 1.2 Ajouter la propriété
- **Type de propriété** : Choisis **"Préfixe d'URL"**
- **URL** : `https://www.elekio.fr/`
- **Clique sur "Continuer"**

### 1.3 Vérification — Méthode recommandée : Balise HTML
Comme tu as déjà ajouté la balise meta hier dans toutes les pages :
1. Google te proposera plusieurs méthodes de vérification
2. Choisis **"Balise HTML"**
3. Tu verras une balise comme `<meta name="google-site-verification" content="...">`
   → **La tienne est déjà en place** (`g8RZxrg2JnI3FMPADEeKH-jYWPKXyNIrwyvGQQ_jAz8`)
4. Clique simplement sur **"Vérifier"**

> ⚠️ **Si tu as créé la propriété avec une autre méthode (DNS TXT)**, ignore l'étape 3. La balise HTML fonctionne aussi. Si Google dit "non vérifié", actualise la page après 5-10 min (le temps que Cloudflare propage).

### 1.4 Alternative : Vérification DNS (plus robuste)
Si tu préfères une vérification qui dure même si tu refais le site :
1. Dans GSC, choisis **"Enregistrement DNS TXT"**
2. Copie la valeur TXT (ex: `google-site-verification=...`)
3. Va sur **Cloudflare Dashboard** → Domaine `elekio.fr` → **DNS**
4. Ajoute un enregistrement :
   - **Type :** `TXT`
   - **Nom :** `@` (ou laisse vide)
   - **Valeur :** colle la clé de vérification
   - **TTL :** Auto
5. Clique **"Vérifier"** dans GSC (attends 1-2 min)

### 1.5 Soumettre le sitemap
Une fois la propriété vérifiée :
1. Va dans le menu de gauche **"Sitemaps"**
2. Dans le champ "Ajouter un nouveau sitemap", entre :
   ```
   sitemap.xml
   ```
3. Clique sur **"Soumettre"**
4. Vérifie après quelques minutes que le statut est **"Réussi"** (22 URLs trouvées)

### 1.6 Vérifier l'indexation
1. Menu gauche → **"Inspection d'URL"**
2. Entre `https://www.elekio.fr/`
3. Clique **"Demander l'indexation"**
4. Tu peux aussi inspecter quelques pages : `services.html`, `about.html`

---

## 🟠 ÉTAPE 2 — Configurer Google Analytics 4 (GA4)

### Option A : Via Google Tag Manager (GTM) — RECOMMANDÉ
GTM est déjà installé (`GTM-MC2MQQ23`). Tu n'as qu'à ajouter le tag GA4 dans GTM.

#### 2.1 Créer la propriété GA4
1. Va sur https://analytics.google.com
2. Clique **"Administrateur"** (en bas à gauche)
3. **"Créer une propriété"** → Choisis GA4
4. Remplis :
   - **Nom :** `Elekio - Site Web`
   - **Fuseau horaire :** `Europe/Paris`
   - **Devise :** `EUR`
5. Sélectionne **"Site Web"**
6. Clique **"Créer"**
7. Note le **Measurement ID** (format `G-XXXXXXXXXX`) — tu en auras besoin

#### 2.2 Ajouter le tag GA4 dans GTM
1. Va sur https://tagmanager.google.com/
2. Connecte-toi avec le même compte Google que GA4
   → Si GTM n'existe pas encore : **"Créer un compte"**
   - Nom du compte : `Elekio`
   - Nom du conteneur : `Elekio - Site Web`
   - Type de cible : **"Site Web"**
   - Container ID : `GTM-MC2MQQ23` (celui déjà dans le code)
3. Une fois dans GTM :
   - Clique **"Ajouter un nouveau tag"**
   - Nom du tag : `GA4 - Page View`
   - **Configuration du tag :**
     - Clique sur l'icône crayon ✏️
     - Choisis **"Google Analytics : balise GA4"**
     - Measurement ID : colle `G-XXXXXXXXXX` (celui de l'étape 2.1)
     - Événement à envoyer : `Page view` (par défaut)
   - **Déclenchement :**
     - Clique sur l'icône déclencheur ⚡
     - Choisis **"All Pages"** (Toutes les pages)
     - Clique sur l'icône de sauvegarde
4. **Publier le conteneur :**
   - Clique sur **"Soumettre"** (en haut à droite)
   - Nom de la version : `V1 - GA4 + Search Console`
   - Clique **"Publier"**

✅ Le tag GA4 est maintenant actif sur toutes les pages du site !

#### 2.3 Vérifier que GA4 reçoit des données
1. Va sur GA4 → **"Temps réel"** (menu gauche)
2. Ouvre `https://www.elekio.fr/` dans un onglet en navigation privée
3. Tu devrais voir 1 utilisateur actif dans les 30 secondes

---

### Option B : Ajout direct du code GA4 (sans GTM)
Si tu préfères ne pas utiliser GTM :

1. Crée la propriété GA4 (idem étape 2.1)
2. Récupère le **Measurement ID** (`G-XXXXXXXXXX`)
3. Dis-le moi, j'ajoute le code GA4 direct sur les 22 pages
4. Je rebuild et redéploie

---

## 🟡 ÉTAPE 3 — Vérifications finales

### 3.1 Voir les premières données GSC
Après 24-48h, Google Search Console commencera à montrer :
- ✅ Nombre de pages indexées
- ✅ Requêtes de recherche qui amènent du trafic
- ✅ Erreurs de crawl éventuelles

### 3.2 Demander l'indexation prioritaire
Dans GSC → **Inspection d'URL** → entre les URLs suivantes une par une et clique "Demander l'indexation" :

1. `https://www.elekio.fr/`
2. `https://www.elekio.fr/services.html`
3. `https://www.elekio.fr/about.html`
4. `https://www.elekio.fr/contact.html`
5. `https://www.elekio.fr/realisations.html`
6. `https://www.elekio.fr/faq.html`
7. `https://www.elekio.fr/villes/electricien-toulouse.html`
8. `https://www.elekio.fr/villes/electricien-albi.html`

### 3.3 Vérifier les Core Web Vitals
Quelques jours après l'indexation :
- GSC → **"Expérience"** → **"Signaux Web essentiels"**
- Vise **vert** sur mobile et desktop

---

## 📋 Récapitulatif — Checklist

- [ ] **ÉTAPE 1** — Ajouté la propriété GSC : `https://www.elekio.fr/`
- [ ] **ÉTAPE 1** — Vérification réussie (balise HTML déjà en place ✅)
- [ ] **ÉTAPE 1** — Sitemap soumis : `sitemap.xml`
- [ ] **ÉTAPE 2** — Propriété GA4 créée (Measurement ID : `G-...`)
- [ ] **ÉTAPE 2** — Tag GA4 configuré dans GTM (ou ajout direct)
- [ ] **ÉTAPE 2** — Données temps réel visibles dans GA4
- [ ] **ÉTAPE 3** — Pages principales demandées à l'indexation
- [ ] **ÉTAPE 3** — Core Web Vitals vérifiés après 1 semaine

---

## 💡 Notes importantes

### Pourquoi GTM plutôt que GA4 direct ?
- Tu pourras ajouter plus tard d'autres tags (Facebook Pixel, conversion tracking) **sans toucher au code du site**
- Le container GTM est déjà installé, tu n'auras qu'à cliquer dans l'interface GTM
- Pas besoin de moi pour ajouter de nouveaux services analytics

### Elekio utilise un sous-domaine elekio.pages.dev ?
Non — ton domaine personnalisé `www.elekio.fr` pointe vers Cloudflare Pages. Tout est bien configuré, le SSL est automatique.

### Si tu vois "Propriété non vérifiée" dans GSC
- Attends 5-10 minutes après avoir ajouté la propriété
- La balise meta est déjà là, Google doit juste crawler le site pour la trouver
- Tu peux accélérer avec **"Inspection d'URL"** → **"Demander l'indexation"**

---

**Des questions ?** Dis-moi où tu bloques et je t'aide étape par étape ! 🚀
