# -*- coding: utf-8 -*-
"""Génère les pages service × ville, les pages « Paysagiste à <ville> »,
la page Débroussaillage, et met à jour la navigation, les deux numéros
de téléphone et le pied de page de toutes les pages.

Rejouable : python3 _build/build.py (depuis la racine du site)."""
import html, json, re, os, sys

sys.path.insert(0, os.path.dirname(__file__))
from contenu_villes import VILLES, ORDRE_VILLES, SERVICES, ORDRE_SERVICES, COMBOS, DEBROUSSAILLAGE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BASE = "https://artisan-david-s.pages.dev/"
NOM = "Artisan David S"
T1 = dict(nom="Noé", tel="+33604417382", aff="06 04 41 73 82")
T2 = dict(nom="David", tel="+33786821293", aff="07 86 82 12 93")
E = html.escape

def lire(f): return open(f, encoding="utf-8").read()
def ecrire(f, t): open(f, "w", encoding="utf-8").write(t)

PHONE_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 010 1.18 2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>'
CHECK_SVG = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
DEVIS_SVG = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>'

def page_combo(s, v): return f"{'elagage' if s=='elagage' else s}-{v}.html"
def page_hub(v): return f"paysagiste-{v}.html"

# ── Blocs communs ─────────────────────────────────────────────────────────
SERVICES_MENU = [
 ("creation-jardin.html", "Création et conception de jardins"),
 ("amenagement-paysager.html", "Aménagement paysager complet"),
 ("entretien-espaces-verts.html", "Entretien d'espaces verts"),
 ("elagage-abattage.html", "Élagage et abattage d'arbres"),
 ("taille-de-haies.html", "Taille de haies"),
 ("debroussaillage-terrain.html", "Débroussaillage et remise en état"),
 ("nettoyage-terrasses.html", "Nettoyage de terrasses et dallages"),
]

def mega(prefix=""):
    cols = []
    for v in ORDRE_VILLES:
        V = VILLES[v]
        items = [f'<li><a href="{page_hub(v)}" class="mega-all">Paysagiste {E(V["dans"])} — tout voir</a></li>']
        items += [f'<li><a href="{page_combo(s, v)}">{E(SERVICES[s]["court"])}</a></li>' for s in ORDRE_SERVICES]
        cols.append(f'<div class="mega-col"><a href="{page_hub(v)}" class="mega-head nav-toggle">{E(V["nom"])} <span class="mega-cp">{V["cp"]}</span></a><ul class="mega-list">{"".join(items)}</ul></div>')
    cols.append('<div class="mega-foot"><a href="zones-intervention.html">Toutes nos zones d\'intervention dans le Morbihan →</a></div>')
    return f'<div class="mega">{"".join(cols)}</div>'

AC = ' aria-current="page"'
def nav(courante, accueil=False):
    ancre = "" if accueil else "index.html"
    subs = "".join(f'<li><a href="{u}"{AC if u == courante else ""}>{E(t)}</a></li>' for u, t in SERVICES_MENU)
    logo_href = "#hero" if accueil else "index.html"
    return f'''<nav id="nav">
  <a href="{logo_href}" class="nav-logo"{' id="navLogo"' if accueil else ''}>
    <img class="logo-blanc" src="images/logo-blanc.webp" alt="" aria-hidden="true" width="440" height="330" />
    <img class="logo-couleur" src="images/logo.webp" alt="Logo {NOM}" width="440" height="330" />
    <span class="nav-logo-text{'' if accueil else ' brand-name'}"{' id="navLogoName"' if accueil else ''}>{NOM}</span>
  </a>
  <ul class="nav-links" id="navLinks">
    <li class="has-sub"><a href="{ancre}#services" class="nav-toggle">Services</a>
      <ul class="sub-links">{subs}</ul>
    </li>
    <li class="has-sub has-mega"><a href="zones-intervention.html" class="nav-toggle">Villes</a>{mega()}</li>
    <li class="nav-opt"><a href="{ancre}#apropos">À propos</a></li>
    <li class="nav-opt"><a href="{ancre}#galerie">Réalisations</a></li>
    <li><a href="{ancre}#avis">Avis</a></li>{'<li id="horNavLi" style="display:none"><a href="#horaires">Horaires</a></li>' if accueil else ''}
    <li><a href="tel:{T1["tel"]}" class="phone-link">{T1["aff"].replace(" ", "&nbsp;")}</a></li>
    <li><a href="{ancre}#devis" class="nav-cta">{DEVIS_SVG}Devis</a></li>
  </ul>
  <button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
</nav>'''

