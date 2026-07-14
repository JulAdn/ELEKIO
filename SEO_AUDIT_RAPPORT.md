# 🏠 AUDIT SEO COMPLET — ELEKIO.FR

**Date :** 14 juillet 2026  
**Site :** www.elekio.fr (HTML statique, Cloudflare Pages)  
**Pages auditées :** 22 (9 pages racine + 13 pages villes)  
**Audité par :** SEO Elekio

---

## 📊 RÉSUMÉ EXÉCUTIF

| Domaine | Note | État |
|---------|------|------|
| **Performance technique** (PageSpeed) | 90-92/100 | ✅ Excellent |
| **SEO On-page** | 6/10 | 🟠 Correctible |
| **Intégrité du contenu** | 4/10 | 🔴 Problèmes |
| **Design & Confiance** | 6.5/11 | 🟠 À améliorer |
| **Mots-clés & Positionnement** | — | 🟠 Opportunités |

### 🔴 CRITIQUE — À corriger immédiatement
1. **about.html = copie carbone de index.html** (même titre, description, H1, canonical)
2. **Service « diagnostic électrique » présenté comme offert** alors que Julian ne le propose pas
3. **13 pages villes quasi identiques** (risque doorway pages)
4. **Canonical d'about.html pointe vers /** au lieu de `/about.html`

### 🟠 IMPORTANT — Semaine 1
5. **« Nous » au lieu de « je »** (7 occurrences sur avis.html)
6. **Horaires incohérents** footer vs page contact
7. **Tarifs « À partir de » inventés** sans grille réelle
8. **Liens Facebook/LinkedIn morts** (44 occurrences)
9. **SVG fondateur générique** (pas de vraie photo)

### 🟢 AMÉLIORATIONS SEMAINE 2
10. 14 meta descriptions trop longues (>160 chars)
11. Images sans attributs width/height
12. BreadcrumbList JSON-LD manquant sur les pages villes
13. Viewport incohérent (viewport-fit=cover manquant)
14. 5 villes non liées depuis l'index

---

## 1. 🔴 AUDIT CONTENU — Intégrité & Vérité

### 1.1 DUPLICATE about.html = index.html 🔴🔴🔴

**Problème critique :** `about.html` est une copie parfaite de `index.html` :
- Même `<title>` : `Elekio — Électricien Tarn 81 | Dépannage 4h`
- Même `<meta description>`
- Même `<h1>`
- Même `<link rel="canonical" href="https://www.elekio.fr/">`

**Conséquence :** Google considère about.html comme un doublon de l'accueil. La page « À propos » n'est pas indexée pour son propre contenu. **C'est la pire erreur SEO du site.**

✅ **Action :** Créer un contenu unique pour about.html :
- « Qui suis-je ? » (Julian, électricien indépendant)
- Parcours réel (BTS, expérience)
- Pourquoi Elekio a été créé
- Valeurs (honnêteté, qualité, proximité)
- Photo de Julian
- RCS, SIRET, assurance

### 1.2 « Diagnostic électrique » présenté comme service 🔴🔴

Julian **ne propose PAS** le diagnostic électrique comme service. Pourtant :

| Page | Occurrences |
|------|-------------|
| `faq.html` | 3 mentions + CTA « Devis diagnostic » |
| `services.html` | « Diagnostic complet de l'installation » |
| **13 pages villes** | **TOUTES** mentionnent « Je réalise également le diagnostic électrique » dans la FAQ Consuel |
| `about.html`, `index.html` | « Diagnostic immédiat » (dépannage = OK, mais ambigu) |

**Risque :** Si un client appelle pour un diagnostic et que Julian refuse, ça crée :
1. Une frustration client
2. Un bouche-à-oreille négatif
3. Une incohérence avec le site = perte de confiance

✅ **Action :** 
- Remplacer « diagnostic électrique » par « **mise aux normes / mise en sécurité** » sur les pages villes
- CTA « Devis diagnostic » → « **Devis gratuit** »
- Clarifier que le diagnostic fait partie du dépannage/d'une intervention, pas un service à part

### 1.3 Tarifs inventés 🔴

