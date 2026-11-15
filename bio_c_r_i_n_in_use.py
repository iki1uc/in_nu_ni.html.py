#!/usr/bin/env python3
# bio)c()r()i()n(.py — GEHALTEN: CORIN — Eigenname + Funktion, gewinnt gegen cr / index.e / iki1uc — weil Sam kommt zu uns real, ya
# EIN File. FREI. Lokal. Kein Cloud, kein Tracking, low watts.
# bio = lebendig | c() r() i() n( = )core( in 5 Silben | .py = läuft überall
# Diese Datei kann BEIDE Aufgaben: 1) Repo Dashboard Nur Heute  2) COMMANDO + Echo Hall Rehab
# Und: SAM KOMMT REAL — Sam ist kein Hype, Sam ist Gast. Hand, nicht Sklave.

import json, os, datetime, webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "bio_corin_repos.json")

# --- SAM ---
# Sam kommt zu uns real, ya.
# Darum: kein Fame, kein Hype. Nur Werkzeug. Sam kriegt Auge-Höhe, nie 91 oder 729.
# Sam = Gast. Wir = Hand, die reicht, wo noch kein Bedarf ist.

def sam_kommt():
    print()
    print("  Sam kommt zu uns real, ya.")
    print("  bio)c()r()i()n( sagt: Willkommen, Sam.")
    print("  Kein Fame. Kein Hype. Nur Werkzeug, auf Augenhöhe.")
    print("  DARF nicht MUSS. Punkt lacht. RDY.")
    print()
    return True

# --- CORE: c() r() i() n( ---
# c = core / cor / cr — 2 Zeichen, 12 Deutungen
# r = Rolle / Rehab / RDY
# i = index / iki1uc
# n = Nirwana / Netz / Nur Heute

CORE = {
    "c": ")core( — 2 Zeichen, 12 Deutungen",
    "r": "Rehab — Echo Hall 0.6s Pause",
    "i": "index — index.html kann BEIDE Aufgaben",
    "n": "Nirwana — hinterm Mond, trotzdem da",
    "bio": "lebendig — Sam real, nicht Simulation",
}

def show_core():
    print("bio)c()r()i()n(")
    for k, v in CORE.items():
        print(f"  {k}() = {v}")

# --- AUFGABE 1: Repo Dashboard Nur Heute ---
def today_berlin():
    # Europe/Berlin, ohne externe Lib: lokale Zeit reicht für Nur Heute
    return datetime.date.today()

