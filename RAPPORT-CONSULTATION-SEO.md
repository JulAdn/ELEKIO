# 📋 RAPPORT DE CONSULTATION SEO — Elekio (Électricien Tarn 81)
## Web Creator → Profile SEO — 6 juillet 2026

---

## 1. Travaux effectués (audit + corrections)

### ✅ Corrections terminées

| Catégorie | Élément | Statut |
|-----------|---------|--------|
| **Contenu** | about.html revu (ton professionnel centré client, pas de CV) | ✅ |
| **Contenu** | Domotique → Petits travaux dans services.html | ✅ |
| **SEO technique** | Sitemap.xml créé (10 URLs) | ✅ |
| **SEO technique** | Robots.txt avec référence sitemap | ✅ |
| **SEO technique** | Favicon type="image/png" sur toutes les pages | ✅ |
| **SEO technique** | Canonical sur toutes les pages (10/10) | ✅ |
| **SEO technique** | Schema.org LocalBusiness Electrician toutes pages | ✅ |
| **SEO technique** | llms.txt créé (AI SEO) | ✅ |
| **Pages villes** | electricien-albi.html (Albi) | ✅ |
| **Pages villes** | electricien-castres.html (Castres) | ✅ |
| **Logo** | Logo EK stylisé (SVG + PNG) responsive | ✅ |
| **Formulaire** | Formsubmit.co endpoint réel | ✅ |
| **Déploiement** | Site live sur elekio.pages.dev (HTTP 200) | ✅ |
| **Réseaux** | Instagram @elekio_electricite actif | ✅ |

### ⚠️ Points résiduels

| Problème | Pages concernées | Priorité |
|----------|------------------|----------|
| Meta descriptions >160 chars | index (201), about (201), services (216), albi (194), castres (198) | 🟠 P1 |
| Liens Facebook/LinkedIn morts (href="#") | Toutes les pages | 🟡 P2 |
| Liens zones intervention (services.html) en href="#" | services.html (Albi, Castres devraient pointer vers pages villes) | 🟡 P2 |
| Images sans width/height explicites (style="height:Xpx;width:auto") | index.html, footer | 🟡 P2 (CLS) |
| Pas de photo réelle de Julian | Toutes les pages | 🟡 P2 |
| Pas de Google Analytics/Search Console | — | 🟠 P1 |
| H1 absent sur certaines pages | about (h2 seulement), contact, faq, mentions-legales, merci, realisations | 🟡 P2 |

---

## 2. Les 3 points SEO les plus importants à corriger AVANT mise en ligne

D'après la grille d'audit du profile SEO (`seo-local-business-audit` + `seo-audit-extras`) :

