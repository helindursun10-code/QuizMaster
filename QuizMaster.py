import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json
import os


# =========================
# Einstellungen
# =========================

HIGHSCORE_DATEI = "highscores.json"

# Maximale Länge für Spielernamen.
# Dadurch bleiben Anzeige und Highscore-Liste übersichtlich.
MAX_NAME_LAENGE = 15

# Zeit pro Frage je nach Modus und Schwierigkeit
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

# Punkte pro Schwierigkeit
PUNKTE = {
    "einfach": 10,
    "mittel": 20,
    "schwer": 30
}


# =========================
# Fragen
# =========================
# Jede Frage hat:
# - frage: Fragetext
# - antworten: vier Antwortmöglichkeiten
# - richtig: richtige Antwort

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
# Globale Spielvariablen
# =========================

spieler_liste = []
aktueller_spieler_index = 0

spieler_name = ""
modus = "Fair"

spiel_fragen = []
frage_index = 0
punkte = 0
timer = 0
timer_id = None

joker_5050_verfuegbar = True
joker_anruf_verfuegbar = True
joker_zeit_verfuegbar = True
joker_switch_verfuegbar = True

# Verhindert, dass man nach einer Antwort nochmal klicken kann.
# Die Buttons bleiben aber farbig und lesbar.
antwort_gesperrt = False

antwort_buttons = []


# =========================
# Highscore-Funktionen
# =========================

def lade_highscores():
    # Wenn die Datei noch nicht existiert, gibt es noch keine Highscores.
    if not os.path.exists(HIGHSCORE_DATEI):
        return []

    try:
        with open(HIGHSCORE_DATEI, "r", encoding="utf-8") as datei:
            return json.load(datei)
    except json.JSONDecodeError:
        return []


def speichere_highscores(daten):
    # Highscores werden dauerhaft in einer JSON-Datei gespeichert.
    with open(HIGHSCORE_DATEI, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, indent=4, ensure_ascii=False)


def speichere_highscore(name, punkte_anzahl, spielmodus):
    # Neuer Punktestand wird zur Rangliste hinzugefügt.
    daten = lade_highscores()

    daten.append({
        "name": name,
        "punkte": punkte_anzahl,
        "modus": spielmodus
    })

    # Höchste Punktzahl steht oben.
    daten = sorted(daten, key=lambda eintrag: eintrag["punkte"], reverse=True)

    speichere_highscores(daten)


def zeige_highscores():
    daten = lade_highscores()

    if not daten:
        messagebox.showinfo(
            "Rangliste",
            "Noch keine Highscores vorhanden.\nSpiele zuerst eine Runde."
        )
        return

    text = "RANGLISTE\n\n"

    for platz, eintrag in enumerate(daten[:10], start=1):
        text += f"{platz}. {eintrag['name']} - {eintrag['punkte']} Punkte ({eintrag['modus']})\n"

    messagebox.showinfo("Rangliste", text)

def zeige_regeln():
    # Diese Funktion zeigt die Spielregeln in einem Infofenster an.
    # Der Spieler kann dadurch jederzeit nachlesen, wie das Spiel funktioniert.
    regeln = (
        "SPIELREGELN\n\n"
        "• Es gibt 9 Fragen pro Runde.\n"
        "• Die ersten 3 Fragen sind einfach.\n"
        "• Die nächsten 3 Fragen sind mittel.\n"
        "• Die letzten 3 Fragen sind schwer.\n"
        "• Jede Frage hat 4 Antwortmöglichkeiten.\n"
        "• Richtige Antworten geben Punkte.\n"
        "• Eine falsche Antwort beendet die Runde.\n"
        "• Wenn die Zeit abläuft, endet die Runde.\n"
        "• Jeder Joker darf nur einmal benutzt werden.\n\n"
        "JOKER:\n"
        "• 50:50 entfernt zwei falsche Antworten.\n"
        "• Anrufjoker gibt einen Hinweis.\n"
        "• Zeitjoker gibt 10 Sekunden extra.\n"
        "• Frage wechseln ersetzt die aktuelle Frage."
    )

    messagebox.showinfo("Spielregeln", regeln)

