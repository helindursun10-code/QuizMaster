import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json
import os


# =========================
# Einstellungen
# =========================

HIGHSCORE_DATEI = "highscores.json"

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
            "richtig": "Technische Hochschule Ostwestfalen-Lippe",
            "hinweis": "Ich glaube OWL steht für Ostwestfalen-Lippe."
        },
        {
            "frage": "Wie heißt der TH-OWL-Lernort in Herford?",
            "antworten": [
                "Innovation Campus",
                "Kreativ Campus",
                "BildungsCampus",
                "Sustainable Campus"
            ],
            "richtig": "BildungsCampus",
            "hinweis": "Der Name beschriebt klar den Fokus auf Lehre und Studium in Herford."
        },
        {
            "frage": "In welchem Bundesland liegt Herford?",
            "antworten": [
                "Berlin",
                "Bremen",
                "NRW",
                "Niedersachsen"
            ],
            "richtig": "NRW",
            "hinweis": "Es ist das bevölkerungsriechste BUndesland Deutschlands."
        },
        {
            "frage": "In welcher Stadt befindet sich der BildungsCampus der TH OWL?",
            "antworten": [
                "Lemgo",
                "Herford",
                "Minden",
                "Höxter"
            ],
            "richtig": "Herford",
            "hinweis": " ich weiss das Lemgo, Detmold und Höxter Hauptstandorte sind."
        },
        {
            "frage": "Wie nennt sich die Stadt Herford offiziell?",
            "antworten": [
                "Universitätsstadt Herford",
                "Landeshauptstadt Herford",
                "Kurstadt Herford",
                "Hansestadt Herford"
            ],
            "richtig": "Hansestadt Herford",
            "hinweis": "Der Name geht auf einen mittelalterlichen Städtebund zurück, der für Handel und Wirtschaft wichtig war."
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
            "richtig": "Digital Management Solutions",
            "hinweis": "Die Abkürzung von dem Studiengang ist DiMS."
        },
        {
            "frage": "Welche drei Orte nennt die TH OWL als Hauptstandorte?",
            "antworten": [
                "Herford, Minden und Detmold",
                "Lemgo, Detmold und Höxter",
                "Lemgo, Herford und Minden",
                "Detmold, Herford und Höxter"
            ],
            "richtig": "Lemgo, Detmold und Höxter",
            "hinweis": "Die Hauptsandorte sind Campusstandorte, die nicht gesuchten Orte sind für Lern- oder Projektstandorte."
        },
        {
            "frage": "Welcher Campusname gehört zur TH OWL in Lemgo?",
            "antworten": [
                "Kreativ Campus",
                "Sustainable Campus",
                "Innovation Campus",
                "RailCampus"
            ],
            "richtig": "Innovation Campus",
            "hinweis": "In Lemgo gibt es ein InnovationSPIN"
        },
        {
            "frage": "Welche Aussage passt zum Studienangebot der TH OWL?",
            "antworten": [
                "Nur Master",
                "Nur Ausbildung",
                "Bachelor & Master",
                "Nur Schulungen"
            ],
            "richtig": "Bachelor & Master",
            "hinweis": "Das Angebot deckt sowohl grundlegende als auch weiterführende akademische Studiengänge ab."
        },
        {
            "frage": "An welcher Straße liegt der BildungsCampus Herford?",
            "antworten": [
                "Berliner Straße",
                "Mary-Somerville-Boulevard",
                "Bahnhofstraße",
                "Campusallee"
            ],
            "richtig": "Mary-Somerville-Boulevard",
            "hinweis": "Viele Straßen im Campusgebiet sind nach bedeutenden Persönlichkeiten aus Wissenschaft und Geschichte benannt."
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
            "richtig": "Britische Kaserne",
            "hinweis": "Der BildungsCampus wurde auf einem ehemaligen militärischen Standort errichtet."
        },
        {
            "frage": "Wie finden die Vorlesungen bei DiMS statt?",
            "antworten": [
                "Täglich vor Ort",
                "Im Labor",
                "Online und Präsenz",
                "Nur Online"
            ],
            "richtig": "Digital mit Präsenz",
            "hinweis": "Man kann an den Volesungen ganz flexibel teilnhemen."
        },
        {
            "frage": "Welche Aussage beschreibt die Rolle von Herford innerhalb der TH OWL am genauesten?",
            "antworten": [
                "Hauptsitz",
                "einziger Campus",
                "Lernort",
                "kein Standort"
            ],
            "richtig": "Lernort",
            "hinweis": "Der Standort ist Teil der Hochschule, dient jedoch vor allem als ergänzender Studienort."
        },
        {
            "frage": "Welche Haltestelle liegt nahe am BildungsCampus?",
            "antworten": [
                "Rathausplatz",
                "Alter Markt",
                "Vlothoer Str./Kaserne",
                "Bahnhof Süd"
            ],
            "richtig": "Vlothoer Str./Kaserne",
            "hinweis": "Der BildungsCampus war eine Militärgelände."
        },
        {
            "frage": "Welche Zuordnung von Campusname und Stadt ist korrekt?",
            "antworten": [
                "Sustainable Campus Höxter"
                "Campus Detmold"
                "Lemgo Innovation Campus"
                "Herford BildungsCampus"
            ],
            "richtig": "Sustainable Campus Höxter",
            "hinweis": "Ein Standort ist besonders nachhaltig ausgerichtet"
        }
    ]
}