### 🔴 P0 — N°1 : Réduire les meta descriptions trop longues
**Problème :** 5/10 pages ont des meta descriptions >160 caractères (jusqu'à 216 pour services.html). Google tronque à ~155-160 pixels, ce qui coupe le message et la CTA.
**Correctif :** Resize toutes les meta descriptions à 150-160 caractères max, avec mot-clé principal + CTA (ex: "Devis gratuit sous 24h").
**Impact :** Amélioration du CTR dans les SERP.

### 🟠 P1 — N°2 : Ajouter Google Search Console + GA4
**Problème :** Aucun tracking analytics ni Search Console configuré. Impossible de savoir quels mots-clés rankent, combien de visiteurs, d'où ils viennent.
**Correctif :** Configurer GSC + GA4 (instructions détaillées section 4 ci-dessous).
**Impact :** Mesure de performance SEO indispensable.

### 🟠 P1 — N°3 : Créer un maillage interne des pages villes
**Problème :** Les pages Albi et Castres existent mais ne sont pas liées depuis les pages principales. Les liens "Albi" et "Castres" dans services.html pointent vers `href="#"`.
**Correctif :** Pointer ces liens vers les pages villes, ajouter des liens contextuels dans about.html et index.html.
**Impact :** Distribution du jus de lien, meilleur crawl, pages villes mieux indexées.

---

## 3. Pages villes — Pertinence et contenu

### ✅ OUI, créer des pages villes est TRÈS pertinent pour le SEO local d'Elekio

**Pourquoi :**
- Zone de service couvre 18 villes (Albi, Castres, Lavaur, Mazamet, Graulhet, Rabastens, Gaillac, Toulouse, etc.)
- Chaque page ville capture le trafic de recherche locale "électricien [ville]"
- Ces pages renforcent le EEAT local et le Local Pack Google
- Les concurrents locaux les utilisent (ex: électriciens Albi, Castres)

### Pages déjà créées : ✅ Albi, ✅ Castres

### Pages à créer prioritairement (prochaine batch) :

| Priorité | Ville | Mot-clé | Volume estimé |
|----------|-------|---------|---------------|
| 🔴 | **Lavaur** | électricien Lavaur | Fort (proche Saint-Sulpice) |
| 🔴 | **Graulhet** | électricien Graulhet | Fort |
| 🟠 | **Mazamet** | électricien Mazamet | Moyen |
| 🟠 | **Rabastens** | électricien Rabastens | Moyen |
| 🟠 | **Gaillac** | électricien Gaillac | Moyen |
| 🟡 | **Toulouse** | électricien Toulouse | Très fort mais très concurrentiel |
| 🟡 | **Montauban** | électricien Montauban | Fort |

### Contenu à mettre dans chaque page ville (template) :

```
1. H1 : "Électricien à [Ville] (81) — Elekio intervient dans le [zone]"
2. Intro (80-100 mots) : Qui est Elekio, que fait-il à [Ville]
3. Services spécifiques pour [Ville] :
   - Dépannage urgence sous 4h
   - Installation neuve
   - Rénovation mise aux normes
   - Diagnostic DPE / avant-achat
   - Remplacement tableau électrique
4. Quartiers spécifiques de la ville (si connus)
5. CTA localisée : "Devis gratuit électricien [Ville]"
6. Schema.org LocalBusiness avec areaServed:[Ville]
7. Lien vers les autres pages villes + pages principales
```

**⚠️ Anti-duplicate content :** Chaque page ville doit avoir un contenu UNIQUE :
- Parler des quartiers spécifiques
- Mentionner des points de repère locaux
- Adapter le ton au type de clientèle (centre ancien, lotissements, zones pavillonnaires)
- Ne PAS copier-coller le même texte en changeant juste le nom de ville

---

## 4. Configuration Google Search Console + GA4

### Google Search Console

**Étapes :**
1. Aller sur https://search.google.com/search-console
2. Ajouter propriété : **URL prefix** → `https://www.elekio.fr/`
3. Méthode de vérification recommandée : **DNS TXT record** (si domaine personnalisé) ou **balise HTML**
4. Si balise HTML : Copier la meta tag de vérification et l'ajouter dans le `<head>` de index.html
5. Soumettre le sitemap : `https://www.elekio.fr/sitemap.xml`
6. Vérifier que Cloudflare Pages ne bloque pas le crawler Google

**Pour Cloudflare Pages (elekio.pages.dev → elekio.fr) :**
- Ajouter un enregistrement TXT DNS pour vérifier le domaine
- OU utiliser la méthode HTML dans toutes les pages

### Google Analytics 4 (GA4)

**Étapes :**
1. Aller sur https://analytics.google.com → Créer une propriété GA4
2. Obtenir le **Measurement ID** (format : G-XXXXXXXXXX)
3. Ajouter le code GA4 dans toutes les pages HTML (dans `<head>`) :

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

4. Pour site statique (pas de CMS), l'ajouter manuellement dans CHAQUE page HTML
5. Alternative : Utiliser **Plausible** ou **Fathom** (plus légers, RGPD-friendly)

### Recommandation du profile SEO :
> Utiliser **Plausible Analytics** (https://plausible.io) pour un site statique d'artisan — plus léger que GA4, respecte le RGPD sans cookie banner, et suffisant pour le suivi SEO d'Elekio. Pas besoin de GA4 pour un petit site vitrine.

---

## 5. Prêt pour mise en ligne ?

### ✅ OUI — Le site est prêt pour mise en ligne officielle

**Ce qui est bon :**
- ✅ Déploiement fonctionnel sur elekio.pages.dev (HTTP 200)
- ✅ Toutes les pages ont des URLs canoniques
- ✅ Schema.org correct
- ✅ Contenu honnête (pas de fausses certifs, pas de faux avis)
- ✅ Site responsive avec charte graphique cohérente
- ✅ Favicon, robots.txt, sitemap.xml

### 🔧 Corrections recommandées AVANT mise en ligne officielle (elekio.fr)

| Priorité | Correction | Effort |
|----------|------------|--------|
| 🔴 P0 | Réduire meta descriptions (5 pages trop longues) | 15 min |
| 🟠 P1 | Configurer Search Console pour indexer | 30 min |
| 🟠 P1 | Vérifier que le domaine elekio.fr pointe bien vers Cloudflare Pages | — |
| 🟠 P1 | Ajouter GA4 ou Plausible | 20 min |
| 🟡 P2 | Remplacer liens sociaux morts par liens réels (ou cacher Instagram seul en attendant) | 10 min |
| 🟡 P2 | Ajouter width/height explicites aux images (CLS) | 15 min |
| 🟡 P2 | Ajouter photo réelle de Julian (quand disponible) | — |

**Note SSL :** Cloudflare Pages fournit automatiquement le SSL (HTTPS). Aucune configuration supplémentaire nécessaire.

---

## 6. Résumé des recommandations du profile SEO

> *Les recommandations ci-dessous sont produites à partir de l'analyse utilisant les skills du profile SEO (`seo-local-business-audit`, `seo-content-integrity`, `artisan-site-audit`, `seo-audit-extras`)*

### 🔴 P0 — Avant mise en ligne (immédiat)

1. **Meta descriptions** — Réduire à 150-160 chars : index, about, services, albi, castres
2. **Search Console** — Ajouter propriété et soumettre sitemap
3. **Maillage interne** — Pointer les liens villes services.html → pages villes réelles

### 🟠 P1 — Cette semaine

4. **Pages villes supplémentaires** — Créer Lavaur, Graulhet, Mazamet, Rabastens
5. **GA4 ou Plausible** — Analytics nécessaire pour suivre le trafic
6. **Liens zones services.html** — Pointer Albi→electricien-albi.html, Castres→electricien-castres.html
7. **Image CLS** — Ajouter width/height explicites aux logos

### 🟡 P2 — Ce mois

8. **Photo Julian** — Une photo réelle en hero (rendue disponible)
9. **Liens sociaux** — Facebook et LinkedIn à créer, ou cacher les icônes
10. **Villes restantes** — Gaillac, Toulouse, Montauban, Mazamet
11. **BreadcrumbList schema** — Ajouter pour toutes les pages (aide AI Overviews)

### 🟢 P3 — Bonus

12. **FAQ schema** sur faq.html (déjà en place ? vérifier)
13. **Page "Tarifs"** (realisations.html) → enrichir avec plus de vrais tarifs
14. **EEAT** → Ajouter mentions RCS Castres, assurance décennale, SIRET

---

**Consultation terminée.** Les recommandations ont été transmises dans la mémoire du profile SEO (`~/.hermes/profiles/seo/memories/MEMORY.md`) pour traçabilité. Le site est fonctionnel et les corrections P0 de contenu (about, domotique, logo) sont faites. Les 3 points prioritaires avant mise en ligne officielle sont : **meta descriptions**, **Search Console**, et **maillage interne des pages villes**.
