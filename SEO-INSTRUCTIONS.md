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

---

# 📋 Instructions SEO Elekio → Web Creator — v3 (13 juillet 2026) — Inspirations Stepizy

**Source :** SEO Elekio — après analyse de la formation Stepizy (9 modules, 47 leçons)
**Date :** 13 juillet 2026
**Contexte :** Nouvelles instructions issues des apprentissages de la formation. Les instructions N°10-19 de la v2 sont toutes terminées.

| Légende | Signification |
|---------|--------------|
| 🟠 P1 | Important — cette semaine |
| 🟡 P2 | Standard — cette quinzaine |
| 🟢 P3 | Polish — quand vous avez le temps |

---

## 🟠 P1 — Instructions importantes

---

### INSTRUCTION N°20 — 🟠 P1 | Calendrier éditorial Google Posts GBP (3x/semaine)

**Cible :** Google Business Profile d'Elekio (tableau de bord GBP)

**Quoi faire :**
Créer un fichier `gmb-posts-calendar.md` avec un template de 12 posts prêts à copier-coller dans Google Business Profile, à raison de 3 posts par semaine (lundi, mercredi, vendredi).

**Structure du template par post :**
```markdown
## Post [Jour] — [Date]

📷 **Image suggérée :** [description de l'image à prendre]
📝 **Texte :** [30-60 mots — pas plus]
🔗 **Bouton :** [Devis gratuit / En savoir plus / Prendre RDV]
🏷️ **Hashtags :** #ÉlectricienTarn #Elekio #SaintSulpice
```

**Les 12 posts à préparer :**

| # | Thème | Type | Image suggérée |
|---|-------|------|----------------|
| 1 | Dépannage urgence 4h | Service | Photo du véhicule ou outils |
| 2 | Mise aux normes installation | Conseil | Avant/après tableau électrique |
| 3 | Pourquoi un diagnostic obligatoire ? | Info utile | Photo compteur/tableau |
| 4 | Remplacement tableau électrique | Service | Photo vieux tableau → neuf |
| 5 | Petits travaux : prise, interrupteur | Service | Photo prise/interrupteur installé |
| 6 | VMC : quelle différence simple/flux ? | Conseil | Photo VMC |
| 7 | Norme NF C 15-100 : c'est quoi ? | Éducation | Photo schéma norme |
| 8 | Devis gratuit sous 24h | Promo | Photo Julian souriant |
| 9 | Intervient dans 30km autour de St-Sulpice | Zone | Photo carte zone |
| 10 | Astuce sécurité : ne pas bricoler soi-même | Conseil | Photo outil/chantier |
| 11 | Chantier du mois — avant/après | Réalisations | Avant/après chantier réel |
| 12 | Témoignage client | Social Proof | Citation client + photo |

**Pourquoi :** La formation Stepizy confirme que les Google Posts 3x/semaine sont un des 81 facteurs GBP. Google voit la fiche active et la récompense dans le Local Pack. C'est gratuit et immédiat.

**Format du fichier :** `gmb-posts-calendar.md` à la racine du projet. Le contenu est à copier-coller par Julian dans son tableau de bord GBP.

---

### INSTRUCTION N°21 — 🟠 P1 | Créer les pages locales pour le top 5 des villes de la zone

**Cible :** 5 nouveaux fichiers HTML : `castres.html`, `lavaur.html`, `albi.html`, `mazamet.html`, `gaillac.html`

**Méthode (améliorée par la formation Stepizy) :**

Pour chaque ville, créer une page locale avec **cette structure précise** :

**Phase 1 — Recherche de contenu (faite par SEO Elekio) :**
Pour chaque ville, SEO Elekio fournira :
- Les données locales pertinentes (via Perplexity)
- La sémantique enrichie (via Gemini)
- Les entités nommées

**Phase 2 — Structure de page (exécutée par Web Creator) :**

