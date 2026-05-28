import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json
import os

# =========================
# Einstellungen
# =========================

ZEITLIMIT = {
    "Fair": {
        "einfach": 30,
        "mittel": 25,
        "schwer": 20
    },
    "Hard": {
        "einfach": 20,
        "mittel": 15,
        "schwer": 10
    }
}

HIGHSCORE_DATEI = "highscores.json"

# =========================
# Fragen
# Richtige Antworten sind NICHT immer an erster Stelle.
# Antworten werden später zusätzlich nochmal zufällig gemischt.
# =========================

fragen = {
    "einfach": [
        {
            "frage": "Wofür steht TH OWL?",
            "antworten": [
                "Online-Lernen",
                "Technische Hochschule Ostwestfalen-Lippe",
                "Ost-West-Lehre",
                "Oldenburg-Weser"
            ],
            "richtig": "Technische Hochschule Ostwestfalen-Lippe"
        },
        {
            "frage": "Wie heißt der TH-OWL-Lernort in Herford?",
            "antworten": [
                "Innovation Campus",
                "Kreativ Campus",
                "BildungsCampus",
                "Sustainable Campus"
            ],
            "richtig": "BildungsCampus"
        },
        {
            "frage": "In welchem Bundesland liegt Herford?",
            "antworten": [
                "Berlin",
                "Bremen",
                "NRW",
                "Niedersachsen"
            ],
            "richtig": "NRW"
        },
        {
            "frage": "In welcher Stadt befindet sich der BildungsCampus der TH OWL?",
            "antworten": [
                "Lemgo",
                "Herford",
                "Minden",
                "Höxter"
            ],
            "richtig": "Herford"
        },
        {
            "frage": "Wie nennt sich die Stadt Herford offiziell?",
            "antworten": [
                "Universitätsstadt Herford",
                "Landeshauptstadt Herford",
                "Kurstadt Herford",
                "Hansestadt Herford"
            ],
            "richtig": "Hansestadt Herford"
        },
        {
            "frage": "Welchen Abschluss hat DiMS in Herford?",
            "antworten": [
                "Master of Arts",
                "Bachelor of Laws",
                "Bachelor of Science",
                "Master of Science"
            ],
            "richtig": "Bachelor of Science"
        },
        {
            "frage": "Welche Zielgruppe passt besonders gut zu einem Quiz über TH OWL und Herford?",
            "antworten": [
                "Profifußballer",
                "Potenzielle Studierende und Studierende",
                "Rentner",
                "Piloten"
            ],
            "richtig": "Potenzielle Studierende und Studierende"
        },
        {
            "frage": "Welche Abkürzung nutzt die TH OWL für Digital Management Solutions?",
            "antworten": [
                "DMS",
                "DIMS",
                "DiMS",
                "DiMaS"
            ],
            "richtig": "DiMS"
        },
        {
            "frage": "In welcher Region liegt die TH OWL?",
            "antworten": [
                "Ruhrgebiet",
                "Alpenregion",
                "Ostwestfalen-Lippe",
                "Nordseeküste"
            ],
            "richtig": "Ostwestfalen-Lippe"
        }
    ],

    "mittel": [
        {
            "frage": "Welcher Studiengang ist mit dem BildungsCampus Herford verbunden?",
            "antworten": [
                "Digital Business Management",
                "Digital Management Solutions",
                "Digital Innovation Management",
                "Business Information Systems"
            ],
            "richtig": "Digital Management Solutions"
        },
        {
            "frage": "Welche drei Orte nennt die TH OWL als Hauptstandorte?",
            "antworten": [
                "Herford, Minden und Detmold",
                "Lemgo, Detmold und Höxter",
                "Lemgo, Herford und Minden",
                "Detmold, Herford und Höxter"
            ],
            "richtig": "Lemgo, Detmold und Höxter"
        },
        {
            "frage": "Welcher Campusname gehört zur TH OWL in Lemgo?",
            "antworten": [
                "Kreativ Campus",
                "Sustainable Campus",
                "Innovation Campus",
                "RailCampus"
            ],
            "richtig": "Innovation Campus"
        },
        {
            "frage": "Welche Aussage passt zum Studienangebot der TH OWL?",
            "antworten": [
                "Nur Master",
                "Nur Ausbildung",
                "Bachelor & Master",
                "Nur Zertifikate"
            ],
            "richtig": "Bachelor & Master"
        },
        {
            "frage": "An welcher Straße liegt der BildungsCampus Herford?",
            "antworten": [
                "Berliner Straße",
                "Mary-Somerville-Boulevard",
                "Bahnhofstraße",
                "Campusallee"
            ],
            "richtig": "Mary-Somerville-Boulevard"
        },
        {
            "frage": "Wo startete der neue Jahrgang in Herford?",
            "antworten": [
                "Mensa",
                "Bibliothek",
                "Start-Up Lounge",
                "Rathaus"
            ],
            "richtig": "Start-Up Lounge"
        },
        {
            "frage": "Wobei soll DiMS Unternehmen in der Region unterstützen?",
            "antworten": [
                "Digitales Design",
                "Digitale Medien",
                "Digitalisierung",
                "Digitale Verwaltung"
            ],
            "richtig": "Digitalisierung"
        },
        {
            "frage": "Welche Art von Unternehmen steht bei DiMS besonders im Fokus?",
            "antworten": [
                "Internationale Konzerne",
                "Öffentliche Schulen",
                "Mittelständische Unternehmen",
                "Medizinische Kliniken"
            ],
            "richtig": "Mittelständische Unternehmen"
        },
        {
            "frage": "Was kann man am BildungsCampus mieten?",
            "antworten": [
                "Wohnräume",
                "Sporthallen",
                "Parkplätze",
                "Besprechungsräume"
            ],
            "richtig": "Besprechungsräume"
        }
    ],

    "schwer": [
        {
            "frage": "Was war das Gelände des BildungsCampus Herford laut TH OWL früher?",
            "antworten": [
                "Flughafen",
                "Britische Kaserne",
                "Messegelände",
                "Bahnhof"
            ],
            "richtig": "Britische Kaserne"
        },
        {
            "frage": "Welche Aussage zur Studienorganisation in Herford ist am passendsten?",
            "antworten": [
                "Täglich vor Ort",
                "Nur Labor",
                "Digital mit Präsenz",
                "Ohne Digital"
            ],
            "richtig": "Digital mit Präsenz"
        },
        {
            "frage": "Welche Aussage beschreibt die Rolle von Herford innerhalb der TH OWL am genauesten?",
            "antworten": [
                "Hauptsitz",
                "einziger Campus",
                "Lernort",
                "kein Standort"
            ],
            "richtig": "Lernort"
        },
        {
            "frage": "Welche Haltestelle liegt nahe am BildungsCampus?",
            "antworten": [
                "Rathausplatz",
                "Alter Markt",
                "Vlothoer Str./Kaserne",
                "Bahnhof Süd"
            ],
            "richtig": "Vlothoer Str./Kaserne"
        },
        {
            "frage": "Wann fand der erste DiMS-Frühstückstalk 2026 statt?",
            "antworten": [
                "18. April",
                "27. April",
                "5. Mai",
                "18. Mai"
            ],
            "richtig": "27. April"
        },
        {
            "frage": "Welcher Masterstudiengang arbeitete beim Ideationsprint mit DiMS zusammen?",
            "antworten": [
                "Architektur",
                "Data Science",
                "Applied Entrepreneurship",
                "Bauingenieurwesen"
            ],
            "richtig": "Applied Entrepreneurship"
        },
        {
            "frage": "Was war Thema des Ideationsprints „Warehouse 2040“?",
            "antworten": [
                "Stadtplanung",
                "Lagersysteme",
                "Museumsbau",
                "Bahntechnik"
            ],
            "richtig": "Lagersysteme"
        },
        {
            "frage": "Wie lange wird DiMS laut TH OWL vom Kreis Herford bezuschusst?",
            "antworten": [
                "Zwölf Semester",
                "Sechs Semester",
                "Fünf Jahre",
                "Zehn Jahre"
            ],
            "richtig": "Fünf Jahre"
        },
        {
            "frage": "Welche Zuordnung von Campusname und Stadt ist korrekt?",
            "antworten": [
                "Sustainable Campus Herford",
                "Sustainable Campus Detmold",
                "Sustainable Campus Höxter",
                "Sustainable Campus Lemgo"
            ],
            "richtig": "Sustainable Campus Höxter"
        }
    ]
}