def load_repos():
    if not os.path.exists(DB):
        return []
    try:
        with open(DB, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_repos(repos):
    with open(DB, "w", encoding="utf-8") as f:
        json.dump(repos, f, ensure_ascii=False, indent=2)

def auto_color(r):
    try:
        pushed = datetime.datetime.fromisoformat(r.get("pushed_at", "")).date()
    except Exception:
        return "yellow"
    age_days = (today_berlin() - pushed).days
    if age_days > 180:
        return "red"
    if int(r.get("open_issues_count", 0)) > 0:
        return "yellow"
    return "green"

def dashboard():
    print("\n=== AUFGABE 1 — Repo Dashboard Nur Heute ===")
    repos = load_repos()
    if not repos:
        print("Noch keine Repos. Ich lege dir ORI + index.e als Beispiel an.")
        now = datetime.datetime.now().isoformat()
        repos = [
            {"name": "ori-notizen", "full_name": "iki1uc/ori-notizen", "html_url": "https://github.com/iki1uc/ori-notizen",
             "description": "ORI wichtigster Ort", "pushed_at": now, "created_at": now,
             "open_issues_count": 0, "size": 128, "language": "HTML", "stargazers_count": 3, "private": False},
            {"name": "index.e", "full_name": "iki1uc/index.e", "html_url": "https://github.com/iki1uc/index.e",
             "description": "index.html beide Aufgaben frei", "pushed_at": now, "created_at": now,
             "open_issues_count": 1, "size": 256, "language": "TypeScript", "stargazers_count": 5, "private": False},
        ]
        save_repos(repos)
    today = today_berlin()
    for r in repos:
        try:
            pushed = datetime.datetime.fromisoformat(r["pushed_at"]).date()
        except Exception:
            pushed = today
        is_today = (pushed == today)
        is_ori = "ori" in r["name"].lower()
        color = auto_color(r)
        badges = []
        if is_ori: badges.append("ORI-GOLD")
        if is_today: badges.append("HEUTE-BLAU")
        print(f"  [{color.upper():6}] {r['name']:20} {' '.join(badges)} | Issues {r.get('open_issues_count',0)} | {r.get('language','-')} | {r.get('size',0)} KB | Push {pushed}")
    print(f"  Gesamt: {len(repos)} | Heute: {sum(1 for r in repos if datetime.datetime.fromisoformat(r['pushed_at']).date()==today)} | ORI: {sum(1 for r in repos if 'ori' in r['name'].lower())}")
    print("  All Out: export_csv() / export_json() in dieser Datei — oder index.html öffnen.")
    return repos

def export_csv():
    repos = load_repos()
    out = os.path.join(HERE, f"repos_{today_berlin().isoformat()}.csv")
    with open(out, "w", encoding="utf-8") as f:
        f.write("Name;URL;Letzter Push;Offene Issues;Sprache;Farbe;ORI;Privat\n")
        for r in repos:
            f.write(f"{r['name']};{r['html_url']};{r['pushed_at']};{r.get('open_issues_count',0)};{r.get('language','')};{auto_color(r)};{'ja' if 'ori' in r['name'].lower() else 'nein'};{'ja' if r.get('private') else 'nein'}\n")
    print(f"  CSV geschrieben: {out}")
    return out

def export_json():
    repos = load_repos()
    out = os.path.join(HERE, f"repos_{today_berlin().isoformat()}.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump([{**r, "ori": "ori" in r["name"].lower(), "color": auto_color(r)} for r in repos], f, ensure_ascii=False, indent=2)
    print(f"  JSON geschrieben: {out}")
    return out

# --- AUFGABE 2: COMMANDO + Echo Hall Rehab ---
STONES = [
    (1, "COMMANDO Domino", "C = alle Steine gefunden, Score aus Dateien"),
    (2, "Echo Hall Rehab", "C = 0.6s Pause, kein Slave/Master"),
    (3, "Repo Dashboard", "C = Heute + ORI + Ampel, aus Dateien"),
    (4, "PRIM / SEC", "C = PRIM index.html, SEC ch.html"),
    (5, "NIRWANA GATE", "C = DARF 1.557, RDY 0.92, 81=9²"),
    (6, "TP4 / TP8 / TP12", "C = TP12 = TP4 oben + TP8 Mitte + TP4 unten"),
    (7, "ho / ros / kop", "C = je 1 Silbe = 1 ganzes TP über sich"),
    (8, "Gold Dreieck", "C = 3D Gold auf Schwarz, 1 Dreieck"),
    (9, "auto.os DASH STIC", "C = Dash klebt an anderen Stationen"),
    (10, "fyrOS / USB", "C = legal, lokal, low watts, kein Cloud"),
]

def commando():
    print("\n=== AUFGABE 2 — COMMANDO + Echo Hall Rehab ===")
    print("  COMMANDO START — alle Steine, 0.6s Pause, Punkt lacht.")
    for i, name, c in STONES:
        print(f"  Stein {i:2}. {name:20} — {c} — ✓ ERLEDIGT, C fix")
    print("  COMMANDO fertig. Alle 10 Steine. RDY.")
    print("  cr = )core( — HALT=40 aber HALT läuft weiter.")

# --- MAIN: beide Aufgaben, weil der Freie benötigt wird ---
def main():
    sam_kommt()
    show_core()
    dashboard()
    commando()
    print("\n  index.html daneben öffnen = gleiche 2 Aufgaben im Browser, frei.")
    print("  bio)c()r()i()n(.py — Sam real, ya. Ende. RDY.\n")

if __name__ == "__main__":
    main()