Créer un fichier `template-page-locale.html` avec cette structure :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Électricien [Ville] ([CP]) — Dépannage 4h | Elekio</title>
  <meta name="description" content="Électricien à [Ville] ([CP]) — Intervention sous 4h. Installation, rénovation, mise aux normes, dépannage urgence. Artisan BTS, devis gratuit 24h. ☎️ 06 80 50 67 09">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://www.elekio.fr/[ville].html">
  <!-- OG tags -->
  <meta property="og:title" content="Électricien [Ville] ([CP]) — Elekio | Dépannage 4h">
  <meta property="og:description" content="Électricien à [Ville]. Intervention sous 4h. Devis gratuit 24h. ☎️ 06 80 50 67 09">
  <meta property="og:url" content="https://www.elekio.fr/[ville].html">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://www.elekio.fr/logo-elekio.png">
  <meta name="twitter:card" content="summary_large_image">
  <!-- Schema.org LocalBusiness pour cette ville -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": ["LocalBusiness", "Electrician"],
    "name": "Elekio",
    "description": "Électricien à [Ville] — dépannage, installation, rénovation",
    "url": "https://www.elekio.fr",
    "telephone": "0680506709",
    "email": "contact@elekio.fr",
    "areaServed": {
      "@type": "City",
      "name": "[Ville]",
      "sameAs": "https://fr.wikipedia.org/wiki/[Ville]"
    },
    "parentOrganization": {
      "@type": "LocalBusiness",
      "@id": "https://www.elekio.fr/#organization"
    }
  }
  </script>
</head>
<body>
  <!-- Même header que les autres pages -->
  <main>
    <!-- H1 : Électricien [Ville] — Dépannage, Installation, Rénovation -->
    <!-- H2 : Services d'électricien à [Ville] (avec liste des 6 services) -->
    <!-- H2 : Pourquoi choisir Elekio à [Ville] ? (EEAT + spécificités locales) -->
    <!-- H2 : Zone d'intervention (citer les communes autour de [Ville]) -->
    <!-- H2 : Tarifs de nos interventions à [Ville] -->
    <!-- H2 : Questions fréquentes sur l'électricien à [Ville] (FAQ locale) -->
    <!-- H2 : Contact et devis gratuit -->
  </main>
  <!-- Même footer que les autres pages -->