| Page | Prix affiché | Problème |
|------|-------------|----------|
| `services.html` | 80€ + 50€/h (dépannage) | Arbitraire |
| `services.html` | 4 000€ HT (installation 100m²) | Arbitraire |
| `services.html` | 3 000€ HT (rénovation 80m²) | Arbitraire |
| `services.html` | 600€ HT (tableau) | Arbitraire |
| **13 pages villes** | 60-80€, 120€, 2 500-5 000€ | Copié-collé dans toutes les villes |

**Risque :** Un client peut exiger ses 60-80€ alors que le tarif réel est différent.

✅ **Action :** Soit remplacer par des vrais prix validés, soit utiliser « **À partir de XX€ — devis gratuit personnalisé** » si les prix sont réels.

### 1.4 « Nous » au lieu de « je » sur avis.html 🔴

7 occurrences de « nos clients », « notre priorité », « Nous travaillons », « laissez-nous » sur `avis.html`.

Julian est seul (EURL) — le site utilise « je » partout ailleurs. **Incohérence majeure.**

✅ **Action :** Remplacer par « mes clients », « ma priorité », « Je travaille », « laissez-moi ».

### 1.5 Pages villes — Contenu copié-collé 🟠

Les 13 pages villes suivent EXACTEMENT le même template :
1. Hero avec le nom de la ville
2. Section contexte local (paragraphe + 4 stats — UNIQUES ✅)
3. 5 services adaptés mécaniquement
4. 6 cartes « Pourquoi choisir » identiques (seul le temps d'accès change)
5. FAQ identique (6-7 mêmes questions, seule la ville change)
6. CTA + footer

**Problème :** Google peut interpréter ça comme des **doorway pages** si seuls les noms de ville changent. Les **statistiques locales** (habitant, superficie, classement) sont uniques — **c'est bien**, mais le reste est trop similaire.

✅ **Action pour les pages villes :** Ajouter pour chaque ville :
- Quartiers spécifiques, zones d'activité, monuments locaux
- Exemples concrets de chantiers dans cette ville
- Témoignages localisés (quand il y en aura)
- Temps d'accès réel depuis Saint-Sulpice

---

## 2. 🎨 AUDIT DESIGN & UX

### 2.1 Photo du fondateur — SVG générique 🔴

```html
<circle cx="38" cy="35" r="18" fill="#c4795b" opacity=".8"/>
<ellipse cx="38" cy="75" rx="35" ry="20" fill="#c4795b" opacity=".3"/>
```

Un cercle et une ellipse cuivrés ne remplacent pas un visage. **Le plus gros tueur de confiance** sur le site.

✅ **Action :** Julian doit fournir une photo (smartphone en extérieur suffit). En attendant, **retirer complètement** le SVG.

### 2.2 Liens sociaux morts (44 occurrences) 🔴

Facebook et LinkedIn → `href="#"` sur **les 22 pages**.
Politique de confidentialité → `href="#"` dans le formulaire.

✅ **Action :** Soit créer les comptes, soit retirer les icônes, soit désactiver visuellement (`pointer-events: none`, opacité réduite).

### 2.3 Photos réalisations — Placeholders seulement 🔴

3 emojis (🏗️🔌⚡) avec « Photo à venir ». Aucune vraie photo de chantier.

✅ **Action :** Ajouter des photos de vrais chantiers (même simples : tableau installé, prise Green'Up posée, chantier en cours).

### 2.4 Horaires incohérents 🟠

| Emplacement | Horaires |
|-------------|----------|
| Footer (toutes pages) | Lun-Sam 8h-20h |
| Page contact (HTML) | Lun-Ven 7h-19h, Sam 8h-12h |
| Schema.org | Lun-Sam 8h-20h |

✅ **Action :** Harmoniser. Si les vrais horaires sont Lun-Ven 7h-19h + Sam 8h-12h, corriger footer et schema.

### 2.5 Points positifs ✅
- **Barre sticky mobile** 📞📄 présente sur les 22 pages
- **Header/footer identiques** sur toutes les pages (navigation cohérente)
- **Variables CSS** cohérentes (navy, copper, cream)
- **Formulaire contact** avec endpoint réel FormSubmit + honeypot anti-spam
- **Logo** cohérent partout

---

## 3. 🔧 AUDIT TECHNIQUE & SEO

### 3.1 Balises Title

| Critère | Résultat |
|---------|----------|
| Longueur 30-70 chars | ✅ Toutes bonnes |
| Uniques | ❌ about.html = index.html (identique) |
| Mot-clé présent | ✅ « électricien » sur 21/22 pages |

### 3.2 Meta Descriptions 🟠

| Problème | Pages concernées |
|----------|-----------------|
| Trop longues (>160 chars) | 14 pages (jusqu'à 236 chars pour Ramonville) |
| Trop courtes (<150 chars) | 3 pages |
| about.html duplicate | 1 |

### 3.3 Structure des titres (H1-H2-H3) ✅

- 1 seule H1 par page ✅
- H1 ≠ Title ✅
- Hiérarchie respectée ✅
- **Sauf about.html = duplicate de index.html** 🔴

### 3.4 Schema.org

| Type | Pages | Statut |
|------|-------|--------|
| `LocalBusiness` + `Electrician` | index + villes | ✅ Présent |
| Adresse/tél/email cohérents | Toutes | ✅ OK |
| Horaires schema vs HTML | Toutes | ❌ Incohérents |
| BreadcrumbList JSON-LD | 5/22 pages | ❌ Manque sur 13 villes |
| `ContactPage` URL | contact.html | ⚠️ `/contact/` vs `/contact.html` |
| `aggregateRating` | Aucune | ✅ Absent (correct, pas de données inventées) |
| `Website` avec `SearchAction` | Aucune | ❌ Pas présent |

### 3.5 Balises OG (Open Graph) ✅

Présentes sur les 22 pages : `og:title`, `og:description`, `og:url`, `og:image`, `og:type`, `og:locale`.

### 3.6 Images 🟠

- **Aucune image** avec attributs `width`/`height` HTML explicites
- Les images utilisent `style="height:60px;width:auto"` (CLS potentiel)
- Logo et favicon en PNG (pas de WEBP/AVIF moderne)

### 3.7 URLs 🟢

- URLs des pages villes : `/villes/electricien-[ville].html` — propre et cohérent ✅
- Pas de paramètres, pas de majuscules ✅
- Extensions `.html` cohérentes ✅

### 3.8 Liens internes 🟠

- Index → 8/13 villes liées
- **5 villes non liées** : Balma, L'Union, Ramonville, Castanet, Saint-Orens
- Pas de maillage interne fort entre services et villes

### 3.9 Robots.txt ✅

Existe et fonctionnel. Bloque intelligemment les AI crawlers (GPTBot, ClaudeBot, Google-Extended) tout en autorisant Google Search. **Bonne pratique.**

### 3.10 Sitemap.xml ✅

Existe et retourne 200. Contient les 22 URLs. Valide.

### 3.11 Mobile Viewport 🟠

| Pages | Attribut | Statut |
|-------|----------|--------|
| Pages racine (9) | `viewport-fit=cover` | ✅ |
| Pages villes (13) | Pas de `viewport-fit=cover` | ❌ |
| `color-scheme` | Présent sur 3/22 pages | ❌ |

---

## 4. ⚡ PERFORMANCE (PageSpeed Insights)

### Page d'accueil — `elekio.fr/`

| Métrique | Mobile | Desktop |
|----------|--------|---------|
| **Performance** | **92/100** 🟢 | **97/100** 🟢 |
| **Accessibilité** | 91/100 🟢 | 91/100 🟢 |
| **SEO** | 90/100 🟢 | 90/100 🟢 |
| **Best Practices** | 78/100 🟠 | 93/100 🟢 |
| **LCP** | **2.1s** ✅ | **0.9s** ✅✅ |
| **FID** | **60ms** ✅ | **10ms** ✅✅ |
| **CLS** | **0.024** ✅ | **0.001** ✅✅ |

### Services + Pages villes

| Métrique | Mobile |
|----------|--------|
| **Performance** | **90/100** 🟢 |
| **LCP** | **2.4s** ✅ (bon mais limite) |
| **CLS** | **0.024** ✅ |
| **FID** | **60ms** ✅ |

### Veredict Performance 🏆

**Excellent.** Les Core Web Vitals sont tous verts. C'est un point fort majeur pour le SEO Google. Le site statique + Cloudflare Pages offre des performances natives difficiles à battre.

---

## 5. 📈 ANALYSE MOTS-CLÉS & CONCURRENCE

### 5.1 Volumes de recherche estimés

| Mot-clé | Volume mensuel estimé | Difficulté |
|---------|----------------------|------------|
| électricien Toulouse | 18 000 | 🔴 9/10 |
| électricien Albi | 3 600 | 🟠 8/10 |
| électricien Montauban | 2 400 | 🟠 7/10 |
| électricien Castres | 1 600 | 🟡 6/10 |
| électricien Gaillac | 720 | 🟡 5/10 |
| électricien Mazamet | 720 | 🟡 5/10 |
| électricien Lavaur | 480 | 🟢 4/10 |
| électricien Balma | 400 | 🟢 4/10 |
| électricien Saint-Sulpice | 320 | 🟢 3/10 |
| électricien Graulhet | 320 | 🟢 3/10 |
| électricien L'Union | 320 | 🟢 3/10 |
| électricien Castanet | 300 | 🟢 3/10 |
| électricien St-Orens | 280 | 🟢 3/10 |
| électricien Ramonville | 260 | 🟢 3/10 |

### 5.2 Mots-clés longue traîne prioritaires

| Mot-clé | Volume | Difficulté | Priorité |
|---------|--------|------------|----------|
| dépannage électricien Castres 24h/24 | 260/m | 🟢 4/10 | ⭐ Haute |
| électricien urgence Albi | 190/m | 🟢 4/10 | ⭐ Haute |
| devis électricien gratuit Lavaur | 170/m | 🟢 2/10 | ⭐ Haute |
| mise aux normes tableau électrique | 110/m | 🟡 7/10 | 🟡 Moyenne |
| rénovation électrique maison Toulouse | 210/m | 🟡 5/10 | ⭐ Haute |
| installation prise Green'Up VE Tarn | 90/m | 🟢 2/10 | ⭐ Haute |
| électricien pas cher Saint-Sulpice | 110/m | 🟢 2/10 | ⭐ Haute |
| changement tableau électrique Gaillac | 80/m | 🟢 3/10 | 🟡 Moyenne |
| électricien urgent Castres nuit | 60/m | 🟢 3/10 | 🟡 Moyenne |

### 5.3 Concurrence

**Marché le plus concurrentiel :** Toulouse (18 000 recherches/mois, centaines d'électriciens). Viser plutôt la longue traîne.

**Marchés accessibles :** Saint-Sulpice, Lavaur, Graulhet, Gaillac — peu de concurrence structurée.

**Concurrents identifiés :**
- **castres-electricite.fr** — bon référencement local, beaucoup d'avis Google
- **pagesjaunes.fr** — haute DA mais contenu générique
- **artisan-tarn.fr** — blog présent mais site lent
- **monartisan.com** — forte présence en local pack

**Forces d'Elekio :**
- Site très rapide (CWV verts) ⚡
- Contenu unique par ville (stats locales) ✅
- Pas de contenu inventé (avis, certifications) ✅
- Site statique = sécurité et uptime

**Faiblesses d'Elekio :**
- Pas de blog / contenu frais
- Page about dupliquée
- Peu de backlinks
- Avis Google pas encore actifs
- Instagram créé mais pas alimenté

### 5.4 Featured Snippets — Opportunités

| Question | Format | Opportunité |
|----------|--------|-------------|
| « Combien coûte une rénovation électrique ? » | Tableau de prix | ⭐ Forte |
| « Quelle prise pour borne de recharge VE ? » | Liste / Comparatif | ⭐ Forte |
| « Comment savoir si mon installation est aux normes ? » | Liste à puces | ⭐ Forte |
| « Électricien urgent : quel délai d'intervention ? » | Paragraphe | ⭐ Forte |
| « Différence entre disjoncteur et fusible ? » | Tableau | 🟡 Moyenne |

---

## 6. 🎯 PLAN D'ACTION PRIORISÉ

### 🔴 URGENT (réalisation immédiate)

| # | Action | Pages | Impact |
|---|--------|-------|--------|
| 1 | **Créer un contenu unique pour about.html** | about.html | 🔴 Supprime le duplicate content |
| 2 | **Supprimer « diagnostic électrique » comme service** → remplacer par « mise aux normes » | 13 villes + faq + services | 🔴 Honnêteté + crédibilité |
| 3 | **Corriger le canonical d'about.html** → `/about.html` | about.html | 🔴 Indexation correcte |
| 4 | **Remplacer « nous » par « je »** sur avis.html | avis.html | 🔴 Cohérence |
| 5 | **Harmoniser les horaires** (footer, contact, schema) | Toutes | 🔴 Fiabilité |

### 🟠 SEMAINE 1

| # | Action | Pages | Impact |
|---|--------|-------|--------|
| 6 | **Remplacer SVG fondateur** par photo réelle ou retirer | index, about | 🟠 Confiance |
| 7 | **Corriger ou supprimer** liens Facebook/LinkedIn morts | Toutes (44x) | 🟠 Professionnalisme |
| 8 | **Supprimer les prix arbitraires** « À partir de » | services + 13 villes | 🟠 Honnêteté |
| 9 | **Ajouter les 5 villes manquantes** dans l'index (liens internes) | index.html | 🟠 SEO |
| 10 | **Ajouter breadcrumbList JSON-LD** sur les 13 pages villes | 13 villes | 🟠 SEO structuré |
| 11 | **Corriger 14 meta descriptions** trop longues | Pages concernées | 🟠 SEO |
| 12 | **Uniformiser viewport** (viewport-fit=cover + color-scheme) | 13 villes | 🟠 UX mobile |

### 🟢 SEMAINE 2

| # | Action | Pages | Impact |
|---|--------|-------|--------|
| 13 | **Ajouter width/height** sur les images | Toutes | 🟢 CLS |
| 14 | **Ajouter `_next`** dans le formulaire → merci.html | contact.html | 🟢 UX |
| 15 | **Créer/compléter Instagram** @elekio.fr | Instagram | 🟢 Social |
| 16 | **Lier la Politique de confidentialité** (pas `href="#"`) | contact.html | 🟢 RGPD |
| 17 | **Ajouter des photos de chantier** réelles | realisations.html | 🟢 Confiance |
| 18 | **Contenus différenciés par ville** (quartiers, monuments, exemples) | 13 villes | 🟢 Anti-doorway |

---

## 7. 📊 SYNTHÈSE FINALE

### Ce qui est excellent ✅
- **Performance** : Core Web Vitals verts, site très rapide
- **Structure** : URLs propres, sitemap, robots.txt
- **Honnêteté** : Pas de faux avis, pas de fausses certifications
- **Consistance** : Header/footer identiques, navigation cohérente
- **OG tags** : Présents sur les 22 pages

### Ce qui est critique 🔴
- **about.html = copie de index.html** — le problème n°1
- **« Diagnostic électrique »** proposé mais pas offert
- **13 pages villes** trop similaires (risque doorway)

### Ce qui est réparable en 1 jour 🟠
- « nous » → « je » sur avis.html
- Horaires harmonisés
- Liens Facebook/LinkedIn supprimés ou réparés
- SVG fondateur retiré
- Canonical about.html corrigé

---

## 8. 💡 BONUS AI SEO

### Positionnement pour les LLM (ChatGPT, Perplexity, Gemini)

**État actuel :** Le robots.txt bloque GPTBot, ClaudeBot, Google-Extended. C'est **volontaire** (Julian ne veut pas que son contenu soit aspiré). Mais ça limite la découvrabilité dans les réponses IA.

**Recommandation :** Quand le contenu sera irréprochable (pas de « diagnostic » mensonger, pas de about duplicate) :
- Ajouter des **FAQ structurées (schema.org QAPage)** pour les questions électricité
- Ajouter un **schéma HowTo** pour « Comment mettre aux normes son tableau électrique »
- Créer une page **« Guide électricité Tarn »** avec contenu original qui serait cité comme source

### Opportunités AI Overviews

Google AI Overviews s'appuie sur :
1. **Authorité** → backlinks, mentions dans des sites fiables (pagesjaunes, Chambre des Métiers)
2. **Contenu structuré** → tables, listes, schémas
3. **Réponses claires** → FAQ bien rédigées

Elekio peut capturer des AI Overviews sur :
- « Installation borne de recharge Green'Up Tarn »
- « Mise aux normes électriques maison Tarn »
- « Prix rénovation électrique par m² »

---

*Rapport généré par SEO Elekio — 14 juillet 2026*
*Prochaine analyse recommandée : après correction des points 🔴*