# =========================
# Globale Spielvariablen
# =========================

spieler_liste = [] #Liste speichert alle spieler + Punkte
aktueller_spieler_index = 0 #welcher spieler ist an der Reihe 1 oder 2

spieler_name = ""
modus = "Fair" #spieler wählt hard oder fair modus

spiel_fragen = [] #enthält die gestellte Frage
frage_index = 0 #wievielte Frage z.B. 1/9
punkte = 0
timer = 0
#speichert die ID des Laufenden Timers
#kann später gestoppt oder neu egstrtet werden
timer_id = None

# =========================
# Joker
# =========================
# Jeder Joker kann nur einmal pro Spiel verwendet werden
# True = Joker ist noch verfügbar
# False = Joker wurde bereits benutzt

joker_5050_verfuegbar = True
joker_anruf_verfuegbar = True
joker_zeit_verfuegbar = True
joker_switch_verfuegbar = True

# Verhindert, dass man nach einer Antwort nochmal klicken kann
# Die Buttons bleiben aber farbig und lesbar
antwort_gesperrt = False

antwort_buttons = [] # Liste mit den vier Antwortbuttons


# =========================
# Highscore-Funktionen
# =========================

def lade_highscores(): # Liest die gespeicherten Highscores aus der JSON-Datei ein.
    if not os.path.exists(HIGHSCORE_DATEI):# Existiert die Datei noch nicht, wird eine leere Liste zurückgegeben
        return []

    try:

        with open(HIGHSCORE_DATEI, "r", encoding="utf-8") as datei:

            daten = json.load(datei)# Wandelt den Inhalt der JSON-Datei in eine Python-Liste um

            if not isinstance(daten, list): # Sicherheitsprüfung: Es wird überprüft, ob die geladenen Daten tatsächlich eine Liste sind
                return []

            return daten# Gibt die gelesenen Highscores zurück.

    except Exception: #Bei Fehler leere Liste zurückgeben

        return []


def speichere_highscores(daten):# Speichert die Highscore-Liste dauerhaft in der JSON-Datei
    with open(HIGHSCORE_DATEI, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, indent=4, ensure_ascii=False)# Wandelt die Python-Liste in das JSON-Format um und speichert sie in der Datei.


def speichere_highscore(name, punkte_anzahl, spielmodus): # Neuer Punktestand wird zur Rangliste hinzugefügt.
    daten = lade_highscores()

    daten.append({  # Neuen Eintrag mit Name, Punkten und Spielmodus hinzufügen.
        "name": name,
        "punkte": punkte_anzahl,
        "modus": spielmodus
    })

    #Höchste Punktzahl steht oben.
    daten = sorted(daten, key=lambda eintrag: eintrag["punkte"], reverse=True)

    speichere_highscores(daten)#Aktualisierte Rangliste speichern.