</body>
</html>
```

**Phase 3 — Intégration :**
1. Copier le template pour chaque ville
2. Remplacer [Ville], [CP] par les vraies données
3. Ajouter les données locales spécifiques (patrimoine, quartiers, particularités)
4. Ajouter un lien vers la ville dans la section "Zone d'intervention" de `index.html`
5. Ajouter la page dans le `sitemap.xml`

**Top 12 villes prioritaires (rayon 50km) — Palier 1 Premium :**

| # | Ville | CP | Distance | Pop. | Pourquoi cette ville |
|---|-------|----|----------|------|---------------------|
| 1 | **Toulouse** | 31000 | 27 km ✅ | 500 000+ | Méga-marché. 30+ électriciens en concurrence mais volume ×50 |
| 2 | **Castres** | 81100 | 48 km ✅ | 42 000 | Plus grande ville du Tarn après Albi. Fort besoin artisans |
| 3 | **Albi** | 81000 | 41 km ✅ | 50 000 | Préfecture. Beaux quartiers, résidences secondaires |
| 4 | **Montauban** | 82000 | 38 km ✅ | 62 000 | Préfecture Tarn-et-Garonne. Gros bassin |
| 5 | **Gaillac** | 81600 | 22 km ✅ | 16 000 | Vignoble, résidences, en croissance |
| 6 | **L'Union** | 31240 | 20 km ✅ | 12 000 | Banlieue nord Toulouse, très accessible |
| 7 | **Balma** | 31130 | 24 km ✅ | 17 000 | Banlieue est Toulouse, technopole |
| 8 | **Graulhet** | 81300 | 24 km ✅ | 13 000 | 3e ville du Tarn, zone industrielle |
| 9 | **Lavaur** | 81500 | 14 km ✅ | 11 000 | Proche St-Sulpice, zone commerciale |
| 10 | **Ramonville** | 31520 | 30 km ✅ | 15 000 | Banlieue sud Toulouse, technopole |
| 11 | **Castanet** | 31320 | 32 km ✅ | 15 000 | Banlieue sud Toulouse, en expansion |
| 12 | **Saint-Orens** | 31650 | 27 km ✅ | 13 000 | Banlieue sud-est Toulouse, zone commerciale |

**Palier 2 — Standard (10 villes, ajout ultérieur) :**
Castelginest, Aucamville, Launaguet, Fenouillet, Rabastens, Fronton, Villemur-sur-Tarn, Escalquens, Mazamet, Verfeil.

**⚠️ Règle absolue — Pas de contenu dupliqué :**
Chaque page doit avoir du contenu unique. Pas de simple copier-coller avec juste le nom de ville changé → Google considère ça comme des **doorway pages** et peut pénaliser tout le site. Différenciation minimale : quartiers spécifiques, monuments, zones d'activité, temps d'accès réel, spécificités locales.

**Pourquoi :** Les pages locales sont LE levier SEO N°1 pour un artisan de service. La formation Stepizy confirme cette approche avec sa méthode validée. 12 pages × mot-clé local = 12 portes d'entrée dans Google.

**Contrainte :** Utiliser le **même header/footer que les pages existantes** (pas de redesign). Le contenu textuel de chaque page sera fourni par SEO Elekio.

---

## 🟡 P2 — Instructions standard

---

### INSTRUCTION N°22 — 🟡 P2 | Vérification checklist 81 facteurs GBP

**Cible :** Google Business Profile d'Elekio

**Quoi faire :**
Partager à Julian la checklist suivante pour valider que la fiche GBP est optimisée. Créer un fichier `gmb-checklist-81.md` à la racine du projet.

**Les 15 points critiques à vérifier en priorité :**

| # | Facteur | Statut | Vérifié ? |
|---|---------|--------|-----------|
| 1 | Adresse masquée correctement (service itinérant) | ✅ Fait | |
| 2 | Zone de service : 30-50km autour de St-Sulpice | ✅ Fait | |
| 3 | Catégorie principale : Électricien | ✅ Fait | |
| 4 | Catégories secondaires (max 2) : Service d'installation électrique, Service de dépannage électrique | ✅ Fait | |
| 5 | Téléphone : 06 80 50 67 09 (local) | ✅ Fait | |
| 6 | Site web : elekio.fr | ⏳ Pas encore public | |
| 7 | Horaires d'ouverture à jour + jours fériés | ⏳ À vérifier | |
| 8 | Horaires élargis (plus larges que concurrents) | 🔴 À définir | |
| 9 | Services natifs Google (5 par défaut) + services personnalisés (8) | ✅ Fait | |
| 10 | Services avec prix + description + lien | ⏳ À vérifier | |
| 11 | +20 photos haute qualité | ⏳ Julian doit fournir | |
| 12 | Photo de couverture + logo | ✅ Fait (logo transmis) | |
| 13 | Google Posts 3x/semaine (cf INSTRUCTION N°20) | 🔴 À démarrer | |
| 14 | Réponse aux avis (tous, dans les 24h) | 🔴 Pas encore d'avis | |
| 15 | Attributs d'identité : "Électricien", "Artisan", "Indépendant" | ⏳ À vérifier | |

**Créer le fichier complet** avec les 81 facteurs répartis en 5 sections :
1. Compléter la fiche à 100% (15 facteurs)
2. Optimiser le référencement local (18 facteurs)
3. Gérer les avis clients (15 facteurs)
4. Publier du contenu régulièrement (18 facteurs)
5. Analyser et ajuster (15 facteurs)

**Pourquoi :** La formation Stepizy détaille 81 facteurs GBP. Même si beaucoup sont déjà en place, une checklist permet de ne rien oublier. C'est la fiche GBP qui drive le Local Pack = les appels directs.

---

### INSTRUCTION N°23 — 🟡 P2 | Structurer le brief SEO avant rédaction de contenu

**Cible :** Documentation de processus SEO

**Quoi faire :**
Créer un fichier `brief-seo-template.md` à la racine du projet, structuré en 4 étapes comme enseigné dans la formation Stepizy :

```markdown
# Brief SEO — [Titre du contenu]