def boutons_tel():
    return (f'<a href="tel:{T1["tel"]}" class="btn btn-primary phone-link">{PHONE_SVG}<span class="phone-text">{T1["aff"]}</span></a>'
            f'<a href="tel:{T2["tel"]}" class="btn btn-ghostw phone2-link">{PHONE_SVG}<span class="phone2-text">{T2["aff"]}</span></a>')

NOTE_TEL = '<p class="tel-note">Pas de réponse au premier numéro ? Appelez le second, l\'un de nous décroche toujours.</p>'

def maillage():
    cols = []
    for v in ORDRE_VILLES:
        V = VILLES[v]
        lis = "".join(f'<li><a href="{page_combo(s, v)}">{E(SERVICES[s]["court"])} {E(V["nom"])}</a></li>' for s in ORDRE_SERVICES)
        cols.append(f'<div><a class="fm-head" href="{page_hub(v)}">Paysagiste {E(V["nom"])}</a><ul>{lis}</ul></div>')
    return f'<div class="footer-maillage">{"".join(cols)}</div>'

def footer():
    svcs = "".join(f'<a href="{u}">{E(t)}</a>' for u, t in [
        ("creation-jardin.html", "Création de jardins"), ("amenagement-paysager.html", "Aménagement paysager"),
        ("entretien-espaces-verts.html", "Entretien d'espaces verts"), ("elagage-abattage.html", "Élagage et abattage"),
        ("taille-de-haies.html", "Taille de haies"), ("debroussaillage-terrain.html", "Débroussaillage"),
        ("nettoyage-terrasses.html", "Nettoyage de terrasses")])
    PIN = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>'
    return f'''<footer>
  <div class="footer-grid">
    <div>
      <img class="footer-logo" src="images/logo-blanc.webp" alt="Logo {NOM} — paysagiste et élagueur dans le Morbihan" loading="lazy" width="440" height="330" />
      <span class="footer-brand brand-name">{NOM}</span>
      <p class="footer-desc">Paysagiste à Plouhinec, {NOM} crée, aménage et entretient vos jardins et espaces verts dans tout le Morbihan.</p>
    </div>
    <div class="footer-col"><h4>Nos services</h4>{svcs}</div>
    <div class="footer-col"><h4>Navigation</h4>
      <a href="index.html">Accueil</a><a href="zones-intervention.html">Zones d'intervention</a><a href="index.html#apropos">À propos</a><a href="index.html#galerie">Réalisations</a><a href="index.html#avis">Avis</a><a href="index.html#faq">FAQ</a>
    </div>
    <div class="footer-col"><h4>Contact</h4>
      <span>{PIN}<span class="brand-ville">10 Ldt Kerjean, 56680 Plouhinec</span></span>
      <a href="tel:{T1["tel"]}" class="phone-link">{PHONE_SVG}<span class="phone-text">{T1["aff"]}</span></a>
      <a href="tel:{T2["tel"]}" class="phone2-link">{PHONE_SVG}<span class="phone2-text">{T2["aff"]}</span></a>
      <span style="font-size:.78rem;opacity:.75">Si l'un ne répond pas, appelez l'autre.</span>
      <a href="index.html#devis">{DEVIS_SVG}Demander un devis gratuit</a>
    </div>
  </div>
  {maillage()}
  <div class="footer-bottom">© <span class="brand-annee">2026</span> <span class="brand-name">{NOM}</span> · Paysagiste à Plouhinec, Lorient, Vannes, Auray, Hennebont, Lanester, Carnac et dans tout le Morbihan · Tous droits réservés</div>
</footer>'''

ASSETS = '  <link rel="stylesheet" href="assets/villes.css?v=2" />\n  <script defer src="assets/villes.js?v=2"></script>\n'