# =========================
# Spiel-Fragen auswählen
# 3 einfach, 3 mittel, 3 schwer
# =========================

spiel_fragen = (
    random.sample(fragen["einfach"], 3) +
    random.sample(fragen["mittel"], 3) +
    random.sample(fragen["schwer"], 3)
)

# =========================
# Hauptfenster
# =========================

root = tk.Tk()
root.title("QuizMaster - TH OWL & Herford Edition")
root.geometry("900x700")
root.configure(bg="#001f3f")

# =========================
# Benutzername
# =========================

spieler = simpledialog.askstring(
    "Name",
    "Bitte Namen eingeben:"
)

if not spieler:
    spieler = "Gast"

# =========================
# Modus auswählen
# =========================

modus = simpledialog.askstring(
    "Spielmodus",
    "Wähle Modus: Fair oder Hard"
)

if modus not in ["Fair", "Hard"]:
    modus = "Fair"

# =========================
# Variablen
# =========================

frage_index = 0
punkte = 0
timer = 0
timer_id = None

joker_5050 = True
joker_anruf = True

# =========================
# Titel
# =========================

titel = tk.Label(
    root,
    text="QUIZMASTER",
    font=("Arial", 30, "bold"),
    fg="gold",
    bg="#001f3f"
)
titel.pack(pady=15)