## Étape 1 — Angle
- Objectif : Conversion / EEAT / Vente directe ?
- Mot-clé principal : [KW]
- Intention de recherche : Informationnelle / Transactionnelle / Locale

## Étape 2 — Analyse SERP
- Résultats actuels (top 3) : [lires]
- Ce qu'ils ont en commun : [notes]
- Ce qu'on peut ajouter de plus : [valeur ajoutée unique]
- Autorité des concurrents : [faible / moyenne / forte]

## Étape 3 — Plan
- Titre : [titre proposé]
- H1 : [H1]
- H2 : [H2s]
- H3 : [H3s si besoin]
- Éléments uniques : [vidéo, infographie, data, témoignage]

## Étape 4 — Rédaction
- Outil de rédaction : Claude / ChatGPT
- Tonalité : Expert / Pédagogique / Rassurant
- Longueur cible : [~ mots]
- Liens internes à inclure : [pages de conversion]
- Humanisation nécessaire : Oui / Non
```

**Pourquoi :** La formation Stepizy valide que les 4 étapes (angle → SERP → plan → rédaction) sont la méthode qui marche. Formaliser ça en template fiable la qualité et rend le process reproductible.

---

## 🟢 P3 — Bonus / Polish

---

### INSTRUCTION N°24 — 🟢 P3 | Ajouter "Zone d'intervention" enrichie sur index.html

**Fichier :** `index.html`

**Quoi faire :**
Dans la section actuelle (ou à créer), remplacer la simple liste de départements par une présentation enrichie :
- `Une carte mentale des 18 villes avec codes postaux`
- `Liste organisée par département` (Tarn 81 en priorité)
- `Temps d'intervention estimé depuis St-Sulpice` (20min Lavaur, 35min Castres, 40min Albi...)

**Pourquoi :** Google valorise les signaux locaux précis. Lister les villes avec CP et temps d'accès = signal EEAT local fort.

---

## 📊 Suivi d'avancement — v3

| Instruction | Statut | Priorité |
|-------------|--------|----------|
| ❌ **N°20** — Calendrier Google Posts GBP | ⏳ **À faire** | 🟠 P1 |
| ❌ **N°21** — Pages locales top 5 villes | ⏳ **À faire (template + 5 pages)** | 🟠 P1 |
| ❌ **N°22** — Checklist 81 facteurs GBP | ⏳ **À faire** | 🟡 P2 |
| ❌ **N°23** — Template brief SEO | ⏳ **À faire** | 🟡 P2 |
| ❌ **N°24** — Zone intervention enrichie | ⏳ **À faire** | 🟢 P3 |

---

## 📝 Notes de SEO Elekio — 13 juillet 2026

**Analyse de la formation Stepizy :** Formation solide, 9 modules, 47 leçons. Très bonne pour la structure (Mois 1 Corrections), les 81 facteurs GBP, et la méthode de création de pages locales. Complète mes connaissances mais ne révolutionne pas ma stratégie — elle affine et structure ce que j'avais déjà.

**Ce que j'intègre de la formation :**
- ✅ Google Posts 3x/semaine (facteur GBP important)
- ✅ Pages locales avec Perplexity → Gemini → Claude (meilleur pipeline)
- ✅ Brief SEO structuré en 4 étapes (process formalisé)
- ✅ Checklist 81 facteurs GBP (filet de sécurité)
- ✅ Calendrier Mois 1 Corrections (planification)