def zeige_highscores():
    daten = lade_highscores() # Lädt die gespeicherten Highscores.

    if not daten:# Falls noch keine Highscores vorhanden sind, wird eine entsprechende Meldung angezeigt.
        messagebox.showinfo(
            "Rangliste",
            "Noch keine Highscores vorhanden.\nSpiele zuerst eine Runde."
        )
        return

    text = "RANGLISTE\n\n"    # Überschrift für die Rangliste.

    for platz, eintrag in enumerate(daten[:10], start=1):# Erstellt die Top-10-Liste mit Platzierung, Name, Punktzahl und Spielmodus
        text += f"{platz}. {eintrag['name']} - {eintrag['punkte']} Punkte ({eintrag['modus']})\n"

    messagebox.showinfo("Rangliste", text) # Zeigt die Rangliste in einem Dialogfenster an


# =========================
# Hilfsfunktionen
# =========================

def waehle_spiel_fragen():
    # Es werden 3 einfache, 3 mittlere und 3 schwere Fragen gewählt
    # Dadurch steigt die Schwierigkeit im Spiel
    return (
        random.sample(fragen["einfach"], 3) +
        random.sample(fragen["mittel"], 3) +
        random.sample(fragen["schwer"], 3)
    )


def aktuelle_schwierigkeit(): # Bestimmt die aktuelle Schwierigkeitsstufe abhängig von der Frage-Position
    # Frage 1-3: einfach
    # Frage 4-6: mittel
    # Frage 7-9: schwer
    if frage_index < 3: # Frage 1–3 → einfach
        return "einfach"
    elif frage_index < 6: #Frage 4–6 → mittel
        return "mittel"
    else:                  #Frage 7–9 → schwer
        return "schwer"


def reset_joker():
    global joker_5050_verfuegbar, joker_anruf_verfuegbar # Setzt alle Joker wieder auf "verfügbar" zu beginn jedes Spiels
    global joker_zeit_verfuegbar, joker_switch_verfuegbar

    joker_5050_verfuegbar = True  # Alle Joker werden zurückgesetzt für die neue Runde (Logik)
    joker_anruf_verfuegbar = True
    joker_zeit_verfuegbar = True
    joker_switch_verfuegbar = True

    joker_5050_button.config(state="normal")  #Die Buttons im UI werden wieder aktiviert,damit der Spieler sie erneut klicken kann.
    joker_anruf_button.config(state="normal")
    joker_zeit_button.config(state="normal")
    joker_switch_button.config(state="normal")


# =========================
# Startabfragen
# =========================

def start_abfragen():
    global spieler_liste, modus

    anzahl = simpledialog.askinteger( # Fragt den Spieler, wie viele Personen mitspielen sollen (1 oder 2).
        "Spieleranzahl",         # Die Eingabe erfolgt über ein Eingabefenster (GUI).
        "Wie viele Spieler? 1 oder 2:"
    )

    if anzahl not in [1, 2]:     # Falls eine ungültige Eingabe gemacht wird (z. B. None oder 3),
        anzahl = 1              # wird automatisch auf 1 Spieler gesetzt.

    for nummer in range(anzahl):# Erstellt für jeden Spieler einen Eintrag in der Spielerliste.
        name = simpledialog.askstring( #Fragt den Namen des jeweiligen Spielers ab.
            "Spielername",
            f"Name Spieler {nummer + 1}:"
        )

        if not name: # Falls kein Name eingegeben wird, wird ein Standardname gesetzt.
            name = f"Spieler {nummer + 1}"

        spieler_liste.append({ # Speichert Spielername und Startpunkte in der Liste.
            "name": name,
            "punkte": 0
        })

    gewaehlter_modus = simpledialog.askstring( # Abfrage des Spielmodus (Fair oder Hard)
        "Spielmodus",
        "Wähle Modus: Fair oder Hard:"
    )

    # Die Eingabe wird bereinigt, damit auch "fair", "FAIR" oder Leerzeichen funktionieren.
    # Wenn die Eingabe ungültig ist, wird automatisch der Fair-Mode genutzt.
    if not gewaehlter_modus:
        gewaehlter_modus = "Fair"
    else:
        gewaehlter_modus = gewaehlter_modus.strip().capitalize()

    if gewaehlter_modus not in ["Fair", "Hard"]:
        gewaehlter_modus = "Fair"

    modus = gewaehlter_modus # Speichert den gewählten Spielmodus global,
                            #damit er im gesamten Spiel verwendet werden kann.