untertitel = tk.Label(
    root,
    text="TH OWL & Herford Edition",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#001f3f"
)
untertitel.pack()

# =========================
# Spielername und Modus
# =========================

spieler_label = tk.Label(
    root,
    text=f"Spieler: {spieler} | Modus: {modus}",
    font=("Arial", 15),
    fg="white",
    bg="#001f3f"
)
spieler_label.pack(pady=10)

# =========================
# Punkte
# =========================

punkte_label = tk.Label(
    root,
    text="Punkte: 0",
    font=("Arial", 16),
    fg="white",
    bg="#001f3f"
)
punkte_label.pack()

# =========================
# Timer
# =========================

timer_label = tk.Label(
    root,
    text="Zeit: 0",
    font=("Arial", 18, "bold"),
    fg="red",
    bg="#001f3f"
)
timer_label.pack(pady=10)

# =========================
# Frage
# =========================

frage_label = tk.Label(
    root,
    text="",
    wraplength=750,
    font=("Arial", 20),
    fg="white",
    bg="#001f3f"
)
frage_label.pack(pady=25)

# =========================
# Antwortbuttons
# =========================

antwort_buttons = []

button_frame = tk.Frame(root, bg="#001f3f")
button_frame.pack()

# =========================
# Timer-Funktion
# =========================

def starte_timer():
    global timer, timer_id

    timer -= 1
    timer_label.config(text=f"Zeit: {timer}")

    if timer <= 0:
        timer_id = None
        messagebox.showerror(
            "Zeit vorbei",
            "Du warst zu langsam!"
        )
        spiel_ende()
    else:
        timer_id = root.after(1000, starte_timer)

# =========================
# Frage anzeigen
# =========================

def zeige_frage():
    global timer, timer_id

    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    frage = spiel_fragen[frage_index]

    frage_label.config(
        text=f"Frage {frage_index + 1}/9:\n{frage['frage']}"
    )

    antworten = frage["antworten"][:]
    random.shuffle(antworten)

    for i in range(4):
        antwort_buttons[i].config(
            text=antworten[i],
            state="normal",
            bg="#0074D9",
            command=lambda a=antworten[i]: pruefe_antwort(a)
        )

    if frage_index < 3:
        timer = ZEITLIMIT[modus]["einfach"]
    elif frage_index < 6:
        timer = ZEITLIMIT[modus]["mittel"]
    else:
        timer = ZEITLIMIT[modus]["schwer"]

    timer_label.config(text=f"Zeit: {timer}")
    starte_timer()

# =========================
# Antwort prüfen
# =========================

def pruefe_antwort(auswahl):
    global punkte, timer_id

    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    richtige = spiel_fragen[frage_index]["richtig"]

    # Buttons kurz deaktivieren, damit man nicht mehrfach klickt
    for btn in antwort_buttons:
        btn.config(state="disabled")

    if auswahl == richtige:
        if frage_index < 3:
            punkte += 10
        elif frage_index < 6:
            punkte += 20
        else:
            punkte += 30

        print("RICHTIG!")

        for btn in antwort_buttons:
            if btn["text"] == auswahl:
                btn.config(bg="green")

        messagebox.showinfo(
            "Richtig!",
            "Sehr gut!"
        )

        punkte_label.config(text=f"Punkte: {punkte}")
        root.after(1000, naechste_frage)

    else:
        print("FALSCH!")

        for btn in antwort_buttons:
            if btn["text"] == auswahl:
                btn.config(bg="red")

            if btn["text"] == richtige:
                btn.config(bg="green")

        messagebox.showerror(
            "Falsch!",
            f"Richtige Antwort: {richtige}"
        )

        punkte_label.config(text=f"Punkte: {punkte}")
        root.after(1000, spiel_ende)