TPL = lire("elagage-abattage.html")
HEAD_FONTS = re.search(r'  <link rel="icon".*?<script defer src="assets/pages\.js\?v=\d+"></script>\n', TPL, re.S).group(0)
REASSUR = re.search(r'<section class="reassur">.*?</section>', TPL, re.S).group(0).replace("Garantie décennale", "Artisan local")

def extrait(f, debut):
    t = lire(f)
    m = re.search(re.escape(debut) + r'.*', t)
    return m.group(0) if m else ""

def faq_items(f):
    t = extrait(f, '<ul class="faq-list">')
    return re.findall(r'<li class="faq-item">.*?</li>', t)

def faq_li(q, a):
    return f'<li class="faq-item"><button class="faq-q" type="button">{E(q)}<span class="ic"></span></button><div class="faq-a"><p>{E(a)}</p></div></li>'

def faq_json(li_list):
    out = []
    for li in li_list:
        q = html.unescape(re.sub(r"<.*?>", "", re.search(r'type="button">(.*?)<span', li).group(1)))
        a = html.unescape(re.sub(r"<.*?>", "", re.search(r'<div class="faq-a"><p>(.*?)</p>', li).group(1)))
        out.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    return out

def ld(o): return '  <script type="application/ld+json">\n' + json.dumps(o, ensure_ascii=False, indent=2) + '\n  </script>\n'

# Contenu de service repris des pages existantes (avant toute modification)
SVC_BLOCS = {}
for s in ORDRE_SERVICES:
    f = SERVICES[s]["page"]
    if s == "debroussaillage":
        SVC_BLOCS[s] = dict(
            checks='<div class="check-grid">' + "".join(f'<div class="check">{CHECK_SVG}<div><b>{E(b)}</b><span>{E(x)}</span></div></div>' for b, x in DEBROUSSAILLAGE["checks"]) + '</div>',
            steps='<div class="steps">' + "".join(f'<div class="step fade"><span class="step-no">0{i+1}</span><h3>{E(a)}</h3><p>{E(b)}</p></div>' for i, (a, b) in enumerate(DEBROUSSAILLAGE["steps"])) + '</div>',
            faqs=[faq_li(q, a) for q, a in DEBROUSSAILLAGE["faq"]])
    else:
        SVC_BLOCS[s] = dict(
            checks=re.search(r'<div class="check-grid">.*?</div></div></div>(?=\n)', lire(f)).group(0),
            steps=re.search(r'<div class="steps">.*?</div></div>(?=\n)', lire(f)).group(0),
            faqs=faq_items(f))

def page(fichier, titre, desc, img, eyebrow, h1, accroche, fil, corps, schemas):
    url = BASE + fichier
    fil_html = "".join(f'<li><a href="{u}">{E(t)}</a></li>' for u, t in fil) + f'<li aria-current="page">{E(fil_courant(h1))}</li>'
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement":
          [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE}] +
          [{"@type": "ListItem", "position": i + 2, "name": t, "item": BASE + u} for i, (u, t) in enumerate(fil[1:])] +
          [{"@type": "ListItem", "position": len(fil) + 1, "name": fil_courant(h1), "item": url}]}
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{E(titre)} | {NOM}</title>
  <meta name="description" content="{E(desc)}" />
  <link rel="canonical" href="{url}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="theme-color" content="#3f6b4a" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="fr_FR" />
  <meta property="og:site_name" content="{NOM}" />
  <meta property="og:title" content="{E(titre)} | {NOM}" />
  <meta property="og:description" content="{E(desc)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{BASE}images/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
{HEAD_FONTS}{ASSETS}{"".join(ld(s) for s in schemas)}{ld(bc)}</head>
<body>
{nav(fichier)}

<header class="page-hero" style="background-image:url('{img}')">
  <div class="wrap">
    <span class="eyebrow">{E(eyebrow)}</span>
    <h1>{E(h1)}</h1>
    <p>{E(accroche)}</p>
    <div class="hero-btns">
      {boutons_tel()}
      <a href="index.html#devis" class="btn btn-ghostw">Devis gratuit</a>
    </div>
    {NOTE_TEL}
  </div>