# =========================
# Oberfläche
# =========================

root = tk.Tk() # Erstellt das Hauptfenster der Anwendung
root.title("QuizMaster - TH OWL & Herford Edition") # Gibt den Fenstertitel am
root.geometry("950x720") # Gibt die Fenstergröße (Breite x Höhe) an
root.configure(bg="#001f3f") #Legt die Hintergrundfarbe des gesamten Fensters fest

# =========================
# Titelbereich
# =========================

titel_label = tk.Label( # Haupttitel des Spiels
    root,
    text="QUIZMASTER",
    font=("Arial", 30, "bold"),
    fg="gold",
    bg="#001f3f"
)
titel_label.pack(pady=10)

untertitel_label = tk.Label( # Untertitel unter dem Haupttitel
    root,
    text="TH OWL & Herford Edition",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#001f3f"
)
untertitel_label.pack()

info_label = tk.Label( # Infoanzeige (z. B. aktueller Spieler oder Hinweise)
    root,
    text="",
    font=("Arial", 15),
    fg="white",
    bg="#001f3f"
)
info_label.pack(pady=10)

punkte_label = tk.Label( # Anzeige der aktuellen Punkte
    root,
    text="Punkte: 0",
    font=("Arial", 16),
    fg="white",
    bg="#001f3f"
)
punkte_label.pack()

timer_label = tk.Label( # Anzeige des Timers für die aktuelle Frage
    root,
    text="Zeit: 0",
    font=("Arial", 18, "bold"),
    fg="red",
    bg="#001f3f"
)
timer_label.pack(pady=10)

frage_label = tk.Label( # Anzeige der aktuellen Frage
    root,
    text="",
    wraplength=800, # Zeilenumbruch nach 800 Pixeln
    font=("Arial", 20),
    fg="white",
    bg="#001f3f"
)
frage_label.pack(pady=20)

# =========================
# Antwortbereich
# =========================

antwort_frame = tk.Frame(root, bg="#001f3f") # Box für die Antwortbuttons
antwort_frame.pack()

antwort_frame.grid_columnconfigure(0, weight=1, minsize=350)# Linke Antwortspalte erhält eine Mindestbreite von 350 Pixeln.
antwort_frame.grid_columnconfigure(1, weight=1, minsize=350)# Rechte Antwortspalte erhält dieselbe Mindestbreite.

for i in range(4): # Erstellt 4 Antwortbuttons
    button = tk.Button(
        antwort_frame,
        text="",
        width=38,
        height=2,
        wraplength=320,
        font=("Arial", 14, "bold"),
        bg="#004C99",
        fg="black"
    )
    button.grid( # Positionierung im Raster (2x2 Layout)
        row=i // 2,
        column=i % 2,
        padx=15,
        pady=15,
        sticky="nsew"
    )
    antwort_buttons.append(button) # Speichert alle Buttons in einer Liste für spätere Änderungen

# =========================
# Joker-Bereich
# =========================

joker_frame = tk.Frame(root, bg="#001f3f") #Box für Joker-Buttons
joker_frame.pack(pady=20)

joker_5050_button = tk.Button( # 50:50 Joker Button
    joker_frame,
    text="50:50 Joker",
    font=("Arial", 14),
    command=lambda: joker_5050()
)
joker_5050_button.grid(row=0, column=0, padx=10)

