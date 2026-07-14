# 🚀 Guide de mise en ligne — Elekio

## Google Search Console · Google Analytics 4 · Domaine elekio.fr

---

## 1️⃣ Google Search Console (Gratuit)

### Étape 1 — Créer le compte
1. Va sur **https://search.google.com/search-console/**
2. Connecte-toi avec ton email **contact@elekio.fr**
3. Clique sur **"Ajouter une propriété"** → **"Préfixe d'URL"**
4. Saisis : `https://www.elekio.fr`
5. Clique sur **"Continuer"**

### Étape 2 — Vérifier la propriété
Google va te demander de prouver que tu es bien le propriétaire du site.

👉 **Méthode recommandée : la balise HTML**

1. Google te donne une **balise meta** qui ressemble à :
   ```html
   <meta name="google-site-verification" content="XXXXXXXXXXXXXXX" />
   ```
2. Copie cette ligne
3. **Je l'ajoute** dans le `<head>` de toutes les pages du site (je fais ça pour toi)
4. Une fois que je l'ai ajoutée, reviens sur Search Console et clique **"Vérifier"**

✅ **C'est fait !** Google commence à indexer ton site.

### À savoir
- Search Console est **un outil de diagnostic** — tu ne paramètres rien, tu regardes les données
- Tu y verras : les mots-clés qui t'amènent du trafic, les erreurs techniques, les clics
- Ça prend **2 à 7 jours** avant d'avoir les premières données

---

## 2️⃣ Google Analytics 4 (GA4) — Gratuit

### Étape 1 — Créer le compte
1. Va sur **https://analytics.google.com/**
2. Connecte-toi avec ton email **contact@elekio.fr**
3. Clique sur **"Commencer"**
4. **Nom du compte :** `Elekio`
5. **Propriété :** `Site Elekio`
6. **Fuseau horaire :** `France (GMT+1)`
7. **Devise :** `Euro (EUR)`
8. **Secteur :** `Services aux entreprises / Construction`
9. Clique sur **"Créer"**

### Étape 2 — Configurer le flux de données
1. Clique sur **"Web"**
2. **URL du site :** `https://www.elekio.fr`
3. **Nom du flux :** `Site Elekio`
4. Clique sur **"Créer le flux"**

### Étape 3 — Récupérer le code de suivi
1. Google va te donner un **tag** qui ressemble à ça (tu peux le copier-coller) :

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

2. Copie ce bloc de code
3. **Je l'ajoute** dans le `<head>` de toutes les pages du site (je fais ça pour toi)
4. Si tu veux vérifier que ça marche : installe l'extension **"GA Debugger"** sur Chrome

### Étape 4 (optionnelle) — Configurer un objectif
Tu peux suivre combien de personnes remplissent le formulaire de contact :

1. Dans GA4, va dans **"Administration"** → **"Objectifs"**
2. **"Nouvel objectif"**
3. **Type :** `Personnalisé`
4. **Nom :** `Envoi formulaire de devis`
5. **Détail :** `Événement` → `page_view` → contient `merci.html`

✅ **GA4 est prêt** — tu verras le nombre de visiteurs, d'où ils viennent, et ce qu'ils font sur ton site.

---

## 3️⃣ Pointer elekio.fr vers Cloudflare Pages

**Prérequis :** Tu dois avoir accès à ton compte OVH (identifiant client + mot de passe ou accès via e-mail).

### Étape 1 — Se connecter à OVH
1. Va sur **https://www.ovh.com/**
2. Clique sur **"Espace client"** en haut à droite
3. Connecte-toi avec ton identifiant client OVH (généralement un code comme `ab12345-ovh`)
4. Tu arrives sur le tableau de bord

### Étape 2 — Accéder au domaine
1. Dans le menu de gauche, clique sur **"Web Cloud"**
2. Puis sur **"Noms de domaine"**
3. Clique sur **elekio.fr** dans la liste

### Étape 3 — Modifier les serveurs DNS (Nameservers)
> ⚠️ **Attention :** Cette opération peut prendre **24 à 48h** pour être effective (propagation DNS).

1. Dans la page du domaine, clique sur **"Serveurs DNS"**
2. Tu vois une liste de serveurs OVH (ex: `dnsXX.ovh.net`, `nsXX.ovh.net`)
3. Clique sur **"Modifier les serveurs DNS"**
4. **Remplace TOUS les serveurs OVH par CEUX de Cloudflare :**

```
alexis.ns.cloudflare.com
kate.ns.cloudflare.com
```

5. Clique sur **"Suivant"** puis **"Valider"**

### Étape 4 — Configurer Cloudflare
Avant de faire l'étape 3, Cloudflare te donnera les bons nameservers. Voici comment :

1. Va sur **https://dash.cloudflare.com/**
2. Connecte-toi (ou crée un compte si tu n'en as pas)
3. Clique sur **"Ajouter un site"**
4. Saisis **elekio.fr** et clique sur **"Ajouter"**
5. Cloudflare scanne tes DNS (prends les réglages par défaut)
6. Cloudflare te donnera **DEUX serveurs DNS** (qui ressemblent à `xxx.ns.cloudflare.com`)
7. **Note ces 2 serveurs** — tu les mettras dans OVH (étape 3)

### Étape 5 — Attendre la propagation
- ⏳ Compte **24 à 48h maximum**
- Pendant ce temps, le site reste accessible sur `elekio.pages.dev`
- Une fois la propagation faite, `https://elekio.fr` affichera ton site

### 🔧 Si tu as un accès Google Domains
Si tu as acheté le domaine sur **Google Domains** (pas OVH) :
1. Va sur **https://domains.google.com/**
2. Connecte-toi
3. Clique sur **elekio.fr**
4. Va dans **"DNS"** → **"Serveurs de noms"**
5. Sélectionne **"Utiliser des serveurs de noms personnalisés"**
6. Ajoute les 2 serveurs Cloudflare
7. Valide

---

## 🔥 Résumé — Ce que je fais

| Tâche | Qui fait |
|-------|:--------:|
| Créer compte Search Console | **Toi** (5 min) |
| Créer compte Google Analytics | **Toi** (5 min) |
| Copier le code de vérification → me l'envoyer | **Toi** |
| J'ajoute les codes dans le site | **Moi** (2 min) |
| Modifier les serveurs DNS OVH | **Toi** (3 min) |
| Configurer Cloudflare | **Toi** (5 min) |

---

**Besoin d'aide pour une étape ?** Dis-moi où tu bloques, je te guide en direct ! 💪