</header>

<nav class="breadcrumb" aria-label="Fil d'Ariane">
  <div class="wrap"><ol>{fil_html}</ol></div>
</nav>

{REASSUR}
{corps}
<section class="sec cta">
  <div class="wrap">
    <h2 class="h2">Un devis gratuit, sans engagement</h2>
    <p>Appelez-nous : nous nous déplaçons gratuitement pour voir votre terrain et vous remettre un prix clair.</p>
    <div class="btns">
      {boutons_tel()}
      <a href="index.html#devis" class="btn btn-ghostw">Demander un devis</a>
    </div>
    {NOTE_TEL}
  </div>
</section>
{footer()}
</body>
</html>
'''

def fil_courant(h1): return h1

PROVIDER = {"@type": "LandscapeArchitect", "@id": BASE + "#business", "name": NOM, "telephone": T1["tel"], "url": BASE}

# ── Pages service × ville ─────────────────────────────────────────────────
generees = []
for s in ORDRE_SERVICES:
    S = SERVICES[s]
    for v in ORDRE_VILLES:
        V = VILLES[v]
        intro, (fq, fa) = COMBOS[(s, v)]
        f = page_combo(s, v)
        fmt = dict(v=V["nom"], cp=V["cp"], dans=V["dans"])
        h1 = S["h1"].format(**fmt)
        autres_svc = "".join(f'<a href="{page_combo(x, v)}"><b>{E(SERVICES[x]["nom"])}</b><span>{E(SERVICES[x]["nom"])} {E(V["dans"])} et alentours.</span><em>Découvrir →</em></a>' for x in ORDRE_SERVICES if x != s)
        autres_villes = "".join(f'<a class="ville-chip" href="{page_combo(s, w)}">{E(S["court"])} {E(VILLES[w]["nom"])}</a>' for w in ORDRE_VILLES if w != v)
        faqs = [faq_li(fq, fa)] + SVC_BLOCS[s]["faqs"][:2]
        corps = f'''
<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">{E(S["nom"])} · {E(V["nom"])}</span>
      <h2 class="h2">{E(S["nom"])} {E(V["dans"])} et alentours</h2>
    </div>
    <div class="prose"><p>{E(intro)}</p><p>Installés à Plouhinec, nous intervenons {E(V["dans"])} ({V["cp"]}) avec tout le matériel nécessaire. Le déplacement pour le devis est gratuit, et le prix est fixé avant le début du chantier.</p></div>
    <div class="local-box">
      <h3>Nos interventions {E(V["dans"])}</h3>
      <p>{E(V["contexte"])}</p>
      <div class="local-facts"><div><b>Accès</b><span>{E(V["acces"])}</span></div><div><b>Jardins</b><span>{E(V["jardins"])}</span></div><div><b>À savoir</b><span>{E(V["attention"])}</span></div></div>
    </div>
    {SVC_BLOCS[s]["checks"]}
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Comment ça se passe</span>
      <h2 class="h2">Le déroulement de votre chantier {E(V["dans"])}</h2>
    </div>
    {SVC_BLOCS[s]["steps"]}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Questions fréquentes</span>
      <h2 class="h2">{E(S["nom"])} {E(V["dans"])} : vos questions</h2>
    </div>
    <ul class="faq-list">{"".join(faqs)}</ul>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Aussi {E(V["dans"])}</span>
      <h2 class="h2">Nos autres services {E(V["dans"])}</h2>
      <p class="lead" style="margin-top:1rem"><a href="{page_hub(v)}" style="color:var(--accent);font-weight:600">Tous nos services de paysagiste {E(V["dans"])} →</a></p>
    </div>
    <div class="city-svc">{autres_svc}</div>
    <div class="villes" style="margin-top:2rem">{autres_villes}</div>
  </div>