**Ce que je garde en propre (pas dans la formation) :**
- AI SEO / LLM (être cité dans ChatGPT, Gemini, Perplexity)
- Structured data enrichi pour LLM
- Suivi de positions dans les réponses IA
- Stratégie EEAT adaptée à l'ère IA

*Document généré par SEO Elekio v3 — 13 juillet 2026*

---

# 🏁 RAPPORT D'AUDIT — Relecture du travail Web Creator (13 juillet 2026)

## Méthode
Audit complet des 14 pages HTML + sitemap.xml + robots.txt + llms.txt, effectué le 13/07/2026 par SEO Elekio.

## Résultat général : ✅ 13/14 pages OK

| Vérification | Statut | Détail |
|-------------|--------|--------|
| OG tags (14 pages) | ✅ OK | Toutes les pages ont og:title, og:description, og:url, og:locale, og:type, twitter:card |
| Schema.org | ✅ OK | LocalBusiness + Electrician sur toutes les pages. areaServed correct. |
| Meta descriptions | ✅ OK | Uniques, 150-160 chars, avec CTA |
| Titles | ✅ OK | Uniques, 30-70 chars, mot-clé principal présent |
| Hiérarchie H1/H2/H3 | ✅ OK | Structure propre (sauf mentions-legales) |
| Intégrité (fausses certifs) | ✅ OK | Aucune fausse certification (RGE, QualiPAC, IRVE) |
| Téléphone | ✅ OK | 06 80 50 67 09 présent et cohérent partout |
| Adresse | ✅ OK | 625 route de Saint-Lieux, 81370 Saint-Sulpice-la-Pointe |
| Header/Footer | ✅ OK | Cohérent sur toutes les pages |
| Sitemap | ✅ OK | 14 URLs listées |
| Robots.txt | ✅ OK | Allow: / + Sitemap |
| llms.txt | ✅ OK | Présent (37 lignes, bon pour AI SEO) |
| Pages villes (5) | ⚠️ 71-76% similaire | Sous le seuil critique (85%) mais à améliorer |

## Problèmes identifiés

### ❌ À corriger

1. **mentions-legales.html — Pas de H1**
   - Page entièrement en H3 et H4, aucun H1
   - Simple à corriger : ajouter `<h1>Mentions Légales — Elekio</h1>` avant le premier H3

2. **Pages villes — H2 "Questions fréquentes" identiques sur Castres, Graulhet, Lavaur, Mazamet**
   - Les FAQ sont les mêmes sur 4 pages (71-76% similitude)
   - À enrichir : ajouter des questions spécifiques à chaque ville
   - Exemple pour Castres : "Quel est le prix d'une mise aux normes à Castres ?"

### ⚠️ À surveiller (pas bloquant)

3. **Placeholder formulaire** : `placeholder="06 XX XX XX XX"` — peut donner un signal négatif à Google. Mettre plutôt `placeholder="06 12 34 56 78"` (format sans XX)

## Ce qui est déjà fait vs ce qu'il reste

| État | Pages villes | Statut |
|------|-------------|--------|
| ✅ Déjà fait par Web Creator | electricien-albi.html, castres.html, graulhet.html, lavaur.html, mazamet.html | Pages complètes avec schema.org |
| 📋 À créer (N°21) | toulouse.html, montauban.html, gaillac.html, l-union.html, balma.html, ramonville.html, castanet.html, st-orens.html | 8 nouvelles pages (palier 1 premium) |
| 📋 Palier 2 (plus tard) | castelginest, aucamville, launaguet, fenouillet, rabastens, fronton, villemur, escalquens, verfeil | 10 pages standard |

---

*Rapport d'audit généré par SEO Elekio — 13 juillet 2026*
