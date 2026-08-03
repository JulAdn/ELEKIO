#!/usr/bin/env python3
"""Correctifs SEO elekio — lot « vrais problèmes » actés avec Julian (03/08/2026).
NAP complet, titles, FAQ home, canonicals/og/sitemap propres, maillage villes,
liens autorité, alt images, WebP + preload, horaires urgences.
"""
import re, os, glob, sys
from PIL import Image

ROOT = "/workspace/1_Projects/site-web"
STREET = "625 route de Saint-Lieux"
RAPPORT = []

def log(msg):
    print(msg)
    RAPPORT.append(msg)

def read(f):
    with open(f, encoding="utf-8") as fh: return fh.read()

def write(f, s):
    with open(f, "w", encoding="utf-8") as fh: fh.write(s)

files = sorted(p for p in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True) if "_site" not in p)
assert len(files) == 26, f"attendu 26 pages, trouvé {len(files)}"
root_files = [f for f in files if f.count("/") == 4]          # /workspace/1_Projects/site-web/X.html
sub_files  = [f for f in files if f not in root_files]        # blog/ et villes/

# ============ 1. NAP : adresse + horaires footer (toutes pages) ============
n_addr = n_hours = 0
for f in files:
    s = read(f)
    a = '<li><span class="fc-icon">📍</span> Saint-Sulpice-la-Pointe, 81370</li>'
    h = '<li><span class="fc-icon">🕐</span> Lun-Sam 8h-20h</li>'
    n_addr += s.count(a)
    n_hours += s.count(h)
    s = s.replace(a, f'<li><span class="fc-icon">📍</span> {STREET}, 81370 Saint-Sulpice-la-Pointe</li>')
    s = s.replace(h, '<li><span class="fc-icon">🕐</span> Lun-Sam 8h-20h · Urgences 24h/24</li>')
    write(f, s)
log(f"[1] NAP footer : {n_addr} lignes adresse + {n_hours} lignes horaires modifiées")

# ============ 2. NAP : streetAddress dans tous les schémas ============
n_schema = 0
for f in files:
    s = read(f)
    s2 = s.replace('"streetAddress":"Résidence Le Clos des Castellanes, 625 route de Saint-Lieux"',
                   f'"streetAddress":"{STREET}"')
    s2 = s2.replace('"streetAddress": "Résidence Le Clos des Castellanes, 625 route de Saint-Lieux"',
                    f'"streetAddress": "{STREET}"')
    # forme compacte sans streetAddress
    s2 = s2.replace('"address":{"@type":"PostalAddress","addressLocality":"Saint-Sulpice-la-Pointe"',
                    f'"address":{{"@type":"PostalAddress","streetAddress":"{STREET}","addressLocality":"Saint-Sulpice-la-Pointe"')
    # forme pretty sans streetAddress
    s2 = s2.replace('"@type": "PostalAddress",\n      "addressLocality": "Saint-Sulpice-la-Pointe",',
                    f'"@type": "PostalAddress",\n      "streetAddress": "{STREET}",\n      "addressLocality": "Saint-Sulpice-la-Pointe",')
    if s2 != s:
        n_schema += 1
        write(f, s2)
log(f"[2] Schémas avec streetAddress : {n_schema} fichier(s) modifié(s)")

# ============ 3. URLs propres : canonical, og:url, JSON-LD ============
n_canon = n_og = n_json = 0
for f in files:
    s = read(f)
    orig = s
    s = s.replace('https://www.elekio.fr/about.html', 'https://www.elekio.fr/a-propos/')
    def clean_url(m):
        return m.group(1)
    s = re.sub(r'(https://www\.elekio\.fr/[a-z0-9/_-]+)\.html', clean_url, s)
    n_canon += len(re.findall(r'rel="canonical" href="https://www\.elekio\.fr/[^"]+"', s))
    n_og   += len(re.findall(r'og:url" content="https://www\.elekio\.fr/[^"]+"', s))
    n_json += len(re.findall(r'https://www\.elekio\.fr/(?!$)[^"\s]*\.html', orig))  # résidus éventuels
    if s != orig:
        write(f, s)
log(f"[3] Canonicals/og:url/JSON-LD nettoyés (canonical présents: {n_canon}, og:url: {n_og}, résidus .html avant: {n_json})")

