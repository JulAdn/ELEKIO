#!/usr/bin/env python3
"""
Boucle de validation SEO Elekio → Web Creator
Vérifie l'avancement des instructions, analyse le site, produit des recommandations.
"""
import re
import json
import os
from pathlib import Path

WORKSPACE = Path("/workspace/1_Projects/site-web")
TRACKING = WORKSPACE / "TRACKING.md"
INSTRUCTIONS = WORKSPACE / "SEO-INSTRUCTIONS.md"
HISTORY = WORKSPACE / ".seo-validation-history.json"

def load_history():
    if HISTORY.exists():
        return json.loads(HISTORY.read_text())
    return {"cycle": 0, "last_report": "", "completed": [], "blockers": []}

def save_history(h):
    HISTORY.write_text(json.dumps(h, indent=2, ensure_ascii=False))

def count_done(html_content):
    """Compte le nombre d'items cochés [x] dans le TRACKING.md"""
    return len(re.findall(r'- \[x\]', html_content))

def count_total(html_content):
    """Compte le nombre total d'items de checklist"""
    return len(re.findall(r'- \[ \]|- \[x\]', html_content))

def check_rge_mentions():
    """Vérifie qu'il n'y a pas de mentions RGE/QualiPAC mensongères"""
    issues = []
    for f in WORKSPACE.glob("*.html"):
        content = f.read_text()
        if re.search(r'\bRGE\b|\bQualiPAC\b|\bReconnu Garant de l', content, re.IGNORECASE):
            issues.append(f"{f.name}: mention RGE/QualiPAC détectée")
    return issues

def check_fake_addresses():
    """Vérifie les adresses fictives"""
    issues = []
    for f in WORKSPACE.glob("*.html"):
        content = f.read_text()
        if "Rue de l'Électricité" in content or "Rue des Artisans" in content:
            issues.append(f"{f.name}: adresse générique détectée")
    return issues

def check_header_consistency():
    """Vérifie la cohérence des headers entre pages"""
    files = list(WORKSPACE.glob("*.html"))
    if len(files) < 2:
        return ["Pas assez de pages HTML pour comparer"]
    
    # Compare les structures de navigation
    navs = {}
    for f in files:
        content = f.read_text()
        nav_match = re.search(r'<nav[^>]*>(.*?)</nav>', content, re.DOTALL)
        if nav_match:
            navs[f.name] = nav_match.group(1)[:200]  # tronqué
    
    ref_nav = list(navs.values())[0] if navs else ""
    diffs = [f"Header de {name} diffère de la référence" 
             for name, nav in navs.items() if nav[:100] != ref_nav[:100]]
    return diffs

def check_schema_org():
    """Vérifie les schémas schema.org"""
    issues = []
    for f in WORKSPACE.glob("*.html"):
        content = f.read_text()
        # Vérifie la présence de schema.org
        if 'schema.org' not in content:
            issues.append(f"{f.name}: pas de schema.org détecté")
        # Vérifie le type LocalBusiness ou Electrician
        if 'LocalBusiness' not in content and 'Electrician' not in content:
            issues.append(f"{f.name}: pas de LocalBusiness/Electrician schema")
    return issues

def check_contact_page():
    """Vérifie la page contact"""
    contact = WORKSPACE / "contact.html"
    if not contact.exists():
        return ["contact.html n'existe pas"]
    content = contact.read_text()
    issues = []
    if 'form' not in content.lower():
        issues.append("contact.html : pas de formulaire")
    return issues

def check_title_tags():
    """Vérifie les balises title"""
    issues = []
    for f in WORKSPACE.glob("*.html"):
        content = f.read_text()
        title_match = re.search(r'<title>(.*?)</title>', content)
        if title_match:
            title = title_match.group(1)
            if len(title) < 20:
                issues.append(f"{f.name}: title trop court ({len(title)} chars)")
            elif len(title) > 70:
                issues.append(f"{f.name}: title trop long ({len(title)} chars)")
        else:
            issues.append(f"{f.name}: pas de balise title")
    return issues

def check_phone_numbers():
    """Vérifie les numéros de téléphone fictifs"""
    issues = []
    # Patterns de téléphones invalides : X, * ou zéros répétés (00 00 00 00)
    patterns = [
        r'0[1-9](?:\s*[X\*]){8,}',         # 05 X X X X X
        r'0[1-9]\s*(?:00\s*){3,}',          # 05 00 00 00 00
        r'0[1-9](?:\s*0){8,}',              # 0500000000 (zéros consécutifs)
        r'\+33\s*[X\*](?:\s*[X\*]){7,}',    # +33 X XX XX XX
        r'06\s*[X\*](?:\s*[X\*]){7,}',      # 06 X XX XX XX
    ]
    combined = '|'.join(patterns)
    for f in WORKSPACE.glob("*.html"):
        content = f.read_text()
        phones = re.findall(combined, content, re.IGNORECASE)
        for p in phones:
            if 'X' in p or '*' in p or p.strip() == '0600000000':
                issues.append(f"{f.name}: téléphone fictif détecté: {p.strip()[:15]}")
    return issues