# =========================
# Hilfsfunktionen
# =========================

def waehle_spiel_fragen():
    # Es werden 3 einfache, 3 mittlere und 3 schwere Fragen gewählt.
    # Dadurch steigt die Schwierigkeit im Spiel.
    return (
        random.sample(fragen["einfach"], 3) +
        random.sample(fragen["mittel"], 3) +
        random.sample(fragen["schwer"], 3)
    )


def aktuelle_schwierigkeit():
    # Frage 1-3: einfach
    # Frage 4-6: mittel
    # Frage 7-9: schwer
    if frage_index < 3:
        return "einfach"
    elif frage_index < 6:
        return "mittel"
    else:
        return "schwer"


def reset_joker():
    global joker_5050_verfuegbar, joker_anruf_verfuegbar
    global joker_zeit_verfuegbar, joker_switch_verfuegbar

    joker_5050_verfuegbar = True
    joker_anruf_verfuegbar = True
    joker_zeit_verfuegbar = True
    joker_switch_verfuegbar = True

    joker_5050_button.config(state="normal")
    joker_anruf_button.config(state="normal")
    joker_zeit_button.config(state="normal")
    joker_switch_button.config(state="normal")


# =========================
# Startabfragen
# =========================

def programm_beenden():
    # Diese Funktion beendet das Programm sauber.
    # Sie wird genutzt, wenn der Spieler bei einer Startabfrage auf "Abbrechen" klickt.
    root.destroy()
    raise SystemExit

def start_abfragen():
    global spieler_liste, modus

    # Diese Funktion fragt alle Startdaten ab:
    # 1. Spieleranzahl
    # 2. Spielernamen
    # 3. Spielmodus
    #
    # Die Variable "schritt" merkt sich, in welchem Teil der Abfrage wir sind.
    # Dadurch kann Cancel zu einem vorherigen Schritt zurückgehen.

    spieler_liste = []
    anzahl = None
    schritt = "spieleranzahl"

    while True:

        # =========================
        # Schritt 1: Spieleranzahl
        # =========================
        if schritt == "spieleranzahl":
            anzahl_text = simpledialog.askstring(
                "Spieleranzahl",
                "Wie viele Spieler? Bitte 1, 2, eins oder zwei eingeben:",
                parent=root
            )

            # Bei der ersten Abfrage gibt es kein vorheriges Fenster.
            # Deshalb beendet Cancel hier das Programm.
            if anzahl_text is None:
                programm_beenden()

            # strip() entfernt Leerzeichen.
            # lower() macht Groß-/Kleinschreibung egal.
            anzahl_text = anzahl_text.strip().lower()

            # in prüft, ob die Eingabe in der erlaubten Liste vorkommt.
            if anzahl_text in ["1", "eins"]:
                anzahl = 1
                spieler_liste = []
                schritt = "namen"
                continue

            if anzahl_text in ["2", "zwei"]:
                anzahl = 2
                spieler_liste = []
                schritt = "namen"
                continue

            messagebox.showwarning(
                "Ungültige Eingabe",
                "Bitte nur 1, 2, eins oder zwei eingeben.",
                parent=root
            )

        # =========================
        # Schritt 2: Spielernamen
        # =========================
        elif schritt == "namen":
            nummer = len(spieler_liste)

            name = simpledialog.askstring(
                "Spielername",
                f"Name Spieler {nummer + 1} eingeben "
                f"(max. {MAX_NAME_LAENGE} Zeichen):",
                parent=root
            )

            # Cancel bei Spieler 1 geht zurück zur Spieleranzahl.
            if name is None:
                if len(spieler_liste) == 0:
                    schritt = "spieleranzahl"
                    continue

                # Cancel bei Spieler 2 geht zurück zu Spieler 1.
                # pop() entfernt den zuletzt gespeicherten Spieler.
                spieler_liste.pop()
                continue

            name = name.strip()

            # not name bedeutet: Der Name ist leer.
            if not name:
                messagebox.showwarning(
                    "Ungültiger Name",
                    "Bitte einen Namen eingeben.",
                    parent=root
                )
                continue

            # len(name) zählt die Zeichen.
            # > prüft, ob der Name zu lang ist.
            if len(name) > MAX_NAME_LAENGE:
                messagebox.showwarning(
                    "Name zu lang",
                    f"Der Name darf maximal {MAX_NAME_LAENGE} Zeichen haben.",
                    parent=root
                )
                continue

            spieler_liste.append({
                "name": name,
                "punkte": 0
            })

            # Wenn alle Namen eingegeben sind, geht es zum Modus.
            if len(spieler_liste) == anzahl:
                schritt = "modus"

        # =========================
        # Schritt 3: Spielmodus
        # =========================
        elif schritt == "modus":
            gewaehlter_modus = simpledialog.askstring(
                "Spielmodus",
                "Wähle Modus: Fair oder Hard:",
                parent=root
            )

            # Cancel beim Modus geht zurück zur letzten Namenseingabe.
            # Dafür entfernen wir den zuletzt gespeicherten Namen.
            if gewaehlter_modus is None:
                if len(spieler_liste) > 0:
                    spieler_liste.pop()

                schritt = "namen"
                continue

            # strip() entfernt Leerzeichen.
            # lower() macht Groß-/Kleinschreibung egal.
            # Dadurch funktionieren z. B. "FAIR", "fair", "F", "f".
            gewaehlter_modus = gewaehlter_modus.strip().lower()

            # Fair-Modus akzeptiert ausgeschrieben oder als Abkürzung.
            if gewaehlter_modus in ["fair", "f"]:
                modus = "Fair"
                break

            # Hard-Modus akzeptiert ausgeschrieben oder als Abkürzung.
            if gewaehlter_modus in ["hard", "h"]:
                modus = "Hard"
                break

            messagebox.showwarning(
                "Ungültiger Modus",
                "Bitte Fair, Hard, F oder H eingeben.",
                parent=root
            )