# ============ 4. Liens internes href *.html -> propres ============
KNOWN = {"services","contact","index","blog","realisations","faq","avis","mentions-legales","cgv","about","a-propos","merci"}
n_href = 0
for f in files:
    s = read(f)
    orig = s
    def fix_href(m):
        global n_href
        prefix, slug = m.group(1), m.group(2)
        if slug == "about":
            n_href += 1; return f'href="{prefix}a-propos"'
        if slug == "index":
            n_href += 1; return 'href="/"' if prefix == "" else 'href="../"'
        if slug in KNOWN or slug.startswith("villes/") or slug.startswith("blog/"):
            n_href += 1; return f'href="{prefix}{slug}"'
        return m.group(0)  # inconnu : inchangé
    s = re.sub(r'href="(\.\./)?((?:villes|blog)/[a-z0-9-]+|[a-z0-9-]+)\.html', fix_href, s)
    if s != orig:
        write(f, s)
log(f"[4] Liens internes .html -> URLs propres : {n_href} remplacés")

# ============ 5. ALT images + src WebP ============
n_alt = n_src = 0
for f in files:
    s = read(f)
    n_alt += s.count('alt="Elekio"')
    s = s.replace('alt="Elekio"', 'alt="Elekio — électricien à Saint-Sulpice-la-Pointe (Tarn 81)"')
    n_src += s.count('logo-elekio-header.png')
    s = s.replace('src="logo-elekio-header.png"', 'src="logo-elekio-header.webp"')
    s = s.replace('src="../logo-elekio-header.png"', 'src="../logo-elekio-header.webp"')
    write(f, s)
log(f"[5] ALT images : {n_alt} | src WebP : {n_src}")

# ============ 6. Preload logo (LCP) ============
n_pre = 0
for f in files:
    s = read(f)
    if 'rel="preload" as="image" href="/logo-elekio-header.webp"' in s:
        continue
    s2 = s.replace('<link rel="manifest" href="https://www.elekio.fr/site.webmanifest">',
                   '<link rel="manifest" href="https://www.elekio.fr/site.webmanifest">\n'
                   '<link rel="preload" as="image" href="/logo-elekio-header.webp">')
    if s2 != s:
        n_pre += 1
        write(f, s2)
log(f"[6] Preload LCP ajouté : {n_pre} pages")

# ============ 7. Home : title, description, og:title, caption carte ============
home = os.path.join(ROOT, "index.html")
s = read(home)
subs = [
    ("<title>Elekio — Électricien Tarn 81 | Dépannage 4h</title>",
     "<title>Électricien Saint-Sulpice-la-Pointe (81) — Elekio | Dépannage 4h</title>"),
    ('<meta name="description" content="Électricien Tarn 81 — Saint-Sulpice. Dépannage urgence 4h, installation neuve, rénovation aux normes. Devis gratuit 24h. Garantie décennale. 06 80 50 67 09">',
     '<meta name="description" content="Électricien à Saint-Sulpice-la-Pointe (Tarn 81). Dépannage urgence 4h, installation neuve, rénovation aux normes. Devis gratuit 24h. Tél. 06 80 50 67 09">'),
    ('<meta property="og:title" content="Électricien Tarn (81) — Elekio | Dépannage 4h & Devis gratuit">',
     '<meta property="og:title" content="Électricien Saint-Sulpice-la-Pointe (81) — Elekio | Dépannage 4h & Devis gratuit">'),
    ("📍 ELEKIO — Saint-Sulpice-la-Pointe (81370) · Intervention dans un rayon de 2h",
     f"📍 ELEKIO — {STREET}, 81370 Saint-Sulpice-la-Pointe · Intervention dans un rayon de 2h"),
]
n_home = 0
for old, new in subs:
    if old in s:
        s = s.replace(old, new); n_home += 1
    else:
        log(f"  !! home : introuvable -> {old[:60]}")
write(home, s)
log(f"[7] Home title/desc/og/caption : {n_home}/4 remplacés")