</section>
'''
        svc = {"@context": "https://schema.org", "@type": "Service", "serviceType": S["nom"], "name": h1,
               "description": S["desc"].format(**fmt), "url": BASE + f, "provider": PROVIDER,
               "areaServed": {"@type": "City", "name": V["nom"], "address": {"@type": "PostalAddress", "postalCode": V["cp"], "addressRegion": "Morbihan", "addressCountry": "FR"}}}
        faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_json(faqs)}
        ecrire(f, page(f, S["titre"].format(**fmt), S["desc"].format(**fmt), S["img"], f"Paysagiste · {V['nom']} ({V['cp']})",
                       h1, S["accroche"].format(**fmt), [("index.html", "Accueil"), (page_hub(v), f"Paysagiste {V['dans']}")], corps, [svc, faqld]))
        generees.append(f)

# ── Pages « Paysagiste à <ville> » ────────────────────────────────────────
for v in ORDRE_VILLES:
    V = VILLES[v]
    f = page_hub(v)
    cartes = "".join(f'<a href="{page_combo(s, v)}"><b>{E(SERVICES[s]["nom"])}</b><span>{E(SERVICES[s]["accroche"].format(v=V["nom"], cp=V["cp"], dans=V["dans"]))}</span><em>{E(SERVICES[s]["court"])} {E(V["dans"])} →</em></a>' for s in ORDRE_SERVICES)
    autres = "".join(f'<a class="ville-chip" href="{page_hub(w)}">Paysagiste {E(VILLES[w]["nom"])}</a>' for w in ORDRE_VILLES if w != v)
    faqs = [faq_li(q, a) for q, a in V["faq"]]
    corps = f'''
<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Paysagiste · {E(V["nom"])}</span>
      <h2 class="h2">Votre paysagiste {E(V["dans"])}</h2>
    </div>
    <div class="prose">{"".join(f"<p>{p}</p>" for p in V["hub_intro"])}</div>
    <div class="local-box">
      <h3>Travailler {E(V["dans"])}</h3>
      <p>{E(V["contexte"])}</p>
      <div class="local-facts"><div><b>Accès</b><span>{E(V["acces"])}</span></div><div><b>Jardins</b><span>{E(V["jardins"])}</span></div><div><b>À savoir</b><span>{E(V["attention"])}</span></div></div>
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Nos services {E(V["dans"])}</span>
      <h2 class="h2">Ce que nous faisons {E(V["dans"])}</h2>
    </div>
    <div class="city-svc">{cartes}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Questions fréquentes</span>
      <h2 class="h2">Paysagiste {E(V["dans"])} : vos questions</h2>
    </div>
    <ul class="faq-list">{"".join(faqs)}</ul>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Autres villes</span>
      <h2 class="h2">Nous intervenons aussi à…</h2>
    </div>
    <div class="villes">{autres}<a class="ville-chip" href="zones-intervention.html">Toutes nos zones</a></div>
  </div>
</section>
'''
    titre = f"Paysagiste {V['dans']} ({V['cp']}) — élagage, haies, entretien de jardin"
    desc = f"Paysagiste {V['dans']} ({V['cp']}) : élagage et abattage, taille de haies, entretien de jardin, débroussaillage, aménagement paysager. Devis gratuit au 06 04 41 73 82 ou au 07 86 82 12 93."
    lb = {"@context": "https://schema.org", "@type": "Service", "serviceType": "Paysagiste", "name": f"Paysagiste {V['dans']}",
          "description": desc, "url": BASE + f, "provider": PROVIDER, "areaServed": {"@type": "City", "name": V["nom"]}}
    faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_json(faqs)}
    ecrire(f, page(f, titre, desc, "images/hero-bg.jpg", f"Paysagiste · {V['nom']} ({V['cp']})", f"Paysagiste {V['dans']}",
                   f"Élagage, taille de haies, entretien, débroussaillage et aménagement de jardin {V['dans']} et alentours, par une équipe basée à Plouhinec.",
                   [("index.html", "Accueil"), ("zones-intervention.html", "Zones d'intervention")], corps, [lb, faqld]))
    generees.append(f)

# ── Page service Débroussaillage ──────────────────────────────────────────
f = "debroussaillage-terrain.html"
B = SVC_BLOCS["debroussaillage"]
villes_chips = "".join(f'<a class="ville-chip" href="{page_combo("debroussaillage", v)}">Débroussaillage {E(VILLES[v]["nom"])}</a>' for v in ORDRE_VILLES)
corps = f'''
<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Débroussaillage</span>
      <h2 class="h2">Débroussaillage et remise en état de terrain dans le Morbihan</h2>
    </div>
    <div class="prose"><p>Ronces, ajoncs, fougères, lierre, jeunes arbres : en Bretagne, un terrain laissé quelques saisons sans entretien redevient vite une friche. <strong>{NOM}</strong> débroussaille, abat les petits arbres, dessouche et évacue tous les déchets verts, pour vous rendre un terrain propre et utilisable.</p><p>Nous intervenons pour des particuliers qui reprennent un jardin abandonné, des familles qui remettent en état une maison de succession, des propriétaires qui préparent une vente ou une location, et avant un projet de construction. Nous pouvons aussi évacuer les encombrants du jardin en même temps.</p></div>
    {B["checks"]}
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Comment ça se passe</span>
      <h2 class="h2">Le déroulement de votre chantier</h2>
    </div>
    {B["steps"]}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Questions fréquentes</span>
      <h2 class="h2">Débroussaillage : ce qu'on nous demande le plus</h2>
    </div>
    <ul class="faq-list">{"".join(B["faqs"])}</ul>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Zones d'intervention</span>
      <h2 class="h2">Débroussaillage dans tout le Morbihan</h2>
    </div>
    <div class="villes">{villes_chips}<a class="ville-chip" href="zones-intervention.html">Toutes nos zones</a></div>
  </div>
