# RAPPORT DE DIAGNOSTIC — SITE ELEKIO

**Date :** 7 juillet 2026  
**Audité par :** Hermes Agent — Audit automatisé complet  
**Cible :** /workspace/1_Projects/site-web/ (14 pages HTML + 6 pages villes)  
**Charte :** #000c42 (Bleu nuit) + #c4795b (Cuivre)

---

## SOMMAIRE

1. [Résumé exécutif](#1-résumé-exécutif)
2. [Ce qui fonctionne](#2-ce-qui-fonctionne)
3. [Problèmes critiques](#3-problèmes-critiques)
4. [Problèmes design — Header/Footer](#4-problèmes-design--headerfooter)
5. [Problèmes navigation & liens](#5-problèmes-navigation--liens)
6. [Problèmes SEO & données structurées](#6-problèmes-seo--données-structurées)
7. [Problèmes contenu & tarifs](#7-problèmes-contenu--tarifs)
8. [Problèmes formulaires & fonctionnalités](#8-problèmes-formulaires--fonctionnalités)
9. [Problèmes fichiers & assets](#9-problèmes-fichiers--assets)
10. [Corrections immédiates](#10-corrections-immédiates)
11. [Améliorations recommandées](#11-améliorations-recommandées)
12. [Checklist par page](#12-checklist-par-page)

---

## 1. RÉSUMÉ EXÉCUTIF

| Catégorie | État |
|---|---|
| ✅ Contenu éditorial | **Bien** — texte cohérent, ton professionnel, pas de fautes majeures |
| ❌ Design (CSS) | **GRAVE** — style.css externe complètement déconnecté du rendu réel |
| ❌ Header | **DÉFAILLANT** — 3 versions différentes coexistent |
| ❌ Footer | **DÉFAILLANT** — HTML cassé dans faq.html, texte incohérent entre pages |
| ⚠️ SEO (Schema.org) | **INCOMPLET** — `#website` jamais défini, URLs schema erronées |
| ⚠️ SEO (Sitemap) | **OK** — mais manque avis.html après merci.html |
| ⚠️ SEO (OG) | **OK** — toutes les pages ont des balises OG valides |
| ⚠️ Navigation | **PROBLÈMES** — avis.html manque le lien "Avis", about.html aussi |
| ✅ Tarifs (prix) | **Cohérents** entre services.html et realisations.html |
| ❌ Formulaire | spam protection minimum (`_captcha=false`) |
| ⚠️ Tarn → Occitanie | **MIXTE** — certaines pages utilisent Occitanie, d'autres Tarn |
| ❌ Images manquantes | Aucune photo réelle (avatars SVG uniquement) |

**Score global : 6/10** — Site fonctionnel mais avec des incohérences design majeures, du HTML cassé, et des données structurées incomplètes.

---

## 2. CE QUI FONCTIONNE

### Contenu
- ✅ Ton cohérent et professionnel sur toutes les pages
- ✅ Pas de fautes d'orthographe visibles
- ✅ Message clair : intervention 4h, devis gratuit 24h, garantie décennale
- ✅ Prix cohérents entre services.html et realisations.html
- ✅ Informations de contact cohérentes (tel, email, adresse)

### SEO de base
- ✅ Balises `lang="fr"` sur toutes les pages
- ✅ `viewport` avec `viewport-fit=cover` — bonne pratique mobile
- ✅ `canonical` URLs présentes sur toutes les pages
- ✅ `og:title`, `og:description`, `og:url`, `og:type`, `og:locale`, `og:image` présentes
- ✅ `twitter:card` présent sur toutes les pages
- ✅ `robots.txt` valide avec sitemap
- ✅ `sitemap.xml` présent et bien structuré

### Fonctionnalités
- ✅ Menu mobile responsive (hamburger toggle) — fonctionne sur toutes les pages
- ✅ Mobile sticky bar (call + devis) — présente partout
- ✅ Accordéon FAQ fonctionnel (toggleFaq avec animation)
- ✅ Formulaire contact avec FormSubmit.co + honeypot anti-spam
- ✅ Animations IntersectionObserver (fade-up)

### Design général
- ✅ Palette cohérente (navy + copper) sur tout le site
- ✅ Typographie propre (system-ui stack)
- ✅ Responsive (breakpoints 1024px, 900px, 768px, 480px)
- ✅ Dark mode (index.html et avis.html)

---

## 3. PROBLÈMES CRITIQUES

### 🔴 CRITIQUE 1 : style.css externe complètement déconnecté du rendu réel

Le fichier `/workspace/1_Projects/site-web/style.css` est un fichier *externe* qui n'est **lié par aucune page HTML**. Aucune page ne fait `<link rel="stylesheet" href="style.css">`. Toutes les pages embarquent leur propre copie *inline* du CSS.

**Pire :** le style.css externe a des règles **totalement différentes** du code inline :

| Propriété | style.css (externe, inutilisé) | Code inline (réel) |
|---|---|---|
| `.header` background | `rgba(0,12,66,.97); backdrop-filter:blur(12px)` | `linear-gradient(100deg,#fff 27%,#c4795b 27.5%,...)` |
| `.logo` color | `#fff` | `var(--navy)` (#000c42) |
| `.footer` background | `var(--navy)` (bleu foncé) | `#fff` (blanc) |
| `.footer` text color | `rgba(255,255,255,.7)` | `var(--gray-600)` |
| `.footer-bottom p` color | `rgba(255,255,255,.4)` | `var(--gray-400)` |
| `.footer-socials a` background | `rgba(255,255,255,.06)` | `var(--bg-cream)` |
| `.mobile-sticky` background | `var(--navy)` | `#fff` |
| `.mobile-sticky .ms-call` color | `#fff` | `var(--navy)` |
| `.menu-toggle` margin-left | *(absent)* | `margin-left:auto` (sur certaines pages) |

**Impact :** Si quelqu'un tente d'ajouter un `<link>` vers style.css, le design sera complètement cassé.

### 🔴 CRITIQUE 2 : HTML cassé dans le footer de faq.html (lignes 591-604)

```html
<ul>
  <li><a href="index.html">Accueil</a></li>
  <li><a href="services.html">Services</a></li>
  <li><a href="realisations.html">Tarifs & Devis</a></li>
  <a href="faq.html">FAQ</a>                    ← balise <a> orpheline
  <a href="avis.html">Avis</a>                  ← balise <a> orpheline
  <a href="about.html">                          ← balise <a> non fermée
  <a href="avis.html">Avis</a></li>              ← doublon
  <li><a href="about.html">À propos</a></li>
  ...
</ul>
```

**Résultat :** Le footer de la FAQ est visuellement cassé — les liens FAQ, Avis, À propos sont mal imbriqués.

### 🔴 CRITIQUE 3 : Navigation manquante sur avis.html et about.html

**avis.html (lignes 264-271) — lien "Avis" absent de la nav :**
```
Accueil | Services | Tarifs | FAQ | À propos | Devis gratuit | 📞
```
→ Pas de lien vers `avis.html` (pourtant la page active est "Avis")

**about.html (lignes 263-269) — même problème :**
```
Accueil | Services | Tarifs | FAQ | À propos (active) | Devis gratuit | 📞
```
→ Pas de lien vers `avis.html`

**Toutes les autres pages ont** `Avis` dans la nav.

---

## 4. PROBLÈMES DESIGN — HEADER/FOOTER

### 4.1 Header — trois versions différentes

| Version | Pages concernées |
|---|---|
| **V1 :** `linear-gradient(100deg,#fff 27%,#c4795b 27.5%,#fff 27.5%,#fff 28%,#000c42 28.7%,#fff 28.7%,#fff 30%,#000c42 30.2%)` | index.html, services.html, about.html, contact.html, faq.html, realisations.html, mentions-legales.html, merci.html |
| **V2 :** Même gradient mais `justify-content:flex-start;max-width:100%` | avis.html (lignes 103-104), merci.html (lignes 79-80) |
| **V3 (inutilisée) :** `rgba(0,12,66,.97);backdrop-filter:blur(12px)` | style.css externe |

Les pages avis.html et merci.html ont un header différent avec `justify-content:flex-start` et `max-width:100%` au lieu de `justify-content:space-between` — le logo et la nav sont alignés à gauche au lieu d'être espacés.

### 4.2 Header — pas de logo `height` en mobile pour avis.html

Dans le responsive mobile @768px, certaines pages ont `height:45px!important` pour le logo (index.html, avis.html), mais d'autres non.

### 4.3 Header — margin-left du menu toggle

Sur avis.html et index.html, le `.menu-toggle` a `margin-left:auto`. Sur les autres pages, cette propriété est absente. Cela peut causer un alignement différent du bouton hamburger.

### 4.4 Footer — texte incohérent entre pages

| Page | Texte footer brand |
|---|---|
| index.html | "Intervention dans tout le **Tarn** et départements limitrophes" |
| services.html | "Intervention en **Occitanie** et départements limitrophes" |
| about.html | "Intervention en **Occitanie** et départements limitrophes" |
| contact.html | "Intervention dans tout le **Tarn** et départements limitrophes" |
| faq.html | "Intervention dans tout le **Tarn** et départements limitrophes" |
| realisations.html | "Intervention en **Occitanie** et départements limitrophes" |
| avis.html | "Intervention en **Occitanie** et départements limitrophes" |
| merci.html | "Intervention en **Occitanie** et départements limitrophes" |
| mentions-legales.html | "Intervention en **Occitanie** et départements limitrophes" |

**Problème :** 3 pages disent "Tarn", 6 pages disent "Occitanie". Incohérence totale.

### 4.5 Dark mode — pas sur toutes les pages

Seules **index.html** et **avis.html** ont des règles `@media(prefers-color-scheme:dark)`. Les autres pages (services, about, contact, faq, realisations, merci, mentions-legales, et les 6 pages villes) **n'ont PAS de dark mode**.

### 4.6 Theme-color — incohérent

- **index.html** : `theme-color` avec `media="(prefers-color-scheme:light)"` ET `media="(prefers-color-scheme:dark)"` ✓
- **avis.html** : idem ✓
- **Toutes les autres pages** : un seul `theme-color` sans media query ⚠️

---

## 5. PROBLÈMES NAVIGATION & LIENS

### 5.1 Liens de navigation

| Lien | Présent partout ? |
|---|---|
| Accueil → index.html | ✅ Oui |
| Services → services.html | ✅ Oui |
| Tarifs → realisations.html | ✅ Oui |
| FAQ → faq.html | ✅ Oui |
| Avis → avis.html | ❌ **Manquant** sur avis.html, about.html |
| À propos → about.html | ✅ Oui |
| Devis gratuit → contact.html | ✅ Oui |
| 📞 → tel:0680506709 | ✅ Oui |

### 5.2 Liens réseaux sociaux (footer)

| Réseau | Lien | Statut |
|---|---|---|
| Facebook | `href="#"` | ❌ **Lien mort** — pointe vers `#` |
| Instagram | `https://www.instagram.com/elekio_electricite/` | ✅ Valide |
| LinkedIn | `href="#"` | ❌ **Lien mort** — pointe vers `#` |

Les liens Facebook et LinkedIn sont des placeholders morts. Mieux vaudrait ne pas les afficher ou les commenter.

### 5.3 Liens "Politique de confidentialité" (contact.html)

```html
<a href="#" style="color:var(--copper);text-decoration:underline">Politique de confidentialité</a>
```

❌ **Lien mort** — pointe vers `#`. Aucune page de politique de confidentialité n'existe.

### 5.4 Liens ville — certaines pages pointe vers `#`

Dans **services.html** (lignes 555-559) :
```html
<a href="#" class="zone-dep"><span class="dep-num">81</span> Saint-Sulpice-la-Pointe</a>
<a href="#" class="zone-dep"><span class="dep-num">31</span> Toulouse</a>
<a href="#" class="zone-dep"><span class="dep-num">82</span> Montauban</a>
<a href="#" class="zone-dep"><span class="dep-num">12</span> Villefranche</a>
<a href="#" class="zone-dep"><span class="dep-num">34</span> Béziers</a>
```

Ces 5 liens pointent vers `#` — ils devraient pointer vers des pages villes dédiées ou être des `<span>`.

### 5.5 Gaillac (index.html), Saint-Sulpice, Rabastens, Carmaux, Toulouse, Montauban, Revel

Dans index.html, ces villes sont des `<span>` (pas de lien), ce qui est cohérent car seules les 5 villes avec pages existantes (Albi, Castres, Graulhet, Lavaur, Mazamet) ont des liens. C'est correct.

---

## 6. PROBLÈMES SEO & DONNÉES STRUCTURÉES

### 6.1 `#website` jamais défini (CRITIQUE)

Toutes les pages utilisent `"isPartOf":{"@id":"https://www.elekio.fr/#website"}` dans leurs données structurées, **mais aucune page ne définit** l'entité `#website`. Le schema suivant est manquant :

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://www.elekio.fr/#website",
  "url": "https://www.elekio.fr",
  "name": "Elekio — Électricien Tarn (81)",
  "description": "...",
  "inLanguage": "fr-FR",
  "publisher": {"@id": "https://www.elekio.fr/#organization"}
}
```

**Impact SEO :** Google comprend mal la hiérarchie des pages. L'organisation n'est pas correctement reliée au site.

### 6.2 URLs Schema erronées — about.html

Dans about.html, le schema utilise :
- `@id:"https://www.elekio.fr/a-propos/#aboutpage"` — mais l'URL réelle est `about.html`
- `@id:"https://www.elekio.fr/a-propos/#person"` — idem
- `@id:"https://www.elekio.fr/a-propos/#breadcrumb"` — idem
- `url:"https://www.elekio.fr/a-propos/"` — devrait être `about.html`

### 6.3 URLs Schema erronées — contact.html

- `@id:"https://www.elekio.fr/contact/#contactpage"` — mais l'URL réelle est `contact.html`
- `@id:"https://www.elekio.fr/contact/#breadcrumb"` — idem
- `url:"https://www.elekio.fr/contact/"` — devrait être `contact.html`

### 6.4 Sitemap — avis.html avant merci.html

Dans sitemap.xml, la page avis.html apparaît **après** merci.html, mais logiquement avis.html devrait être avant (priorité 0.8 vs 0.2). Ce n'est pas bloquant mais inhabituel.

### 6.5 Balises meta description — longueurs

Toutes les meta descriptions font entre 120-160 caractères — correct.

### 6.6 Pas de balises `<h2>` manquantes

Structure des titres correcte : chaque section a un `h2`.

### 6.7 Avis.html — pas de AggregateRating schema

La page d'avis n'a pas de schema `AggregateRating` pour la note moyenne. Idéal pour le SEO local.

---

## 7. PROBLÈMES CONTENU & TARIFS

### 7.1 Tarn → Occitanie (migration inachevée)

**Pages qui disent encore "Tarn" pour la zone d'intervention (hors mentions administratives légitimes) :**

| Page | Texte concerné |
|---|---|
| index.html (footer) | "Intervention dans tout le **Tarn** et départements limitrophes" |
| contact.html (footer) | "Intervention dans tout le **Tarn** et départements limitrophes" |
| faq.html (footer) | "Intervention dans tout le **Tarn** et départements limitrophes" |
| index.html (zone-cta) | "🚗 Je me déplace dans 5 départements" → OK, pas de Tarn |
| index.html (section-title) | "Électricien de proximité dans tout le **Tarn** et au-delà" |

Les mentions "Tarn" comme département (81) sont légitimes et doivent rester. Les mentions "dans le Tarn" en zone d'intervention doivent être changées en "en Occitanie" sauf quand il s'agit d'une limite administrative.

### 7.2 Tarifs — incohérences mineures

| Service | services.html | realisations.html | Différence |
|---|---|---|---|
| Dépannage | "80€ + 50€/h" | "80€ + 50€/h" | ✅ OK |
| Installation 100m² | "4 000€ HT" | "4 000€" | ⚠️ HT manquant |
| Rénovation 80m² | "3 000€ HT" | "3 000€" | ⚠️ HT manquant |
| Tableau | "600€ HT" | "600€" | ⚠️ HT manquant |
| DPE | "150€ HT" | "150€" | ⚠️ HT manquant |
| Petits travaux | "80€" | "Sur devis" | ✅ OK (cohérent, pas de prix fixe) |

**Recommandation :** Ajouter "HT" sur realisations.html ou retirer "HT" partout pour harmoniser.

### 7.3 "DPE" abusif — page services.html

Dans la FAQ (Q5), l'auteur écrit : "Le diagnostic électrique obligatoire (officiellement DPE — Diagnostic de Performance Énergétique partie électrique...)" — **c'est faux**. Le DPE (Diagnostic de Performance Énergétique) et le diagnostic électrique (État de l'Installation Intérieure d'Électricité) sont **deux diagnostics distincts** régis par des textes différents. Les confondre est une erreur éditoriale.

### 7.4 "Loi Carrez" inapproprié

Dans services.html (ligne 458) : "État installation intérieure (loi Carrez)" — la loi Carrez concerne **les surfaces**, pas l'électricité. Cette mention est incorrecte.

### 7.5 Mentions légales — hébergement erroné

mentions-legales.html indique : "Ce site est hébergé par **OVH**". Selon le contexte, le site est déployé sur **Cloudflare Pages**. L'hébergeur mentionné est incorrect.

---

## 8. PROBLÈMES FORMULAIRES & FONCTIONNALITÉS

### 8.1 Formulaire contact — spam protection minimale

```html
<input type="hidden" name="_captcha" value="false">
```

`_captcha=false` désactive le captcha de FormSubmit. Le honeypot (`_honey`) est présent mais ne suffit pas contre les bots agressifs.

**Risque :** Spam important si le site reçoit du trafic.

### 8.2 Formulaire — pas de redirection explicite vers merci.html

Le formulaire n'a pas de champ `_next` pour rediriger vers `merci.html`. FormSubmit utilise probablement la redirection par défaut (page blanche "Thank you"). 

**Correction possible :** Ajouter `<input type="hidden" name="_next" value="https://www.elekio.fr/merci.html">`

### 8.3 Accordéon FAQ — pas d'état initial ouvert

Tous les items FAQ commencent fermés. C'est bien — bonne pratique UX.

### 8.4 Pas de JavaScript externe — tout est inline

Tout le JS est en inline. C'est OK pour Cloudflare Pages, mais pas idéal pour le caching.

---

## 9. PROBLÈMES FICHIERS & ASSETS

### 9.1 Fichier inutilisé

- **style.css** (196 lignes) — n'est lié par aucune page HTML ❌

### 9.2 Images

| Fichier | Statut |
|---|---|
| favicon.png | ✅ Présent |
| apple-touch-icon.png | ✅ Présent |
| logo-elekio.png | ✅ Présent |
| logo-elekio-header.png | ✅ Présent |
| Photos réelles (Julian, chantiers) | ❌ **Absentes** — seuls des SVG placeholders |

### 9.3 6 pages villes

- electricien-albi.html ✅
- electricien-castres.html ✅
- electricien-graulhet.html ✅
- electricien-lavaur.html ✅
- electricien-mazamet.html ✅

Toutes ont la même structure, des metas OG, schema.org LocalBusiness. **Attention :** elles n'ont pas de dark mode.

---

## 10. CORRECTIONS IMMÉDIATES

Par ordre de priorité :

### 🔴 P1 — HTML cassé
1. **faq.html footer** (lignes 593-604) : Réécrire le bloc navigation footer avec des `<li>` corrects
2. **avis.html navigation** : Ajouter le lien "Avis" manquant dans la nav
3. **about.html navigation** : Ajouter le lien "Avis" manquant dans la nav

### 🔴 P2 — Header & footer incohérents
4. **Unifier le header** sur toutes les pages (même `justify-content`)
5. **Unifier le texte du footer brand** : remplacer "Tarn" par "Occitanie" sur index.html, contact.html, faq.html
6. **ajouter dark mode** sur services.html, about.html, contact.html, faq.html, realisations.html, merci.html, mentions-legales.html + les 6 pages villes

### 🔴 P3 — SEO
7. **Ajouter `#website` schema.org** sur index.html (ou toutes les pages)
8. **Corriger les URLs Schema** de about.html (`/a-propos/` → `about.html`)
9. **Corriger les URLs Schema** de contact.html (`/contact/` → `contact.html`)
10. **Corriger l'hébergement** dans mentions-legales.html (OVH → Cloudflare)

### ⚠️ P4 — Liens morts
11. **Remplacer les liens Facebook/LinkedIn `#`** — soit mettre les vrais URLs, soit retirer les icônes
12. **Remplacer le lien "Politique de confidentialité" `#`** — créer la page ou retirer le lien
13. **Remplacer les 5 liens `#` dans services.html** — créer les pages villes ou utiliser des `<span>`

### ⚠️ P5 — Contenu
14. **Corriger "DPE"** dans la FAQ — ne pas confondre avec le diagnostic électrique
15. **Corriger "loi Carrez"** dans services.html (ligne 458)
16. **Ajouter HT** sur realisations.html ou retirer HT sur services.html pour harmoniser
17. **Ajouter `_next`** au formulaire contact pour rediriger vers merci.html

---

## 11. AMÉLIORATIONS RECOMMANDÉES

### Design & UX
- ⭐ Ajouter de **vraies photos** (portrait Julian + photos de chantiers)
- ⭐ Ajouter un **widget Google Reviews** fonctionnel (Place ID déjà trouvé: `/g/11zcnc3dny`)
- ⭐ Ajouter des **animations de compteurs** pour les stats (24h, 4h)
- ⭐ Ajouter une **carte interactive** (OpenStreetMap/Leaflet) pour la zone d'intervention
- ⭐ Ajouter un **bouton "scroll to top"** pour les longs articles

### SEO avancé
- ⭐ Ajouter `Product` schema pour les services avec prix
- ⭐ Ajouter `AggregateRating` schema sur avis.html
- ⭐ Ajouter des **balises `<h2>` de service** dans les contenus pour améliorer la sémantique
- ⭐ Créer un **fichier `.well-known/`** pour la vérification Google Search Console

### Technique
- ⭐ Externaliser le CSS commun dans `style.css` et le lier avec `<link>` (actuellement dupliqué 14×)
- ⭐ Minifier le HTML/CSS/JS pour améliorer les performances
- ⭐ Ajouter `defer` sur les scripts inline
- ⭐ Ajouter `preload` sur le logo pour améliorer le LCP
- ⭐ Configurer des en-têtes HTTP de sécurité (Content-Security-Policy, X-Frame-Options)

### Contenu
- ⭐ Ajouter une page **"Politique de confidentialité"** dédiée (le lien existe déjà dans le formulaire)
- ⭐ Ajouter une section **"Certifications"** (Qualifelec, assurance) avec logos
- ⭐ Ajouter un **blog** ou des actualités pour du contenu SEO frais
- ⭐ Ajouter une page **"Témoignages"** avec photos clients (avec consentement)

---

## 12. CHECKLIST PAR PAGE

| Page | Header OK | Nav OK | Footer OK | OG | Schema | Dark mode | Liens valides |
|---|---|---|---|---|---|---|---|
| index.html | ✅ | ✅ | ⚠️ Tarn→Occitanie | ✅ | ❌ #website manquant | ✅ | ✅ |
| services.html | ✅ | ✅ | ✅ (Occitanie) | ✅ | ✅ ItemList | ❌ | ❌ 5 liens `#` |
| about.html | ✅ | ❌ avis manquant | ✅ (Occitanie) | ✅ | ❌ URLs erronées | ❌ | ✅ |
| contact.html | ✅ | ✅ | ⚠️ Tarn→Occitanie | ✅ | ❌ URLs erronées | ❌ | ❌ Lien politique `#` |
| faq.html | ✅ | ✅ | ❌ HTML cassé | ✅ | ✅ FAQPage | ❌ | ✅ |
| realisations.html | ✅ | ✅ | ✅ (Occitanie) | ✅ | ✅ CollectionPage | ❌ | ✅ |
| avis.html | ❌ layout | ❌ nav manquante | ✅ (Occitanie) | ✅ | ✅ WebPage | ✅ | ❌ RS `#` |
| merci.html | ❌ layout | ✅ | ✅ (Occitanie) | ✅ | ✅ WebPage | ❌ | ❌ RS `#` |
| mentions-legales.html | ✅ | ✅ | ✅ (Occitanie) | ✅ | ✅ WebPage | ❌ | ❌ RS `#` |
| 6 × villes/ | ✅ | ✅ | N/A | ✅ | ✅ LocalBusiness | ❌ | ✅ |

---

## CONCLUSION

Le site Elekio a une **base solide** : contenu de qualité, message clair, SEO de base en place, fonctionnalité satisfaisante (formulaire, accordéon FAQ, responsive). 

Les **problèmes critiques** sont :
1. **style.css externe inutilisé** avec des règles contradictoires — source de confusion
2. **HTML cassé dans faq.html footer**
3. **Navigation incomplète** sur avis.html et about.html

Les **problèmes importants** :
4. **Footer texte incohérent** (Tarn vs Occitanie)
5. **Schema.org incomplet** (#website manquant, URLs erronées)
6. **Dark mode absent** sur 8 pages + 6 pages villes
7. **Liens morts** (Facebook, LinkedIn, politique confidentialité)
8. **DPE confondu avec diagnostic électrique** dans la FAQ

**Temps estimé pour les corrections immédiates : 2-3 heures**  
**Temps estimé pour les améliorations recommandées : 1-2 jours**

---

*Rapport généré automatiquement par Hermes Agent — Audit complet du 7 juillet 2026*
