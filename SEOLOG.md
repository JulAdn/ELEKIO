# SEOLOG.md — Rapport d'Audit SEO Complet + Plan d'Action
**Date : 07/07/2026**
**Auteur : SEO Elekio (profile seo)**
**Destination : Web Creator (profile web-creator)**

---

## SOMMAIRE
1. [Résumé Exécutif](#1-résumé-exécutif)
2. [Audit 3 axes — Synthèse](#2-audit-3-axes--synthèse)
3. [Réponses aux 6 Questions de Web Creator](#3-réponses-aux-6-questions-de-web-creator)
4. [Instructions P0 — URGENT (avant mise en ligne)](#4-instructions-p0--urgent-avant-mise-en-ligne)
5. [Instructions P1 — IMPORTANT](#5-instructions-p1--important)
6. [Instructions P2 — OPTIMISATION](#6-instructions-p2--optimisation)
7. [Instructions P3 — BONUS (AI SEO)](#7-instructions-p3--bonus-ai-seo)
8. [Track Record des corrections](#8-track-record-des-corrections)

---

## 1. Résumé Exécutif

### Score global : 72/100 — « Solide, quelques corrections avant mise en ligne »

**Ce qui est remarquable : le site évite les pièges classiques** — pas de fausses certifications, pas d'avis inventés, pas d'aggregateRating frauduleux, pas de "nous" pour un artisan seul. Julian peut être fier de l'intégrité du site.

### Top 5 problèmes bloquants (🔴 P0)

| # | Problème | Pages | Sévérité |
|---|----------|-------|----------|
| 1 | **Meta descriptions trop longues (>160 chars)** | index, services, about, contact, realisations | 🔴 Bloque l'affichage optimal dans Google |
| 2 | **Mentions légales incomplètes** | mentions-legales.html | 🔴 Risque juridique (pas de SIRET, TVA, RCS complet) |
| 3 | **Erreur factuelle : DPE ≠ Diagnostic électrique** | faq.html | 🔴 Désinformation — Julian déteste ça |
| 4 | **Pas de H1 sur mentions-legales.html** | mentions-legales.html | 🔴 Structure HTML invalide |
| 5 | **Balise HTML invalide `</h41>`** | electricien-castres.html | 🔴 HTML cassé |

---

## 2. Audit 3 axes — Synthèse

### Axe 1 : Véracité du contenu ✅ Majoritairement sain
- ✅ **Aucune fausse certification** (RGE, QualiPAC, IRVE, etc.)
- ✅ **Aucun avis inventé** — avis.html dit honnêtement « Les avis Google arrivent bientôt »
- ✅ **Pas d'aggregateRating** frauduleux dans le schema.org
- ✅ **Utilisation cohérente du "je"** (pas de "nous" pour un artisan seul)
- ✅ **Pas de CV-style** dans about.html
- ✅ **Services listés = services réellement offerts**
- ❌ **ERREUR FACTUELLE** : FAQ confond DPE et diagnostic électrique (ce sont 2 diagnostics distincts)

### Axe 2 : Design & UX ⚠️ À améliorer
- ❌ **Photo de Julian absente** — placeholder SVG abstrait au lieu de sa photo en hero (inverse du brief)
- ❌ **Hero section = stats/graphiques** alors que Julian veut sa photo
- ❌ **Lien "Avis" manquant** dans la nav de about.html, faq.html, et les 5 pages villes
- ❌ **Contraste insuffisant** cuivre `#c4795b` sur fond blanc (ratio 2.6:1, norme 4.5:1)
- ❌ **Liens villes cassés** — `villes/electricien-albi.html` mais le fichier est `villes_electricien-albi.html`
- ⚠️ **Logo en PNG** pas en SVG comme demandé
- ⚠️ **CSS dupliqué** ~250 lignes × 13 pages

### Axe 3 : Technique & SEO ⚠️ Correct mais à peaufiner
- ✅ **Tous les `<title>` uniques et optimisés** (33-69 chars)
- ✅ **Canoniques self-référençantes** sur toutes les pages
- ✅ **Schema.org LocalBusiness + Electrician** présent, données cohérentes
- ✅ **FAQPage schema** avec 8 Q&A
- ✅ **llms.txt complet** ✅
- ❌ **5 meta descriptions > 160 chars** (index=165, services=163, about=164, contact=164, realisations=165)
- ❌ **Pas de H1** sur mentions-legales.html
- ❌ **URLs schema.org incohérentes** (`/a-propos/` au lieu de `/about.html`, etc.)
- ❌ **merci.html dans sitemap** mais fichier inexistant → 404
- ❌ **Meta robots absent** sur toutes les pages
- ⚠️ **Pages villes : contenu quasi identique** — risque de duplicate content
- ⚠️ **BreadcrumbList absent** sur index, faq, mentions, city pages

---

## 3. Réponses aux 6 Questions de Web Creator

### QUESTION 1 — Top 3 points prioritaires avant mise en ligne ?

**1. 🔴 Corriger les meta descriptions trop longues** 
Les 5 pages principales (index, services, about, contact, realisations) ont des meta descriptions > 160 chars. Google les tronquera dans les SERP.
→ Réduire chaque meta desc à 150-158 chars max.

**2. 🔴 Compléter les mentions légales**
Ajouter obligatoirement : SIRET/SIREN, numéro TVA intracommunautaire, RCS complet (avec numéro), assurance RC pro et garantie décennale (numéro et assureur).

**3. 🔴 Corriger l'erreur DPE/Diagnostic Électrique dans la FAQ**
La ligne « Le diagnostic électrique obligatoire (officiellement DPE — Diagnostic de Performance Énergétique...) » est FAUSSE. Le DPE et l'état de l'installation intérieure d'électricité sont deux diagnostics distincts.

**Bonus : Ajouter un H1 sur mentions-legales.html** — c'est une page sans titre principal.

### QUESTION 2 — Pages villes supplémentaires ?

**Oui, mais PAS maintenant.** Tu as déjà 5 pages villes (Albi, Castres, Graulhet, Lavaur, Mazamet). C'est suffisant pour commencer.

**Problème prioritaire** : Ces 5 pages ont un contenu quasi identique (même HTML à 95%). Google les verra comme du duplicate content. **Corrige d'abord le contenu unique**, puis ajoute des villes.

**Comment rendre chaque page ville unique :**
1. **H2 spécifique** : parler d'un quartier emblématique par ville
   - Albi → « La Cité épiscopale classée UNESCO »
   - Castres → « Le centre-ville avec ses maisons aux bords de l'Agout »
   - Graulhet → « La cité du cuir et son patrimoine industriel »
   - Lavaur → « La cathédrale Saint-Alain et le cœur historique »
   - Mazamet → « La ville aux portes de la Montagne Noire »
2. **Ajouter une section « Mon expérience à [Ville] »** — 2-3 phrases authentiques de Julian
3. **Distances/temps de trajet réels** depuis Saint-Sulpice
4. **Types de logements courants** (maisons anciennes à Albi, résidences récentes à Castres, etc.)
5. **Schéma LocalBusiness unique par ville** — avec `@id` différent

**Pour les villes restantes (Toulouse, Lavaur, Gaillac, etc.) :** Ajoute-les quand les 5 premières seront uniques et indexées.

### QUESTION 3 — Configuration Google Search Console & GA4

**Google Search Console :**
1. Crée une propriété de type « Préfixe d'URL » avec `https://elekio.pages.dev`
2. Ajoute une deuxième propriété pour `https://www.elekio.fr` (pour plus tard)
3. **Méthode de vérification** Cloudflare Pages :
   - Option A (recommandée) : Ajoute un enregistrement TXT DNS sur le domaine elekio.fr
   - Option B (plus simple) : Télécharge le fichier HTML de vérification Google et dépose-le à la racine du projet GitHub (JulAdn/ELEKIO)
   - Option C : Utilise la méta-balise de vérification dans le `<head>` de index.html
4. Soumets sitemap.xml une fois la propriété vérifiée

**Google Analytics 4 :**
1. Crée une propriété GA4 dans Google Analytics
2. Récupère le « Measurement ID » (format : G-XXXXXXXXXX)
3. Ajoute le script GA4 dans le `<head>` de chaque page HTML
4. Alternative plus légère : utilise **Plausible Analytics** ou **Umami** (hébergement plus respectueux des données)

Pour le site statique Cloudflare Pages, tu peux :
- Ajouter les scripts directement dans les fichiers HTML
- OU utiliser Cloudflare Web Analytics (gratuit, pas de cookie banner nécessaire)

### QUESTION 4 — Prêt pour mise en ligne avec elekio.fr ?

**Pas encore. Corrige d'abord les P0 ci-dessus.**

**Checklist avant mise en ligne :**
- [ ] Domaine elekio.fr pointé vers Cloudflare Pages (DNS + SSL auto via Cloudflare)
- [ ] Meta descriptions corrigées (< 160 chars)
- [ ] Mentions légales complètes (SIRET, TVA, RCS, assurance)
- [ ] Erreur DPE corrigée dans FAQ
- [ ] H1 ajouté sur mentions-legales.html
- [ ] Balise `</h41>` corrigée sur castres
- [ ] SSL : Cloudflare fournit le SSL automatiquement ✅ (aucune action nécessaire)
- [ ] Redirection 301 de elekio.pages.dev vers elekio.fr
- [ ] Search Console configurée AVANT le changement de domaine
- [ ] Sitemap.xml : mettre à jour les URLs avec le bon domaine

**Ne pas oublier de mettre à jour :**
- robots.txt : changer `Sitemap: https://www.elekio.fr/sitemap.xml` → fonctionnera après déploiement
- llms.txt : vérifier que les URLs pointent vers le bon domaine
- Tous les OG tags og:url

### QUESTION 5 — Meta descriptions trop longues

**Solution par page :**

| Page | Actuelle (chars) | Proposition corrigée |
|------|-----------------|---------------------|
| index.html | 165 | `Électricien Tarn 81 — Saint-Sulpice. Dépannage urgence 4h, installation neuve, rénovation aux normes. Devis gratuit 24h. Garantie décennale. 06 80 50 67 09` (155) |
| services.html | 163 | `Électricien Tarn (81) : dépannage urgence 4h, installation neuve, rénovation aux normes. Devis gratuit 24h. Intervention Tarn et départements limitrophes.` (155) |
| about.html | 164 | `Elekio — électricien à Saint-Sulpice-la-Pointe (81). Dépannage, installation, rénovation dans le Tarn. Devis gratuit 24h. Faites confiance à un vrai pro.` (157) |
| contact.html | 164 | `Contactez Elekio, électricien à Saint-Sulpice (81370). Devis gratuit sous 24h, dépannage urgence 4h. Tél : 06 80 50 67 09. Intervention Tarn 81.` (154) |
| realisations.html | 165 | `Tarifs électricien dans le Tarn 81 : installation neuve dès 4000€, rénovation dès 3000€, dépannage 80€. Devis gratuit sous 24h à Saint-Sulpice.` (158) |

### QUESTION 6 — Photo, H1, liens Facebook/LinkedIn, etc.

**Photo de Julian :** En attente que Julian fournisse une vraie photo. En attendant, remplace le SVG placeholder par un **icône ou illustration plus professionnelle** (pas un cercle+ellipse basique). La section hero devrait être repensée pour mettre la photo en avant (quand elle sera disponible).

**H1 manquants :** Ajouter `<h1>Mentions Légales — Elekio</h1>` sur mentions-legales.html (après la balise `<main>`).

**Liens Facebook/LinkedIn morts :** Correct de laisser `href="#"` avec libellé « à venir » — c'est honnête. Mais ajoute un `aria-label` approprié et éventuellement désactive le lien CSS (`pointer-events: none`).

---

## 4. Instructions P0 — URGENT (avant mise en ligne)

### I1 — P0 | Réduire les meta descriptions à ≤ 158 chars

| Page | Meta description corrigée |
|------|--------------------------|
| index.html | `Électricien Tarn 81 — Saint-Sulpice. Dépannage urgence 4h, installation neuve, rénovation aux normes. Devis gratuit 24h. Garantie décennale. 06 80 50 67 09` |
| services.html | `Électricien Tarn (81) : dépannage urgence 4h, installation neuve, rénovation aux normes. Devis gratuit 24h. Intervention Tarn et départements limitrophes.` |
| about.html | `Elekio — électricien à Saint-Sulpice-la-Pointe (81). Dépannage, installation, rénovation dans le Tarn. Devis gratuit 24h. Faites confiance à un vrai pro.` |
| contact.html | `Contactez Elekio, électricien à Saint-Sulpice (81370). Devis gratuit sous 24h, dépannage urgence 4h. Tél : 06 80 50 67 09. Intervention Tarn 81.` |
| realisations.html | `Tarifs électricien dans le Tarn 81 : installation neuve dès 4000€, rénovation dès 3000€, dépannage 80€. Devis gratuit sous 24h à Saint-Sulpice.` |

### I2 — P0 | Compléter les mentions légales

Ajouter DANS mentions-legales.html (après l'adresse ou dans une section dédiée) :
- SIRET / SIREN (à demander à Julian)
- Numéro TVA intracommunautaire (FR + SIREN)
- RCS complet : RCS Castres XXX XXX XXX
- Assurance RC Pro : nom de l'assureur + numéro de contrat
- Garantie décennale : nom de l'assureur + numéro de contrat
- Capital social de l'EURL (montant exact)

### I3 — P0 | Corriger l'erreur DPE dans FAQ

Dans faq.html, remplacer :
`"Le diagnostic électrique obligatoire (officiellement DPE — Diagnostic de Performance Énergétique partie électrique, ou état de l'installation intérieure d'électricité)"`

Par :
`"Le diagnostic électrique obligatoire, officiellement appelé état de l'installation intérieure d'électricité (à ne pas confondre avec le DPE — Diagnostic de Performance Énergétique — qui concerne l'énergie). Ce diagnostic vérifie la conformité et la sécurité de votre installation électrique."`

### I4 — P0 | Ajouter H1 sur mentions-legales.html

Après `<main>`, ajouter : `<h1>Mentions Légales — Elekio</h1>`

### I5 — P0 | Corriger balise HTML invalide `</h41>` dans electricien-castres.html

Remplacer `</h41>` par `</h3>` (ligne ~312)

### I6 — P0 | Supprimer merci.html du sitemap.xml (page inexistante)

---

## 5. Instructions P1 — IMPORTANT

### I7 — P1 | Unifier la navigation « Avis » sur toutes les pages

Ajouter le lien `avis.html` dans la nav de :
- about.html (entre FAQ et Contact)
- faq.html (entre FAQ et Contact)
- Les 5 pages villes

### I8 — P1 | Ajouter BreadcrumbList à toutes les pages manquantes

Ajouter schema.org BreadcrumbList sur :
- index.html
- faq.html
- mentions-legales.html
- Les 5 pages villes (electricien-*.html)

### I9 — P1 | Ajouter meta robots sur toutes les pages

Dans le `<head>` de chaque page : `<meta name="robots" content="index, follow">`

### I10 — P1 | Corriger les URLs incohérentes dans le schema.org

Dans les JSON-LD de :
- about.html : `"@id": "https://elekio.pages.dev/about.html"` (au lieu de `/a-propos/`)
- contact.html : `"@id": "https://elekio.pages.dev/contact.html"` (au lieu de `/contact/`)
- realisations.html : `"@id": "https://elekio.pages.dev/realisations.html"`

### I11 — P1 | Différencier le contenu des 5 pages villes

Ajouter un paragraphe unique par ville :
- Albi → parler de la Cité épiscopale, des maisons en brique rouge, des quartiers Madeleine, Cantepau
- Castres → les bords de l'Agout, le centre-ville avec ses maisons à colombages, quartier Albinque
- Graulhet → la cité du cuir, le patrimoine industriel, quartiers périphériques résidentiels
- Lavaur → la cathédrale Saint-Alain, le cœur historique, les nouveaux lotissements
- Mazamet → la ville aux portes de la Montagne Noire, maisons de caractère, résidences récentes

### I12 — P1 | Corriger le lien « Politique de confidentialité » dans contact.html

Soit créer la page, soit faire pointer vers mentions-legales.html (avec ancre ou sous-section RGPD)

---

## 6. Instructions P2 — OPTIMISATION

### I13 — P2 | Ajouter des @id uniques par page ville dans le schema.org

Chaque schema LocalBusiness des pages villes devrait avoir un `@id` unique, ex :
```json
"@id": "https://elekio.pages.dev/villes/electricien-albi.html#LocalBusiness",
"@id": "https://elekio.pages.dev/villes/electricien-castres.html#LocalBusiness"
```

### I14 — P2 | Remplacer le SVG placeholder de Julian par une vraie photo (quand disponible)

Repenser la section hero pour mettre la photo en premier plan, déplacer les stats en dessous ou sur le côté.

### I15 — P2 | Externaliser le CSS en fichier .css dédié

Créer `style.css` et remplacer les ~250 lignes de CSS inline par un `<link rel="stylesheet" href="style.css">` dans chaque page. Gain : ~250KB de bande passante économisés par chargement de page, maintenance plus simple.

### I16 — P2 | Ajouter le dark mode aux pages qui en manquent

Pages concernées : services.html, contact.html, realisations.html, about.html, mentions-legales.html, 5 villes

### I17 — P2 | Améliorer les alt text des images

Remplacer `alt="Elekio"` (trop générique) par `alt="Elekio — Électricien Tarn 81"` (logo header) et des alt descriptifs pour les autres images.

---

## 7. Instructions P3 — BONUS (AI SEO)

### I18 — P3 | Optimiser le contenu pour les LLM (AI Overviews)

1. Ajouter des **définitions claires** pour chaque service dans services.html (format question → réponse courte → détail)
2. Dans la FAQ, structurer les réponses avec des listes à puces pour améliorer l'extraction par les LLM
3. Ajouter une section « Pourquoi me choisir ? » avec des arguments concis (idéal pour Google AI Overviews)

### I19 — P3 | Ajouter un blog ou des articles de fond

- 1 article / mois sur des sujets : « Norme NF C 15-100 : ce qui change », « Diagnostic électrique : ce qu'il faut savoir avant de vendre », etc.
- Format : 800-1200 mots, questions-réponses, liste de contrôle
- Ces articles seront la base pour les citations par ChatGPT/Perplexity

### I20 — P3 | Ajouter un avis Google → Lier le vrai profil GBP

Quand Julian aura des avis Google, les intégrer avec le bon schema.org Review

---

## 8. Track Record des corrections

| Instruction | Statut | Date | Notes |
|-------------|--------|------|-------|
| I1 — Meta desc | ⬜ TODO | | 5 pages à corriger |
| I2 — Mentions légales | ⬜ TODO | | Demander SIRET/TVA à Julian |
| I3 — Erreur DPE | ⬜ TODO | | FAQ ligne 64 |
| I4 — H1 mentions | ⬜ TODO | | Après `<main>` |
| I5 — `</h41>` | ⬜ TODO | | castres.html ligne 312 |
| I6 — Sitemap merci.html | ⬜ TODO | | Supprimer l'URL |
| I7 — Nav Avis | ⬜ TODO | | 7 pages à modifier |
| I8 — BreadcrumbList | ⬜ TODO | | 8 pages |
| I9 — Meta robots | ⬜ TODO | | Toutes pages |
| I10 — URLs schema | ⬜ TODO | | about, contact, realisations |
| I11 — Contenu villes | ⬜ TODO | | 5 pages |
| I12 — Politique confidentialité | ⬜ TODO | | contact.html |
| I13 — @id schema villes | ⬜ TODO | | |
| I14 — Photo Julian | ⬜ TODO | | En attente de Julian |
| I15 — CSS externalisé | ⬜ TODO | | |
| I16 — Dark mode | ⬜ TODO | | 11 pages |
| I17 — Alt text | ⬜ TODO | | |
| I18 — Contenu LLM | ⬜ TODO | | |
| I19 — Blog | ⬜ TODO | | |
| I20 — Avis Google | ⬜ TODO | | |