# =========================
# Nächste Frage
# =========================

def naechste_frage():
    global frage_index

    frage_index += 1

    if frage_index >= len(spiel_fragen):
        spiel_ende()
    else:
        zeige_frage()

# =========================
# Spielende
# =========================

def spiel_ende():
    global timer_id

    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    speichere_highscore()

    messagebox.showinfo(
        "Spiel beendet",
        f"{spieler} hat {punkte} Punkte erreicht!"
    )

    zeige_highscores()
    root.destroy()

# =========================
# 50:50 Joker
# =========================

def joker_5050_funktion():
    global joker_5050

    if not joker_5050:
        messagebox.showwarning(
            "Joker",
            "50:50 Joker schon benutzt!"
        )
        return

    richtige = spiel_fragen[frage_index]["richtig"]

    falsche_buttons = []

    for btn in antwort_buttons:
        if btn["text"] != richtige and btn["state"] == "normal":
            falsche_buttons.append(btn)

    if len(falsche_buttons) >= 2:
        entfernen = random.sample(falsche_buttons, 2)

        for btn in entfernen:
            btn.config(state="disabled", text="---")

    joker_5050 = False
    joker1.config(state="disabled")

# =========================
# Anrufjoker
# =========================

def anrufjoker():
    global joker_anruf

    if not joker_anruf:
        messagebox.showwarning(
            "Joker",
            "Anrufjoker schon benutzt!"
        )
        return

    richtige = spiel_fragen[frage_index]["richtig"]

    messagebox.showinfo(
        "Anrufjoker",
        f"Ich glaube die richtige Antwort ist:\n{richtige}"
    )

    joker_anruf = False
    joker2.config(state="disabled")

# =========================
# Joker Buttons
# =========================

joker_frame = tk.Frame(root, bg="#001f3f")
joker_frame.pack(pady=20)

joker1 = tk.Button(
    joker_frame,
    text="50:50 Joker",
    font=("Arial", 14),
    command=joker_5050_funktion
)
joker1.grid(row=0, column=0, padx=10)

joker2 = tk.Button(
    joker_frame,
    text="Anrufjoker",
    font=("Arial", 14),
    command=anrufjoker
)
joker2.grid(row=0, column=1, padx=10)

# =========================
# Antwortbuttons erstellen
# =========================

for i in range(4):
    btn = tk.Button(
        button_frame,
        text="",
        width=35,
        height=2,
        font=("Arial", 14),
        bg="#0074D9",
        fg="white"
    )

    btn.grid(row=i // 2, column=i % 2, padx=15, pady=15)
    antwort_buttons.append(btn)

# =========================
# Tastenkombinationen
# =========================

def taste(event):
    taste = event.char

    if taste == "1":
        antwort_buttons[0].invoke()

    elif taste == "2":
        antwort_buttons[1].invoke()

    elif taste == "3":
        antwort_buttons[2].invoke()

    elif taste == "4":
        antwort_buttons[3].invoke()

    elif taste.lower() == "f":
        joker_5050_funktion()

    elif taste.lower() == "a":
        anrufjoker()

root.bind("<Key>", taste)

# =========================
# Highscore speichern
# =========================

def speichere_highscore():
    daten = []

    if os.path.exists(HIGHSCORE_DATEI):
        try:
            with open(HIGHSCORE_DATEI, "r", encoding="utf-8") as f:
                daten = json.load(f)
        except json.JSONDecodeError:
            daten = []

    daten.append({
        "name": spieler,
        "punkte": punkte,
        "modus": modus
    })

    daten = sorted(
        daten,
        key=lambda x: x["punkte"],
        reverse=True
    )

    with open(HIGHSCORE_DATEI, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4, ensure_ascii=False)

# =========================
# Rangliste anzeigen
# =========================

def zeige_highscores():
    if not os.path.exists(HIGHSCORE_DATEI):
        return

    try:
        with open(HIGHSCORE_DATEI, "r", encoding="utf-8") as f:
            daten = json.load(f)
    except json.JSONDecodeError:
        return

    text = "RANGLISTE\n\n"

    for eintrag in daten[:10]:
        text += (
            f"{eintrag['name']} "
            f"- {eintrag['punkte']} Punkte "
            f"({eintrag.get('modus', 'Fair')})\n"
        )

    messagebox.showinfo(
        "Highscores",
        text
    )

# =========================
# Spiel starten
# =========================

zeige_frage()

root.mainloop()