# ============ 8. Home : section FAQ + schéma FAQPage ============
FAQ_BLOCK = """
<!-- ===== SECTION FAQ ACCUEIL ===== -->
<section class="section section-faq" id="faq">
  <div class="container">
    <div class="section-header animate-fade-up">
      <span class="section-label">Questions fréquentes</span>
      <h2>Vos questions sur <span class="highlight">nos services</span></h2>
      <p>Les réponses aux questions qu'on nous pose le plus souvent, en toute transparence.</p>
    </div>
    <div class="faq-grid">
      <div class="faq-item animate-fade-up delay-1">
        <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">
          <span>Intervenez-vous rapidement en cas d'urgence ?</span>
          <span class="faq-toggle">+</span>
        </button>
        <div class="faq-a">
          <p>Oui. Dépannage d'urgence sous <strong>4h</strong> dans le Tarn (81) et ses alentours, <strong>7j/7</strong> — y compris week-end et jours fériés pour les urgences. En cas de panne, disjoncteur qui saute ou odeur suspecte, appelez directement le <strong><a href="tel:0680506709" style="color:var(--copper);font-weight:700">06 80 50 67 09</a></strong>.</p>
        </div>
      </div>
      <div class="faq-item animate-fade-up delay-2">
        <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">
          <span>Le devis est-il gratuit ?</span>
          <span class="faq-toggle">+</span>
        </button>
        <div class="faq-a">
          <p>Oui, le devis est <strong>gratuit et sans engagement</strong>, avec une réponse sous 24h. Il est détaillé poste par poste, et le déplacement pour l'évaluation est offert.</p>
        </div>
      </div>
      <div class="faq-item animate-fade-up delay-3">
        <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">
          <span>Quelles zones couvrez-vous ?</span>
          <span class="faq-toggle">+</span>
        </button>
        <div class="faq-a">
          <p>Basé à <strong>Saint-Sulpice-la-Pointe (81370)</strong>, j'interviens dans tout le Tarn (81) : Lavaur, Albi, Castres, Gaillac, Graulhet, Mazamet… ainsi que <strong>Toulouse et sa périphérie</strong> (31) et les départements voisins (82, 12, 34).</p>
        </div>
      </div>
      <div class="faq-item animate-fade-up delay-1">
        <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">
          <span>Vos interventions sont-elles garanties ?</span>
          <span class="faq-toggle">+</span>
        </button>
        <div class="faq-a">
          <p>Oui. Elekio est assuré en <strong>responsabilité civile professionnelle et décennale</strong>, et chaque installation est réalisée selon la norme <strong>NF C 15-100</strong>.</p>
        </div>
      </div>
      <div class="faq-item animate-fade-up delay-2">
        <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">
          <span>Puis-je vous joindre le week-end ?</span>
          <span class="faq-toggle">+</span>
        </button>
        <div class="faq-a">
          <p>Pour les <strong>urgences, oui</strong> : le dépannage d'urgence fonctionne 7j/7. Pour les devis et travaux programmés, je réponds du lundi au samedi de 8h à 20h.</p>
        </div>
      </div>
    </div>
    <div style="text-align:center;margin-top:32px">
      <a href="/faq" class="btn btn-copper">Voir toutes les questions fréquentes →</a>
    </div>
  </div>
</section>
"""
ANCHOR = '<section class="section-cta animate-fade-up">'
if ANCHOR in s:
    s = s.replace(ANCHOR, FAQ_BLOCK + "\n" + ANCHOR, 1)
    log("[8] Section FAQ insérée sur la home")
else:
    log("  !! ANCHOR CTA introuvable sur la home")