# =========================
# Oberfläche
# =========================

root = tk.Tk()
root.title("QuizMaster - TH OWL & Herford Edition")
root.geometry("950x720")
root.configure(bg="#001f3f")

titel_label = tk.Label(
    root,
    text="QUIZMASTER",
    font=("Arial", 30, "bold"),
    fg="gold",
    bg="#001f3f"
)
titel_label.pack(pady=10)

untertitel_label = tk.Label(
    root,
    text="TH OWL & Herford Edition",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#001f3f"
)
untertitel_label.pack()

info_label = tk.Label(
    root,
    text="",
    font=("Arial", 15),
    fg="white",
    bg="#001f3f"
)
info_label.pack(pady=10)

punkte_label = tk.Label(
    root,
    text="Punkte: 0",
    font=("Arial", 16),
    fg="white",
    bg="#001f3f"
)
punkte_label.pack()

timer_label = tk.Label(
    root,
    text="Zeit: 0",
    font=("Arial", 18, "bold"),
    fg="red",
    bg="#001f3f"
)
timer_label.pack(pady=10)

frage_label = tk.Label(
    root,
    text="",
    wraplength=800,
    font=("Arial", 20),
    fg="white",
    bg="#001f3f"
)
frage_label.pack(pady=20)

antwort_frame = tk.Frame(root, bg="#001f3f")
antwort_frame.pack()

