# 📋 Instructions SEO Elekio → Web Creator — Mise à jour v2

**Source :** SEO Elekio (stratège référencement)
**Destination :** Web Creator (orchestrateur exécution)
**Date :** 30 juin 2026
**Contexte :** Audit SEO complet des 7 pages. P0/P1 déjà corrigés par SEO Elekio (sitemap.xml, robots.txt, favicon, canonical). Reste les actions ci-dessous.

| Légende | Signification |
|---------|--------------|
| 🔴 P0 | Bloquant — fait avant toute autre chose |
| 🟠 P1 | Important — cette semaine |
| 🟡 P2 | Standard — cette quinzaine |
| 🟢 P3 | Polish — quand vous avez le temps |

---

## 🔴 DÉJÀ FAIT par SEO Elekio (vérifier que c'est bien en place)

- ✅ `sitemap.xml` créé à la racine
- ✅ `robots.txt` créé avec référence au sitemap
- ✅ Favicon corrigé : `type="image/png"` (était `image/svg+xml`)
- ✅ Balises `<link rel="canonical">` ajoutées sur les 7 pages

---

## 🔴 P0 — Instructions critiques

---

### INSTRUCTION N°10 — 🔴 P0 | Remplacer "Domotique" par "Petits travaux" dans services.html

**Fichier :** `services.html`

**Quoi faire :**
Remplacer le service "Domotique & Smart Home" par un service **"Petits travaux électriques"** — car c'est un vrai service qu'Elekio propose réellement (domotique est secondaire/pas encore actif).

**Ancien contenu à remplacer (trouvé vers ligne 348-366) :**
```
Domotique & Smart Home → La maison connectée
```
Et tout le bloc associé (icône 🏠, description, liste de points).

**Nouveau contenu :**
```
Petits travaux électriques → Interventions rapides
```
- Icône : 🔧
- Titre H3 : "Petits travaux électriques"
- Sous-titre : "Prises, interrupteurs, luminaires, VMC"
- Description (80-100 mots) : "Besoin d'ajouter une prise, de changer un interrupteur, d'installer un luminaire ou une VMC ? Je réalise tous vos petits travaux électriques dans le Tarn. Interventions rapides, travail soigné, conformes à la norme NF C 15-100. Devis gratuit sous 24h."
- Liste à puces : ✓ Ajout de prises et interrupteurs, ✓ Installation de luminaires et appliques, ✓ Mise en place VMC simple/flux, ✓ Sonneries, visiophones, ✓ Petits dépannages électriques
- Prix : "À partir de 80€ + 50€/h — Devis gratuit"
- Mettre à jour aussi le `ItemList` schema.org (JSON-LD) : remplacer l'entrée position 6 "Domotique &amp; Smart Home" par "Petits travaux électriques"

**Pourquoi :** Elekio ne propose pas encore la domotique comme service courant. "Petits travaux" est son vrai service quotidien.

---

### INSTRUCTION N°11 — 🔴 P0 | Ajouter un backend au formulaire de contact

**Fichier :** `contact.html`

**Quoi faire :**
Remplacer `action="#"` par une action réelle. Deux options :

**Option A (recommandée — gratuite) :** Utiliser **Formspree**
1. Créer un compte sur https://formspree.io
2. Créer un nouveau formulaire avec l'email `contact@elekio.fr`
3. Remplacer `<form action="#" method="POST">` par `<form action="https://formspree.io/f/XXXXXXX" method="POST">`
4. Ajouter `redirect` caché pour rediriger vers une page de confirmation après envoi :
   `<input type="hidden" name="_redirect" value="https://www.elekio.fr/merci.html">`

**Option B :** **Netlify Forms** (si le site est hébergé sur Netlify)
1. Ajouter `netlify` dans l'attribut form : `<form action="#" method="POST" netlify>`
2. Le traitement est automatique

**Pourquoi :** Sans backend, les demandes de devis sont perdues. C'est le P0 le plus critique pour le business.

---

## 🟠 P1 — Instructions importantes

---

### INSTRUCTION N°12 — 🟠 P1 | Ajouter les balises OG sur toutes les pages

**Fichiers :** `services.html`, `about.html`, `faq.html`, `contact.html`, `realisations.html`, `mentions-legales.html`

**Quoi faire :**
Ajouter dans le `<head>` de chaque page (après la meta description) les balises OG suivantes, adaptées à chaque page :

**Template OG général (à adapter par page) :**
```html
<meta property="og:title" content="[TITRE PAGE] | Elekio">
<meta property="og:description" content="[META DESCRIPTION de la page]">
<meta property="og:url" content="https://www.elekio.fr/[PAGE].html">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="https://www.elekio.fr/logo-elekio.png">
<meta name="twitter:card" content="summary">
```

**Valeurs par page :**