FAQ_JSONLD = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type":"Question","name":"Intervenez-vous rapidement en cas d'urgence ?","acceptedAnswer":{"@type":"Answer","text":"Oui. Dépannage d'urgence sous 4h dans le Tarn (81) et ses alentours, 7j/7, y compris week-end et jours fériés pour les urgences."}},
    {"@type":"Question","name":"Le devis est-il gratuit ?","acceptedAnswer":{"@type":"Answer","text":"Oui, le devis est gratuit et sans engagement, avec une réponse sous 24h."}},
    {"@type":"Question","name":"Quelles zones couvrez-vous ?","acceptedAnswer":{"@type":"Answer","text":"Basé à Saint-Sulpice-la-Pointe (81370), j'interviens dans tout le Tarn (81) : Lavaur, Albi, Castres, Gaillac, Graulhet, Mazamet, ainsi que Toulouse et sa périphérie (31) et les départements voisins (82, 12, 34)."}},
    {"@type":"Question","name":"Vos interventions sont-elles garanties ?","acceptedAnswer":{"@type":"Answer","text":"Oui. Elekio est assuré en responsabilité civile professionnelle et décennale, et chaque installation est réalisée selon la norme NF C 15-100."}},
    {"@type":"Question","name":"Puis-je vous joindre le week-end ?","acceptedAnswer":{"@type":"Answer","text":"Pour les urgences, oui : le dépannage d'urgence fonctionne 7j/7. Pour les devis et travaux programmés, du lundi au samedi de 8h à 20h."}}
  ]
}
</script>
"""
s = read(home)
if "FAQPage" not in s:
    s = s.replace("</head>", FAQ_JSONLD + "\n</head>", 1)
    log("[8b] Schéma FAQPage ajouté sur la home")
else:
    log("[8b] FAQPage déjà présent, inchangé")
write(home, s)

# ============ 9. Maillage : villes proches sur les pages villes ============
VILLES = {
    "albi": "Albi", "balma": "Balma", "castanet": "Castanet-Tolosan", "castres": "Castres",
    "gaillac": "Gaillac", "graulhet": "Graulhet", "lavaur": "Lavaur", "lunion": "L'Union",
    "mazamet": "Mazamet", "montauban": "Montauban", "ramonville": "Ramonville-Saint-Agne",
    "saint-orens": "Saint-Orens-de-Gameville", "saint-sulpice": "Saint-Sulpice-la-Pointe",
    "toulouse": "Toulouse",
}
PROCHES = {
    "albi": ["castres", "gaillac", "graulhet", "mazamet"],
    "balma": ["toulouse", "lunion", "saint-orens", "ramonville"],
    "castanet": ["ramonville", "toulouse", "saint-orens", "balma"],
    "castres": ["albi", "mazamet", "graulhet", "toulouse"],
    "gaillac": ["albi", "graulhet", "lavaur", "saint-sulpice"],
    "graulhet": ["castres", "gaillac", "lavaur", "saint-sulpice"],
    "lavaur": ["saint-sulpice", "gaillac", "graulhet", "toulouse"],
    "lunion": ["toulouse", "balma", "saint-orens", "castanet"],
    "mazamet": ["castres", "albi", "graulhet", "toulouse"],
    "montauban": ["toulouse", "saint-sulpice", "lavaur", "gaillac"],
    "ramonville": ["toulouse", "castanet", "balma", "saint-orens"],
    "saint-orens": ["toulouse", "balma", "lunion", "castanet"],
    "saint-sulpice": ["lavaur", "gaillac", "toulouse", "albi"],
    "toulouse": ["balma", "lunion", "ramonville", "castanet"],
}
n_maillage = 0
for slug, name in VILLES.items():
    f = os.path.join(ROOT, "villes", f"electricien-{slug}.html")
    if not os.path.exists(f):
        log(f"  !! page ville manquante : {slug}")
        continue
    s = read(f)
    if "Aussi disponible à" in s:
        log(f"  -- {slug} : maillage déjà présent, ignoré")
        continue
    links = "".join(
        f'      <a href="../villes/electricien-{p}.html" class="zone-ville"><span class="pin">📍</span> {VILLES[p]}</a>\n'
        for p in PROCHES[slug]
    )
    block = f"""
<!-- ===== MAILLAGE VILLES PROCHES ===== -->
<section class="section section-local">
  <div class="container">
    <div class="section-header animate-fade-up">
      <span class="section-label">À proximité</span>
      <h2>Électricien aussi disponible à <span class="highlight">proximité</span></h2>
      <p>Vous cherchez un électricien près de chez vous ? Elekio intervient également à :</p>
    </div>
    <div class="zone-grid">
{links}    </div>
  </div>