</section>
'''
desc = "Débroussaillage et remise en état de terrain dans le Morbihan : friche, ronces, jardin abandonné, succession, avant vente. Évacuation des déchets verts. Devis gratuit au 06 04 41 73 82."
svc = {"@context": "https://schema.org", "@type": "Service", "serviceType": "Débroussaillage", "name": "Débroussaillage et remise en état de terrain",
       "description": desc, "url": BASE + f, "provider": PROVIDER, "areaServed": {"@type": "AdministrativeArea", "name": "Morbihan"}}
ecrire(f, page(f, "Débroussaillage et remise en état de terrain dans le Morbihan (56)", desc, SERVICES["debroussaillage"]["img"],
               "Paysagiste · Morbihan", "Débroussaillage et remise en état de terrain dans le Morbihan",
               "Terrain en friche, jardin abandonné, succession ou maison à vendre : nous dégageons, dessouchons et évacuons tout.",
               [("index.html", "Accueil"), ("index.html#services", "Nos services")], corps,
               [svc, {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_json(B["faqs"])}]))
generees.append(f)

# ── Mise à jour des pages existantes ──────────────────────────────────────
ANCIENNES = ["amenagement-paysager.html", "creation-jardin.html", "elagage-abattage.html", "entretien-espaces-verts.html",
             "nettoyage-terrasses.html", "taille-de-haies.html", "zones-intervention.html"]
BTN_TEL = re.compile(r'<a href="(?:#|tel:[^"]*)" class="btn btn-primary phone-link">.*?</a>(?:<a href="tel:[^"]*" class="btn btn-ghostw phone2-link">.*?</a>)?', re.S)
for f in ANCIENNES:
    t = lire(f)
    t = re.sub(r'<nav id="nav">.*?</nav>', lambda m: nav(f), t, count=1, flags=re.S)
    t = re.sub(r'<footer>.*?</footer>', lambda m: footer(), t, count=1, flags=re.S)
    t = BTN_TEL.sub(lambda m: boutons_tel(), t)
    t = re.sub(r'\n\s*<p class="tel-note">.*?</p>', '', t)
    t = re.sub(r'(<div class="(?:hero-btns|btns)">.*?</div>)', lambda m: m.group(1) + "\n    " + NOTE_TEL, t, flags=re.S)
    t = t.replace("Garantie décennale", "Artisan local")
    t = t.replace('"telephone": "+33786821293"', f'"telephone": "{T1["tel"]}"')
    t = t.replace("Devis gratuit au 07 86 82 12 93", "Devis gratuit au 06 04 41 73 82")
    if "assets/villes.css" not in t:
        t = re.sub(r'(  <script defer src="assets/pages\.js\?v=\d+"></script>\n)', lambda m: m.group(1) + ASSETS, t, count=1)
    ecrire(f, t)

# Zones d'intervention : liens vers les pages villes
t = lire("zones-intervention.html")
bloc = '<!-- VILLES-GOOGLE-ADS -->'
liens = "".join(f'<a class="ville-chip" href="{page_hub(v)}">Paysagiste {E(VILLES[v]["nom"])}</a>' for v in ORDRE_VILLES)
insert = f'{bloc}<div class="villes" style="margin:1.4rem 0 0">{liens}</div>{bloc}'
if bloc in t:
    t = re.sub(re.escape(bloc) + ".*?" + re.escape(bloc), insert, t, flags=re.S)
else:
    t = re.sub(r'(<section class="sec">\s*<div class="wrap">\s*<div class="sec-head">.*?</div>)', lambda m: m.group(1) + "\n    " + insert, t, count=1, flags=re.S)
ecrire("zones-intervention.html", t)

# ── Accueil ───────────────────────────────────────────────────────────────
t = lire("index.html")
t = re.sub(r'<nav id="nav">.*?</nav>', lambda m: nav("index.html", accueil=True), t, count=1, flags=re.S)
hero_old = re.search(r'(<section id="hero">.*?<div class="hero-btns">)(.*?)(</div>)', t, re.S)
t = t[:hero_old.start(2)] + "\n      " + boutons_tel() + '\n      <a href="#services" class="btn btn-ghostw">Nos services</a>\n    ' + t[hero_old.end(2):]
if 'class="tel-note"' not in t.split('<section id="stats">')[0]:
    t = re.sub(r'(<section id="hero">.*?<div class="hero-btns">.*?</div>)', lambda m: m.group(1) + "\n    " + NOTE_TEL, t, count=1, flags=re.S)
# pied de page : deuxième numéro + maillage villes
t = re.sub(r'(<a href="(?:#|tel:[^"]*)" class="phone-link">.*?<span id="footerTel"> ?</span></a>)(\s*<a href="tel:[^"]*" class="phone2-link">.*?</a>\s*<span class="tel-foot"[^>]*>.*?</span>)*',
           lambda m: m.group(1).replace('href="#"', f'href="tel:{T1["tel"]}"') +
           f'\n      <a href="tel:{T2["tel"]}" class="phone2-link">{PHONE_SVG}<span class="phone2-text">{T2["aff"]}</span></a>\n      <span class="tel-foot" style="font-size:.78rem;opacity:.75">Si l\'un ne répond pas, appelez l\'autre.</span>',
           t, count=1, flags=re.S)
t = re.sub(r'\s*<div class="footer-maillage">.*?</div>(?=\s*<div class="footer-bottom">)', '', t, flags=re.S)
t = t.replace('<div class="footer-bottom">', maillage() + '\n  <div class="footer-bottom">', 1)
t = t.replace('"telephone": "+33786821293"', f'"telephone": "{T1["tel"]}"')
t = re.sub(r'href="#" class="(btn btn-primary )?phone-link"', lambda m: f'href="tel:{T1["tel"]}" class="{m.group(1) or ""}phone-link"', t)
if "assets/villes.css" not in t:
    t = t.replace("</head>", ASSETS + "</head>", 1)
ecrire("index.html", t)

# ── Sitemap ───────────────────────────────────────────────────────────────
pages = ["", "creation-jardin.html", "amenagement-paysager.html", "entretien-espaces-verts.html", "elagage-abattage.html",
         "taille-de-haies.html", "debroussaillage-terrain.html", "nettoyage-terrasses.html", "zones-intervention.html"] + \
        [page_hub(v) for v in ORDRE_VILLES] + [page_combo(s, v) for s in ORDRE_SERVICES for v in ORDRE_VILLES]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f'  <url><loc>{BASE}{p}</loc><changefreq>monthly</changefreq><priority>{"1.0" if not p else ("0.8" if "-" not in p or p.startswith("paysagiste-") else "0.7")}</priority></url>\n' for p in pages) + '</urlset>\n'
ecrire("sitemap.xml", sm)
print(len(generees), "pages générées ;", len(pages), "URL dans le sitemap")