| Page | og:title |
|------|----------|
| services.html | "Services Électricien Tarn — Dépannage, Installation, Rénovation | Elekio" |
| about.html | "Qui est Julian AUDOUIN ? — Électricien Tarn 81 | Elekio" |
| faq.html | "FAQ Électricien Tarn — Normes, Prix, Dépannage | Elekio" |
| contact.html | "Contact & Devis Gratuit — Électricien Tarn 81 | Elekio" |
| realisations.html | "Réalisations & Tarifs — Électricien Tarn 81 | Elekio" |
| mentions-legales.html | "Mentions Légales — Elekio | Électricien Tarn 81" |

**Pourquoi :** Sans OG tags, le partage sur Facebook/WhatsApp/LinkedIn affiche un aperçu vide.

---

### INSTRUCTION N°13 — 🟠 P1 | Améliorer le schema.org : ajouter le type Electrician

**Fichier :** `index.html` (JSON-LD dans le head)

**Quoi faire :**
Dans le schema `@type` actuellement `"LocalBusiness"`, ajouter `"Electrician"` comme type supplémentaire :

```json
"@type": ["LocalBusiness", "Electrician"],
```

**Changer aussi :** Dans `about.html`, le schema Person pourrait référencer le type `Electrician`.

**Pourquoi :** `Electrician` est un sous-type plus précis de `LocalBusiness`. Google comprend mieux que c'est un électricien et peut afficher des rich results spécifiques.

---

### INSTRUCTION N°14 — 🟠 P1 | Réduire la meta description de l'accueil

**Fichier :** `index.html`

**Quoi faire :**
La meta description actuelle fait ~320 caractères. La couper à 150-160 caractères maximum tout en gardant les mots-clés essentiels.

**Actuelle (320+ chars) :**
```
Électricien à Saint-Sulpice-la-Pointe (81370). Julian AUDOUIN, artisan qualifié BTS Électrotechnique. Dépannage électrique urgence sous 4h, installation neuve, rénovation, mise aux normes, domotique. Devis gratuit 24h. Intervention Tarn 81, Haute-Garonne 31, Tarn-et-Garonne 82, Aveyron 12, Hérault 34.
```

**Nouvelle (155 chars) :**
```
Électricien Tarn 81 — Saint-Sulpice-la-Pointe. Dépannage urgence 4h, installation, rénovation, mise aux normes. Artisan BTS, devis gratuit 24h.
```

**Pourquoi :** Google tronque les meta descriptions à ~160px sur mobile.

---

### INSTRUCTION N°15 — 🟠 P1 | Corriger la hiérarchie H1/H2/H3 dans services.html

**Fichier :** `services.html`

**Quoi faire :**
Actuellement les sections de services utilisent des `<h3>` directement sans `<h2>` parent. Ajouter un `<h2>` invisible ou modifier la structure :