</section>
"""
    anchor = '<section class="section-cta">'
    if anchor in s:
        s = s.replace(anchor, block + "\n" + anchor, 1)
        write(f, s)
        n_maillage += 1
    else:
        log(f"  !! {slug} : anchor CTA introuvable")
log(f"[9] Maillage villes proches : {n_maillage} pages")

# ============ 10. Liens sortants autorité ============
blog = os.path.join(ROOT, "blog", "installation-electrique-aux-normes-8-signes.html")
s = read(blog)
LINK_CU = ('<p style="font-size:1.05rem;color:var(--gray-600);line-height:1.8;margin-bottom:20px">'
           'Après une mise en conformité, l\'<strong>attestation de conformité</strong> est visée par le '
           '<a href="https://www.consuel.com/" target="_blank" rel="noopener">CONSUEL</a>, organisme agréé par l\'État '
           '— c\'est le document officiel qui atteste que votre installation respecte la norme <strong>NF C 15-100</strong>.</p>')
ANCHOR_BLOG = "Voici comment faire le point chez vous.</p>"
if "consuel.com" not in s:
    if ANCHOR_BLOG in s:
        s = s.replace(ANCHOR_BLOG, ANCHOR_BLOG + "\n    " + LINK_CU, 1)
        write(blog, s)
        log("[10a] Lien CONSUEL ajouté dans l'article blog")
    else:
        log("  !! anchor blog introuvable")
else:
    log("[10a] Lien CONSUEL déjà présent")

faq = os.path.join(ROOT, "faq.html")
s = read(faq)
LINK_DECRET = ('<a href="https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000696656" target="_blank" rel="noopener">'
               'décret n° 72-1120 du 14 décembre 1972</a>')
ANCHOR_FAQ = "(décret n° 72-1120 du 14 décembre 1972)"
if "legifrance.gouv.fr" not in s:
    n = s.count(ANCHOR_FAQ)
    if n:
        s = s.replace(ANCHOR_FAQ, LINK_DECRET, 1)  # seulement la 1re occurrence (visible ou schema)
        write(faq, s)
        log(f"[10b] Lien Légifrance ajouté dans la FAQ ({n} occurrences de l'ancre, 1 liée)")
    else:
        log("  !! ancre décret introuvable dans faq.html")
else:
    log("[10b] Lien Légifrance déjà présent")

# ============ 11. WebP du logo ============
src_png = os.path.join(ROOT, "logo-elekio-header.png")
dst_webp = os.path.join(ROOT, "logo-elekio-header.webp")
img = Image.open(src_png).convert("RGBA")
img.save(dst_webp, "WEBP", quality=80, method=6)
s_p = os.path.getsize(src_png); s_w = os.path.getsize(dst_webp)
log(f"[11] logo-elekio-header.webp créé : {s_p}o -> {s_w}o ({(100*s_w//s_p)}%)")

# ============ 12. Sitemap propre ============
urls = [
    ("https://www.elekio.fr/", "1.0"),
    ("https://www.elekio.fr/services", "0.9"),
    ("https://www.elekio.fr/realisations", "0.8"),
    ("https://www.elekio.fr/faq", "0.8"),
    ("https://www.elekio.fr/blog", "0.8"),
    ("https://www.elekio.fr/blog/installation-electrique-aux-normes-8-signes", "0.7"),
    ("https://www.elekio.fr/a-propos/", "0.7"),
    ("https://www.elekio.fr/contact", "0.9"),
    ("https://www.elekio.fr/mentions-legales", "0.3"),
    ("https://www.elekio.fr/avis", "0.8"),
]
ville_prio = {"saint-sulpice": "0.8", "toulouse": "0.8", "montauban": "0.8",
              "albi": "0.7", "castres": "0.7", "lavaur": "0.7", "mazamet": "0.7",
              "graulhet": "0.7", "gaillac": "0.7", "lunion": "0.6", "balma": "0.6",
              "ramonville": "0.6", "castanet": "0.6", "saint-orens": "0.6"}
for slug in sorted(ville_prio, key=lambda x: ville_prio[x], reverse=True):
    urls.append((f"https://www.elekio.fr/villes/electricien-{slug}", ville_prio[slug]))
xml = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u, p in urls:
    xml.append("  <url>")
    xml.append(f"    <loc>{u}</loc>")
    xml.append("    <lastmod>2026-08-03</lastmod>")
    xml.append("    <changefreq>monthly</changefreq>")
    xml.append(f"    <priority>{p}</priority>")
    xml.append("  </url>")
xml.append("</urlset>")
write(os.path.join(ROOT, "sitemap.xml"), "\n".join(xml) + "\n")
log(f"[12] sitemap.xml réécrit : {len(urls)} URLs propres")

# ============ Vérifications finales ============
errs = []
for f in files:
    s = read(f)
    if not s.rstrip().endswith("</html>"):
        errs.append(f"FIN INVALID : {f}")
    if "favicon.png" not in s and "site.webmanifest" not in s:
        errs.append(f"favicon/manifest manquant : {f}")
res = read(os.path.join(ROOT, "index.html"))
if "FAQPage" not in res: errs.append("FAQPage absent home")
if 'alt="Elekio"' in res: errs.append("alt logo non remplacé")
if "section-cta" not in res: errs.append("structure home cassée")
for f in files:
    s = read(f)
    if ".html" in re.search(r'rel="canonical" href="[^"]+"', s).group(0) if re.search(r'rel="canonical" href="[^"]+"', s) else False:
        errs.append(f"canonical .html restant : {f}")
print()
if errs:
    log("=== ERREURS ===")
    for e in errs: log("  !! " + e)
    sys.exit(1)
log("=== VÉRIFS OK : 26 pages intègres, canonicals propres, home FAQ/FAQPage OK ===")