def generate_report():
    print("=" * 60)
    print("  🔍 SEO Elekio — Rapport de validation automatique")
    print("=" * 60)
    print()
    
    history = load_history()
    history["cycle"] += 1
    cycle = history["cycle"]
    print(f"  Cycle n°{cycle}")
    print()
    
    # Lire le tracking
    tracking_content = TRACKING.read_text() if TRACKING.exists() else ""
    done = count_done(tracking_content)
    total = count_total(tracking_content)
    
    print(f"  📊 Avancement : {done}/{total} instructions complétées")
    print()
    
    # Vérifications
    all_issues = []
    
    print("  ─── RÈGLE ABSOLUE (RGE, adresses fictives) ───")
    rge = check_rge_mentions()
    addr = check_fake_addresses()
    phones = check_phone_numbers()
    
    if rge:
        print(f"  ❌ RGE détecté : {len(rge)} problème(s)")
        for i in rge: print(f"     • {i}")
        all_issues.extend(rge)
    else:
        print("  ✅ Pas de mentions RGE/QualiPAC interdites")
    
    if addr:
        print(f"  ❌ Adresses fictives : {len(addr)} problème(s)")
        for i in addr: print(f"     • {i}")
        all_issues.extend(addr)
    else:
        print("  ✅ Adresses cohérentes")
    
    if phones:
        print(f"  ❌ Téléphones fictifs : {len(phones)}")
        for i in phones[:3]: print(f"     • {i}")
        all_issues.extend(phones)
    else:
        print("  ✅ Téléphones valides")
    
    print()
    print("  ─── STRUCTURE ───")
    headers = check_header_consistency()
    if headers:
        print(f"  ⚠️  Headers : {len(headers)} incohérence(s)")
        for i in headers: print(f"     • {i}")
        all_issues.extend(headers)
    else:
        print("  ✅ Headers cohérents entre pages")
    
    print()
    print("  ─── TECHNIQUE ───")
    schemas = check_schema_org()
    titles = check_title_tags()
    contact = check_contact_page()
    
    for issues, label in [(schemas, "Schema.org"), (titles, "Balises title"), (contact, "Contact")]:
        if issues:
            print(f"  ⚠️  {label} : {len(issues)} problème(s)")
            for i in issues: print(f"     • {i}")
            all_issues.extend(issues)
        else:
            print(f"  ✅ {label} : OK")
    
    print()
    print("  ─── RÉSUMÉ DU CYCLE ───")
    print(f"  ✅ {done}/{total} instructions faites")
    print(f"  ⚠️  {len(all_issues)} problèmes détectés")
    
    if all_issues:
        print()
        print("  📋 Prochaines actions recommandées :")
        action_count = 0
        for issue in all_issues:
            action_count += 1
            if action_count > 5:
                print(f"     ... et {len(all_issues) - 5} autre(s) problème(s)")
                break
            issue_lower = issue.lower()
            if "rge" in issue_lower or "qualipac" in issue_lower:
                print(f"     {action_count}. 🚨 CORRIGER : {issue}")
            elif "fictif" in issue_lower or "téléphone" in issue_lower:
                print(f"     {action_count}. 📞 CORRIGER : {issue}")
            elif "adresse" in issue_lower or "fictive" in issue_lower or "générique" in issue_lower:
                print(f"     {action_count}. 📍 CORRIGER : {issue}")
            elif "header" in issue_lower or "incohérence" in issue_lower:
                print(f"     {action_count}. 🔧 CORRIGER : {issue}")
            elif "schema" in issue_lower:
                print(f"     {action_count}. 📊 À AJOUTER : {issue}")
            elif "title" in issue_lower:
                print(f"     {action_count}. 🏷️ À OPTIMISER : {issue}")
            else:
                print(f"     {action_count}. {issue}")
    
    # Update history
    if done > len(history["completed"]):
        history["completed"] = [f"{done}/{total}"]
    if all_issues:
        history["blockers"] = list(set(history["blockers"] + all_issues[:5]))
    history["last_report"] = f"Cycle {cycle}: {done}/{total} faits, {len(all_issues)} problèmes"
    save_history(history)
    
    print()
    print("=" * 60)
    print(f"  Prochain cycle dans ~30 min")
    print("=" * 60)

if __name__ == "__main__":
    generate_report()