joker_anruf_button = tk.Button( # Anrufjoker Button
    joker_frame,
    text="Anrufjoker",
    font=("Arial", 14),
    command=lambda: anrufjoker()
)
joker_anruf_button.grid(row=0, column=1, padx=10)

joker_zeit_button = tk.Button( # Zeitjoker Button
    joker_frame,
    text="Zeitjoker +10s",
    font=("Arial", 14),
    command=lambda: zeitjoker()
)
joker_zeit_button.grid(row=0, column=2, padx=10)

joker_switch_button = tk.Button(  # Fragewechsel-Joker Button
    joker_frame,
    text="Frage wechseln",
    font=("Arial", 14),
    command=lambda: frage_wechseln_joker()
)
joker_switch_button.grid(row=0, column=3, padx=10)

# =========================
# Highscore Button
# =========================

highscore_button = tk.Button( # Öffnet die Rangliste (Highscores)
    root,
    text="Rangliste anzeigen",
    font=("Arial", 14),
    command=zeige_highscores
)
highscore_button.pack(pady=5)

# =========================
# Hilfe / Steuerung
# =========================

hilfe_label = tk.Label( # Zeigt Tastenkürzel für das Spiel an
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
    # Nach dem Effekt (richtig/falsch) wird die normale Hintergrundfarbe wiederhergestellt
    normale_farbe = "#001f3f"

    root.configure(bg=normale_farbe) # Alle UI-Elemente bekommen wieder die Standard-Hintergrundfarbe
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
    # Zeigt einen visuellen und akustischen Effekt,
    # wenn der Spieler eine Antwort auswählt
    # Dabei wird unterschieden, ob die Antwort richtig oder falsch ist

    if richtig:   # Grün für richtige Antwort
        farbe = "#0b5c0b"
        text = "✅ RICHTIG!"
    else:        # Rot für falsche Antwort
        farbe = "#7a0000"
        text = "❌ FALSCH!"

    root.bell() # Gibt einen kurzen Soundeffekt aus (System-Bell)

    # Ändert die Hintergrundfarbe aller UI-Elemente,
    # um den Erfolg/Misserfolg visuell darzustellen
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

    frage_label.config(text=text, font=("Arial", 28, "bold")) #Eine sehr auffällige, gut sichtbare Rückmeldung direkt nach Eingabe der Antwort

    root.after(500, farbe_zuruecksetzen) # Nach 500 Millisekunden wird die normale Farbe wiederhergestellt


# =========================
# Spiellogik
# =========================

def starte_spieler_runde(): # Startet die Spielrunde für den aktuellen Spieler
    global spieler_name, punkte, frage_index, spiel_fragen, timer_id
    global aktueller_spieler_index

    if aktueller_spieler_index >= len(spieler_liste): # Wenn keine Spieler mehr übrig sind, wird das Spiel beendet
        spiel_komplett_beenden()
        return

    spieler_name = spieler_liste[aktueller_spieler_index]["name"] # Holt den Namen des Spielers, der aktuell an der Reihe ist, aus der Spielerliste
    punkte = 0# Setzt den Punktestand für die neue Spielrunde des nächsten Spielers zurück
    frage_index = 0 # Setzt den Fragenzähler für die neue Spielrunde des nächsten Spielers zurück
    spiel_fragen = waehle_spiel_fragen() # Wählt neue zufällige Fragen für die Runde aus

    if timer_id is not None:# Stoppt eventuell laufenden Timer aus vorheriger Runde
        root.after_cancel(timer_id)
        timer_id = None

    reset_joker()    # Setzt alle Joker zurück

    messagebox.showinfo("Spielstart", f"{spieler_name} ist dran!") # Informiert den Spieler, dass seine Runde beginnt

    zeige_frage() # Zeigt die erste Frage


def zeige_frage(): # Zeigt die aktuelle Frage und die Antwortmöglichkeiten an.
    global timer, timer_id, antwort_gesperrt

    # Bei jeder neuen Frage darf wieder geantwortet werden.
    antwort_gesperrt = False

    # Alte Timer werden gestoppt, damit nicht mehrere Timer gleichzeitig laufen.
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    frage = spiel_fragen[frage_index] # Holt neue Frage aus der Fragenliste
    schwierigkeitsgrad = aktuelle_schwierigkeit() # Bestimmt die aktuelle Schwierigkeit

    info_label.config(  # Aktualisiert Infoanzeige (Spieler, Modus, Schwierigkeit)
        text=f"Spieler: {spieler_name} | Modus: {modus} | Schwierigkeit: {schwierigkeitsgrad}"
    )

    punkte_label.config(text=f"Punkte: {punkte}") # Aktualisiert Punktestand im UI

    frage_label.config( # Zeigt Frage im Label an
        text=f"Frage {frage_index + 1}/9:\n{frage['frage']}",
        font=("Arial", 20)
    )

    antworten = frage["antworten"][:] # Mischt die Antwortmöglichkeiten zufällig
    random.shuffle(antworten)

    for i in range(4): # Erstellt die Antwortbuttons neu
        antwort_buttons[i].config(
            text=antworten[i],
            bg="#004C99",
            fg="black",
            activebackground="#0066CC",
            activeforeground="black",
            state="normal",
            command=lambda antwort=antworten[i]: pruefe_antwort(antwort)
        )

    timer = ZEITLIMIT[modus][schwierigkeitsgrad] # Setzt Timer abhängig von Modus und Schwierigkeit
    timer_label.config(text=f"Zeit: {timer}")

    starte_timer() # Startet den Countdown


def starte_timer(): # Verwaltet den Countdown-Timer für jede Frage
    global timer, timer_id, antwort_gesperrt

    timer_label.config(text=f"Zeit: {timer}")

    if timer <= 0: # Wenn Zeit abgelaufen ist
        antwort_gesperrt = True # keine Antwort mehr möglich
        timer_id = None

        for button in antwort_buttons:  # Deaktiviert alle Antwortbuttons
            button.config(command=lambda: None)

        frage_label.config(text="⏰ ZEIT VORBEI!\n\nDas Spiel endet.") # Zeigt Zeit-abgelaufen Nachricht
        messagebox.showerror("Zeit vorbei", "Du warst zu langsam!")
        root.after(1000, spieler_runde_beenden)
    else:
        timer -= 1 # Timer läuft weiter runter
        timer_id = root.after(1000, starte_timer) # Ruft Funktion nach 1 Sekunde erneut auf


def pruefe_antwort(auswahl): # Prüft, ob die ausgewählte Antwort richtig oder falsch ist
    global punkte, frage_index, timer_id, antwort_gesperrt

    # Falls schon geantwortet wurde, passiert nichts mehr.
    # So bleiben die Buttons sichtbar und müssen nicht deaktiviert werden.
    if antwort_gesperrt:
        return

    antwort_gesperrt = True

    if timer_id is not None: # Stoppt den Timer
        root.after_cancel(timer_id)
        timer_id = None

    frage = spiel_fragen[frage_index] # Aktuelle Frage und richtige Antwort
    richtige_antwort = frage["richtig"]
    schwierigkeitsgrad = aktuelle_schwierigkeit()

    # Nach einer Antwort werden nur die Klick-Funktionen entfernt.
    # Die Farben bleiben sichtbar.
    for button in antwort_buttons:
        button.config(command=lambda: None)

    if auswahl == richtige_antwort:  # Wenn Antwort richtig ist
        punkte += PUNKTE[schwierigkeitsgrad]
        punkte_label.config(text=f"Punkte: {punkte}")

        for button in antwort_buttons:  # Markiert richtige Antwort grün
            if button["text"] == auswahl:
                button.config(bg="#00cc44", fg="black", font=("Arial", 16, "bold"))

        zeige_effekt(True)  # Zeigt visuellen Effekt

        root.after( # Zeigt kurze Erfolgsmeldung
            600,
            lambda: frage_label.config(
                text=f"✅ RICHTIG!\n\n+{PUNKTE[schwierigkeitsgrad]} Punkte"
            )
        )

        root.after(   # Geht zur nächsten Frage
            1600,
            naechste_frage
        )

    else: # Wenn Antwort falsch ist
        for button in antwort_buttons: # Markiert falsche Antwort rot und richtige grün
            if button["text"] == auswahl:
                button.config(bg="#cc0000", fg="white", font=("Arial", 16, "bold"))

            if button["text"] == richtige_antwort:
                button.config(bg="#00cc44", fg="black", font=("Arial", 16, "bold"))

        zeige_effekt(False) # Zeigt Fehler-Effekt

        root.after(  # Zeigt richtige Antwort im Text
            600,
            lambda: frage_label.config(
                text=f"❌ FALSCH!\n\nRichtige Antwort: {richtige_antwort}"
            )
        )

        root.after(2000, spieler_runde_beenden)  # Beendet die Runde nach falscher Antwort


def naechste_frage(): # Wechselt zur nächsten Frage im Spiel
    global frage_index

    frage_index += 1

    if frage_index >= len(spiel_fragen): # Wenn keine Fragen mehr übrig sind, Runde beenden
        spieler_runde_beenden()
    else: # Sonst nächste Frage anzeigen
        zeige_frage()


def spieler_runde_beenden(): # Beendet die Runde eines Spielers
    global aktueller_spieler_index

    spieler_liste[aktueller_spieler_index]["punkte"] = punkte # Speichert Punkte des Spielers

    speichere_highscore(spieler_name, punkte, modus) # Speichert Highscore in Datei

    messagebox.showinfo( # Zeigt Ergebnis der Runde
        "Runde beendet",
        f"{spieler_name} hat {punkte} Punkte erreicht."
    )

    aktueller_spieler_index += 1  # Nächster Spieler ist dran
    starte_spieler_runde()


def spiel_komplett_beenden():  # Beendet das gesamte Spiel nach allen Spielern
    sortierte_spieler = sorted( # Sortiert Spieler nach Punkten (höchste zuerst)
        spieler_liste,
        key=lambda spieler: spieler["punkte"],
        reverse=True
    )

    text = "ENDERGEBNIS\n\n"  # Erstellt Ergebnistext

    for platz, spieler in enumerate(sortierte_spieler, start=1):
        text += f"{platz}. {spieler['name']} - {spieler['punkte']} Punkte\n"

    if len(sortierte_spieler) == 2:  # Wenn zwei Spieler vorhanden sind, Gewinner bestimmen
        if sortierte_spieler[0]["punkte"] > sortierte_spieler[1]["punkte"]:
            text += f"\nGewinner: {sortierte_spieler[0]['name']}"
        else:
            text += "\nUnentschieden"

    messagebox.showinfo("Spiel beendet", text) # Zeigt Endergebnis
    zeige_highscores() # Zeigt Highscore-Liste

# =========================
# Joker
# =========================

def joker_5050():
    global joker_5050_verfuegbar

    if not joker_5050_verfuegbar: # Prüft, ob der Joker bereits verwendet wurde
        messagebox.showwarning("Joker", "50:50 Joker wurde schon benutzt!")
        return

    frage = spiel_fragen[frage_index] # Holt die aktuelle Frage und die richtige Antwort
    richtige_antwort = frage["richtig"]

    falsche_buttons = [] # Speichert alle Buttons mit falschen Antworten

    for button in antwort_buttons:
        if button["text"] != richtige_antwort and button["text"] != "---":
            falsche_buttons.append(button)

    # Zwei falsche Antworten werden entfernt.
    for button in random.sample(falsche_buttons, 2):
        button.config(
            text="---",
            bg="#333333",
            fg="white",
            command=lambda: None
        )

    joker_5050_verfuegbar = False
    joker_5050_button.config(state="disabled")


def anrufjoker(): # Prüft, ob der Joker bereits verwendet wurde
    global joker_anruf_verfuegbar

    if not joker_anruf_verfuegbar:
        messagebox.showwarning(
            "Joker",
            "Anrufjoker wurde schon benutzt!"
        )
        return

    frage = spiel_fragen[frage_index] # Holt die aktuelle Frage

    messagebox.showinfo( # Zeigt den gespeicherten Hinweis zur aktuellen Frage an
        "Anrufjoker",
        "📞 Dein Anrufjoker sagt:\n\n" + frage["hinweis"]
    )

    joker_anruf_verfuegbar = False # Joker als benutzt markieren und Button deaktivieren
    joker_anruf_button.config(state="disabled")


def zeitjoker():
    global timer, joker_zeit_verfuegbar

    if not joker_zeit_verfuegbar: # Prüft, ob der Joker bereits verwendet wurde
        messagebox.showwarning("Joker", "Zeitjoker wurde schon benutzt!")
        return

    timer += 10 # Erhöht die verbleibende Zeit um 10 Sekunden
    timer_label.config(text=f"Zeit: {timer}")

    joker_zeit_verfuegbar = False # Joker als benutzt markieren und Button deaktivieren
    joker_zeit_button.config(state="disabled")

    messagebox.showinfo("Zeitjoker", "Du hast 10 Sekunden extra bekommen!") # Informiert den Spieler über die zusätzliche Zeit

def frage_wechseln_joker():
    global joker_switch_verfuegbar, spiel_fragen

    if not joker_switch_verfuegbar: # Prüft, ob der Joker bereits verwendet wurde
        messagebox.showwarning("Joker", "Frage-wechseln-Joker wurde schon benutzt!")
        return

    schwierigkeitsgrad = aktuelle_schwierigkeit() # Ermittelt die Schwierigkeit der aktuellen Frage

    moegliche_fragen = []

    # Es wird eine neue Frage mit derselben Schwierigkeit gesucht.
    for frage in fragen[schwierigkeitsgrad]:
        if frage not in spiel_fragen:
            moegliche_fragen.append(frage)

    if not moegliche_fragen: # Falls keine passende Ersatzfrage vorhanden ist, wird der Spieler informiert.
        messagebox.showwarning(
            "Joker",
            "Keine weitere Frage auf diesem Niveau verfügbar!"
        )
        return

    neue_frage = random.choice(moegliche_fragen) # Wählt zufällig eine neue Frage aus und ersetzt die aktuelle
    spiel_fragen[frage_index] = neue_frage

    joker_switch_verfuegbar = False # Joker als benutzt markieren und Button deaktivieren
    joker_switch_button.config(state="disabled")

    messagebox.showinfo( # Informiert den Spieler über den Fragenwechsel
        "Frage wechseln",
        "Die Frage wurde durch eine neue Frage im gleichen Schwierigkeitsgrad ersetzt."
    )

    zeige_frage()


# =========================
# Tastatursteuerung
# =========================

def taste(event): # Liest die gedrückte Taste ein und wandelt sie in Kleinbuchstaben um
    taste = event.char.lower()

    if taste in ["1", "2", "3", "4"]: # Tasten 1 bis 4 wählen die entsprechende Antwort aus
        index = int(taste) - 1
        antwort = antwort_buttons[index]["text"]

        if antwort != "---": # Bereits entfernte Antworten ("---") können nicht ausgewählt werden
            pruefe_antwort(antwort)

    elif taste == "f": # Tastenkürzel für 50:50 Joker
        joker_5050()

    elif taste == "a": # Tastenkürzel für Anruf Joker
        anrufjoker()

    elif taste == "z":# Tastenkürzel für Zeit Joker
        zeitjoker()

    elif taste == "w":# Tastenkürzel für Frage wechseln Joker
        frage_wechseln_joker()


# =========================
# Programmstart
# =========================

root.bind_all("<Key>", taste) # Aktiviert die Tastatursteuerung für das gesamte Fenster

start_abfragen() # Fragt die Spielerinformationen und den Spielmodus ab
starte_spieler_runde() # Startet die erste Spielrunde

root.mainloop() # Startet die Ereignisschleife von Tkinter. Das Fenster bleibt geöffnet und reagiert auf Eingaben.