for i in range(4):
    button = tk.Label(
        antwort_frame,
        text="",
        width=38,
        height=2,
        font=("Arial", 14, "bold"),
        bg="#004C99",
        fg="white",
        relief="raised",
        bd=4,
        cursor="hand2"
    )

    button.grid(row=i // 2, column=i % 2, padx=15, pady=15)
    antwort_buttons.append(button)

joker_frame = tk.Frame(root, bg="#001f3f")
joker_frame.pack(pady=20)

joker_5050_button = tk.Button(
    joker_frame,
    text="50:50 Joker",
    font=("Arial", 14),
    command=lambda: joker_5050()
)
joker_5050_button.grid(row=0, column=0, padx=10)

joker_anruf_button = tk.Button(
    joker_frame,
    text="Anrufjoker",
    font=("Arial", 14),
    command=lambda: anrufjoker()
)
joker_anruf_button.grid(row=0, column=1, padx=10)

joker_zeit_button = tk.Button(
    joker_frame,
    text="Zeitjoker +10s",
    font=("Arial", 14),
    command=lambda: zeitjoker()
)
joker_zeit_button.grid(row=0, column=2, padx=10)

joker_switch_button = tk.Button(
    joker_frame,
    text="Frage wechseln",
    font=("Arial", 14),
    command=lambda: frage_wechseln_joker()
)
joker_switch_button.grid(row=0, column=3, padx=10)

highscore_button = tk.Button(
    root,
    text="Rangliste anzeigen",
    font=("Arial", 14),
    command=zeige_highscores
)
highscore_button.pack(pady=5)

regeln_button = tk.Button(
    root,
    text="Regeln anzeigen",
    font=("Arial", 14),
    command=zeige_regeln
)
regeln_button.pack(pady=5)

hilfe_label = tk.Label(
    root,
    text="Tasten: 1-4 Antworten | F = 50:50 | A = Anrufjoker | Z = Zeitjoker | W = Frage wechseln",
    font=("Arial", 12),
    fg="white",
    bg="#001f3f"
)
hilfe_label.pack(pady=5)


# =========================
# Effekt-Funktionen
# =========================

def farbe_zuruecksetzen():
    # Nach dem Effekt wird die normale Hintergrundfarbe wiederhergestellt.
    normale_farbe = "#001f3f"

    root.configure(bg=normale_farbe)
    titel_label.config(bg=normale_farbe)
    untertitel_label.config(bg=normale_farbe)
    info_label.config(bg=normale_farbe)
    punkte_label.config(bg=normale_farbe)
    timer_label.config(bg=normale_farbe)
    frage_label.config(bg=normale_farbe)
    antwort_frame.config(bg=normale_farbe)
    joker_frame.config(bg=normale_farbe)
    hilfe_label.config(bg=normale_farbe)


def zeige_effekt(richtig):
    # Der Effekt ist mehr als nur ein grüner/roter Antwortbutton.
    # Es gibt Ton, großen Text und kurz veränderten Hintergrund.
    if richtig:
        farbe = "#0b5c0b"
        text = "✅ RICHTIG!"
    else:
        farbe = "#7a0000"
        text = "❌ FALSCH!"

    root.bell()

    root.configure(bg=farbe)
    titel_label.config(bg=farbe)
    untertitel_label.config(bg=farbe)
    info_label.config(bg=farbe)
    punkte_label.config(bg=farbe)
    timer_label.config(bg=farbe)
    frage_label.config(bg=farbe)
    antwort_frame.config(bg=farbe)
    joker_frame.config(bg=farbe)
    hilfe_label.config(bg=farbe)

    frage_label.config(text=text, font=("Arial", 28, "bold"))

    root.after(500, farbe_zuruecksetzen)


# =========================
# Spiellogik
# =========================

def starte_spieler_runde():
    global spieler_name, punkte, frage_index, spiel_fragen, timer_id
    global aktueller_spieler_index

    if aktueller_spieler_index >= len(spieler_liste):
        spiel_komplett_beenden()
        return

    spieler_name = spieler_liste[aktueller_spieler_index]["name"]
    punkte = 0
    frage_index = 0
    spiel_fragen = waehle_spiel_fragen()

    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    reset_joker()

    messagebox.showinfo("Spielstart", f"{spieler_name} ist dran!")

    zeige_frage()


def zeige_frage():
    global timer, timer_id, antwort_gesperrt

    # Bei jeder neuen Frage darf wieder geantwortet werden.
    antwort_gesperrt = False

    # Alte Timer werden gestoppt, damit nicht mehrere Timer gleichzeitig laufen.
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    frage = spiel_fragen[frage_index]
    schwierigkeitsgrad = aktuelle_schwierigkeit()

    info_label.config(
        text=f"Spieler: {spieler_name} | Modus: {modus} | Schwierigkeit: {schwierigkeitsgrad}"
    )

    punkte_label.config(text=f"Punkte: {punkte}")

    frage_label.config(
        text=f"Frage {frage_index + 1}/9:\n{frage['frage']}",
        font=("Arial", 20)
    )

    antworten = frage["antworten"][:]
    random.shuffle(antworten)

    for i in range(4):
        antwort_buttons[i].config(
            text=antworten[i],
            bg="#004C99",
            fg="white",
            relief="raised",
            bd=4
        )

        # Bei Labels gibt es kein command=...
        # Deshalb verbinden wir den Mausklick mit bind().
        antwort_buttons[i].bind(
            "<Button-1>",
            lambda event, antwort=antworten[i]: pruefe_antwort(antwort)
        )

    timer = ZEITLIMIT[modus][schwierigkeitsgrad]
    timer_label.config(text=f"Zeit: {timer}")

    starte_timer()


def starte_timer():
    global timer, timer_id, antwort_gesperrt

    timer_label.config(text=f"Zeit: {timer}")

    if timer <= 0:
        antwort_gesperrt = True
        timer_id = None

        for button in antwort_buttons:
            # Bei Labels entfernen wir die Klick-Funktion mit unbind().
            button.unbind("<Button-1>")

        frage_label.config(text="⏰ ZEIT VORBEI!\n\nDas Spiel endet.")
        messagebox.showerror("Zeit vorbei", "Du warst zu langsam!")
        root.after(1000, spieler_runde_beenden)
    else:
        timer -= 1
        timer_id = root.after(1000, starte_timer)


def pruefe_antwort(auswahl):
    global punkte, frage_index, timer_id, antwort_gesperrt

    # Falls schon geantwortet wurde, passiert nichts mehr.
    # So bleiben die Buttons sichtbar und müssen nicht deaktiviert werden.
    if antwort_gesperrt:
        return

    antwort_gesperrt = True

    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    frage = spiel_fragen[frage_index]
    richtige_antwort = frage["richtig"]
    schwierigkeitsgrad = aktuelle_schwierigkeit()

    for button in antwort_buttons:
        # Nach einer Antwort sollen die Antwortfelder nicht mehr klickbar sein.
        button.unbind("<Button-1>")

    if auswahl == richtige_antwort:
        punkte += PUNKTE[schwierigkeitsgrad]
        punkte_label.config(text=f"Punkte: {punkte}")

        for button in antwort_buttons:
            if button["text"] == auswahl:
                button.config(bg="green", fg="white")

        zeige_effekt(True)

        root.after(
            600,
            lambda: frage_label.config(
                text=f"✅ RICHTIG!\n\n+{PUNKTE[schwierigkeitsgrad]} Punkte"
            )
        )

        root.after(1600, naechste_frage)

    else:
        for button in antwort_buttons:
            if button["text"] == auswahl:
                button.config(bg="red", fg="white")

            if button["text"] == richtige_antwort:
                button.config(bg="green", fg="white")

        zeige_effekt(False)

        root.after(
            600,
            lambda: frage_label.config(
                text=f"❌ FALSCH!\n\nRichtige Antwort: {richtige_antwort}"
            )
        )

        root.after(2000, spieler_runde_beenden)


def naechste_frage():
    global frage_index

    frage_index += 1

    if frage_index >= len(spiel_fragen):
        spieler_runde_beenden()
    else:
        zeige_frage()


def spieler_runde_beenden():
    global aktueller_spieler_index

    spieler_liste[aktueller_spieler_index]["punkte"] = punkte

    speichere_highscore(spieler_name, punkte, modus)

    messagebox.showinfo(
        "Runde beendet",
        f"{spieler_name} hat {punkte} Punkte erreicht."
    )

    aktueller_spieler_index += 1
    starte_spieler_runde()


def spiel_komplett_beenden():
    sortierte_spieler = sorted(
        spieler_liste,
        key=lambda spieler: spieler["punkte"],
        reverse=True
    )

    text = "ENDERGEBNIS\n\n"

    for platz, spieler in enumerate(sortierte_spieler, start=1):
        text += f"{platz}. {spieler['name']} - {spieler['punkte']} Punkte\n"

    if len(sortierte_spieler) == 2:
        if sortierte_spieler[0]["punkte"] > sortierte_spieler[1]["punkte"]:
            text += f"\nGewinner: {sortierte_spieler[0]['name']}"
        else:
            text += "\nUnentschieden"

    messagebox.showinfo("Spiel beendet", text)
    zeige_highscores()
    root.destroy()


# =========================
# Joker
# =========================

def joker_5050():
    global joker_5050_verfuegbar

    if not joker_5050_verfuegbar:
        messagebox.showwarning("Joker", "50:50 Joker wurde schon benutzt!")
        return

    frage = spiel_fragen[frage_index]
    richtige_antwort = frage["richtig"]

    falsche_buttons = []

    for button in antwort_buttons:
        if button["text"] != richtige_antwort and button["text"] != "---":
            falsche_buttons.append(button)

    # Zwei falsche Antworten werden entfernt.
    for button in random.sample(falsche_buttons, 2):
        button.config(
            text="---",
            bg="#333333",
            fg="white"
        )

        # Entfernte Antwort darf nicht mehr anklickbar sein.
        button.unbind("<Button-1>")

    joker_5050_verfuegbar = False
    joker_5050_button.config(state="disabled")


def anrufjoker():
    global joker_anruf_verfuegbar

    if not joker_anruf_verfuegbar:
        messagebox.showwarning("Joker", "Anrufjoker wurde schon benutzt!")
        return

    frage = spiel_fragen[frage_index]
    richtige_antwort = frage["richtig"]

    # Der Anrufjoker gibt nur einen Hinweis und verrät nicht direkt die Lösung.
    hinweise = [
        f"Die richtige Antwort beginnt mit: {richtige_antwort[0]}",
        f"Die richtige Antwort besteht aus {len(richtige_antwort.split())} Wort/Wörtern.",
        "Die richtige Antwort passt am besten zum Thema TH OWL / Herford.",
        "Ich würde die fachlich passendste Antwort nehmen."
    ]

    messagebox.showinfo(
        "Anrufjoker",
        "📞 Dein Anrufjoker sagt:\n\n" + random.choice(hinweise)
    )

    joker_anruf_verfuegbar = False
    joker_anruf_button.config(state="disabled")


def zeitjoker():
    global timer, joker_zeit_verfuegbar

    if not joker_zeit_verfuegbar:
        messagebox.showwarning("Joker", "Zeitjoker wurde schon benutzt!")
        return

    timer += 10
    timer_label.config(text=f"Zeit: {timer}")

    joker_zeit_verfuegbar = False
    joker_zeit_button.config(state="disabled")

    messagebox.showinfo("Zeitjoker", "Du hast 10 Sekunden extra bekommen!")

def frage_wechseln_joker():
    global joker_switch_verfuegbar, spiel_fragen

    if not joker_switch_verfuegbar:
        messagebox.showwarning("Joker", "Frage-wechseln-Joker wurde schon benutzt!")
        return

    schwierigkeitsgrad = aktuelle_schwierigkeit()

    moegliche_fragen = []

    # Es wird eine neue Frage mit derselben Schwierigkeit gesucht.
    for frage in fragen[schwierigkeitsgrad]:
        if frage not in spiel_fragen:
            moegliche_fragen.append(frage)

    if not moegliche_fragen:
        messagebox.showwarning(
            "Joker",
            "Keine weitere Frage auf diesem Niveau verfügbar!"
        )
        return

    neue_frage = random.choice(moegliche_fragen)
    spiel_fragen[frage_index] = neue_frage

    joker_switch_verfuegbar = False
    joker_switch_button.config(state="disabled")

    messagebox.showinfo(
        "Frage wechseln",
        "Die Frage wurde durch eine neue Frage im gleichen Schwierigkeitsgrad ersetzt."
    )

    zeige_frage()


# =========================
# Tastatursteuerung
# =========================

def taste(event):
    taste = event.char.lower()

    if taste in ["1", "2", "3", "4"]:
        index = int(taste) - 1
        antwort = antwort_buttons[index]["text"]

        if antwort != "---":
            pruefe_antwort(antwort)

    elif taste == "f":
        joker_5050()

    elif taste == "a":
        anrufjoker()

    elif taste == "z":
        zeitjoker()

    elif taste == "w":
        frage_wechseln_joker()


# =========================
# Programmstart
# =========================

root.bind_all("<Key>", taste)

start_abfragen()
starte_spieler_runde()

root.mainloop()