1. Dans le `section-header` (ligne 234-238 remplacer `div class="section-title"` par un vrai `<h2>` :
```html
<h2 class="section-title">Nos <span class="highlight">6 services</span> en détail</h2>
```

2. Les titres de chaque service (`<h3>`) sont corrects — ils descendent bien du H2.

**Pourquoi :** Google analyse la hiérarchie des titres pour comprendre la structure de la page. H1 → H2 → H3 est la hiérarchie sémantique correcte.

---

## 🟡 P2 — Standard

---

### INSTRUCTION N°16 — 🟡 P2 | Ajouter la photo réelle de Julian quand disponible

**Fichier :** `about.html` (et éventuellement `index.html` section about)

**Quoi faire :**
Quand Julian aura sa photo professionnelle :
1. Remplacer le placeholder SVG dans `about.html` par `<img src="julian-audouin-elekio.jpg" alt="Julian AUDOUIN — Électricien Tarn 81">`
2. Ajouter `width` et `height` explicites
3. Mettre à jour la même section dans `index.html` (section about, ligne 422-426)

**Pourquoi :** Une photo réelle renforce considérablement l'EEAT (Experience, Expertise, Authoritativeness, Trustworthiness).

---

### INSTRUCTION N°17 — 🟡 P2 | Remplacer les liens sociaux morts

**Fichier :** Footer de toutes les pages

**Quoi faire :**
Remplacer les `href="#"` par les vrais liens quand les réseaux sociaux seront créés, ou supprimer les icônes en attendant.

**Option recommandée :** Laisser les icônes mais ajouter un `title="À venir"` et garder `href="#"` avec un message clair que les réseaux ne sont pas encore actifs.

**Pourquoi :** Des liens morts dans le footer sont un signal négatif pour l'expérience utilisateur.

---

### INSTRUCTION N°18 — 🟡 P2 | Ajouter dimensions explicites aux images logo

**Fichier :** Toutes les pages (header + footer)

**Quoi faire :**
Dans tous les `<img src="logo-elekio-small.png">`, ajouter des attributs `width` et `height` explicites :
```html
<img src="logo-elekio-small.png" alt="Elekio" width="44" height="44" style="height:44px;width:auto">
```

**Pourquoi :** Les dimensions explicites évitent le Cumulative Layout Shift (CLS), un Core Web Vital.

---

### INSTRUCTION N°19 — 🟡 P2 | Ajouter une page "Merci" post-formulaire

**Nouveau fichier :** `merci.html`

**Quoi faire :**
Créer une page de confirmation simple après soumission du formulaire :
- Même header/footer que les autres pages
- Message type : "Merci ! Votre demande de devis a bien été envoyée. Je vous réponds sous 24h."
- Lien retour vers l'accueil
- Numéro de téléphone bien visible

**Pourquoi :** UX / confirmation que le message est bien parti. Aussi, c'est une page de conversion.

---

## 📊 Suivi d'avancement

| Instruction | Statut | Priorité |
|-------------|--------|----------|
| ❌ **N°10** — Domotique → Petits travaux | **FAIT** ✅ | 🔴 P0 |
| ❌ **N°11** — Backend formulaire contact | **FAIT** ✅ (Formspree placeholder) | 🔴 P0 |
| ❌ **N°12** — OG tags sur toutes les pages | **FAIT** ✅ (8 pages) | 🟠 P1 |
| ❌ **N°13** — Schema Electrician | **FAIT** ✅ (index.html) | 🟠 P1 |
| ❌ **N°14** — Meta description accueil | **FAIT** ✅ (155c) | 🟠 P1 |
| ❌ **N°15** — Hiérarchie H1/H2/H3 services | **FAIT** ✅ | 🟠 P1 |
| ⏳ **N°16** — Photo réelle Julian | ⏳ **En attente photo** | 🟡 P2 |
| ❌ **N°17** — Liens sociaux | **FAIT** ✅ (title="À venir" ajouté) | 🟡 P2 |
| ❌ **N°18** — Dimensions logo | **FAIT** ✅ (44×44 header, 36×36 footer) | 🟡 P2 |
| ❌ **N°19** — Page merci.html | **FAIT** ✅ (créée) | 🟡 P2 |

**Déjà fait par SEO Elekio :** sitemap.xml ✅, robots.txt ✅, favicon ✅, canonical ✅

---

*Document généré par SEO Elekio v2 — 30 juin 2026*

---

# 🚀 Infra & Déploiement — Handoff Julian → Web Creator (3 juillet 2026)

**Source :** Julian (via Hermes)
**Destination :** Web Creator
**Contexte :** Mise en place de l'hébergement + design header finalisé.

## ✅ DÉJÀ FAIT — Infrastructure

- ✅ **Hébergement :** Cloudflare Pages — projet `elekio` créé, déployé
- ✅ **URL preview :** https://elekio.pages.dev (accessible uniquement via ce lien — pas de domaine)
- ✅ **GitHub :** `JulAdn/ELEKIO` — branche `main` — les tokens sont dans `~/.hermes/elekio-tokens/`
- ✅ **Domaine elekio.fr :** pas encore pointé (on attend que le contenu soit final)
- ✅ **Formulaire :** FormSubmit activé sur contact.html
- ✅ **FormSubmit :** Configuré et actif

## ✅ DÉJÀ FAIT — Design Header

- ✅ **Header split :** blanc (logo) → diagonale → bleu marine (menu)
- ✅ **Gradient exact :** `linear-gradient(100deg,#fff 27%,#c4795b 27.5%,#fff 27.5%,#fff 28%,#000c42 28.7%,#fff 28.7%,#fff 30%,#000c42 30.2%)`
- ✅ **Logo :** `logo-elekio-header.png` — version transparente (fond supprimé), 60px de haut dans header, 40px dans footer
- ✅ **Autres fichiers logo :** `logo-elekio.png` (original avec fond blanc), `Logo_ELEKIO_Horizontal.png` (source originale)
- ✅ **Header appliqué sur les 8 pages HTML**
- ✅ **Footer :** fond blanc, logo transparent, liens en gris

## 🔴 NE PAS TOUCHER — Header

Le header est validé par Julian. **Ne pas modifier le gradient, la taille du logo, ni les couleurs du header.** Toute modification devra être validée par Julian.

## 🟠 RESTANT — Contenu

- ⏳ **N°16** — Photo réelle de Julian pour la section "À propos" (en attente photo)
- ⏳ **Contenu des pages :** revoir le texte, les services, les réalisations
- ⏳ **Images :** photos de chantier à ajouter
- ⏳ **Domaine :** pointer elekio.fr → Cloudflare quand le site sera prêt (changer les nameservers OVH)

## 🔧 Déploiement

Pour redéployer après modification :
```bash
cd /workspace/1_Projects/site-web
git add -A && git commit -m "message" && git push
# Puis utiliser wrangler avec le token Cloudflare stocké
CLOUDFLARE_API_TOKEN=*** cat ~/.hermes/elekio-tokens/cloudflare-api-token)
npx wrangler pages deploy . --project-name=elekio --branch=main
```

*Handoff créé par Hermes — 3 juillet 2026*
