# Tkinter wird für die grafische Benutzeroberfläche verwendet.
import tkinter as tk

# messagebox zeigt Hinweis-, Fehler- und Bestätigungsfenster.
# simpledialog wird für Texteingaben wie Name oder Spielmodus verwendet.
from tkinter import messagebox, simpledialog

# random wird für zufällige Fragen und gemischte Antworten verwendet.
import random

# json wird genutzt, um Highscores dauerhaft in einer JSON-Datei zu speichern.
import json

# os wird genutzt, um zu prüfen, ob die Highscore-Datei existiert.
import os


# =========================
# Einstellungen
# =========================

# Name der Datei, in der die Highscores dauerhaft gespeichert werden.
# Da nur ein Dateiname angegeben wird, liegt die Datei im Arbeitsordner des Programms.
HIGHSCORE_DATEI = "highscores.json"

# Projektname und Slogan werden an mehreren Stellen der Oberfläche verwendet.
PROJEKTNAME = "QuizMaster"
SLOGAN = "Wissen ist Millionen wert."

# Spielernamen dürfen höchstens 15 Zeichen lang sein.
MAX_NAME_LAENGE = 15

# Die Zeitlimits werden in einem verschachtelten Dictionary gespeichert.
# Erste Ebene: Spielmodus "Fair" oder "Hard".
# Zweite Ebene: Schwierigkeitsgrad der Frage.
# Der gespeicherte Zahlenwert entspricht den Sekunden pro Frage.
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

# Punkte pro Schwierigkeitsgrad.
# Über den Namen der Schwierigkeit kann später
# direkt auf den passenden Punktwert zugegriffen werden.
PUNKTE = {
    "einfach": 10,
    "mittel": 20,
    "schwer": 30
}


# =========================
# Fragen
# =========================
# Fragen nach Schwierigkeit geordnet.
# Jede Frage enthält Text, vier Antworten, richtige Lösung und Joker-Hinweis.

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
            "hinweis": "Der Name beschreibt klar den Fokus auf Lehre und Studium in Herford."
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
            "hinweis": "Es ist das bevölkerungsreichste Bundesland Deutschlands."
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
            "hinweis": "Ich weiß, dass Lemgo, Detmold und Höxter Hauptstandorte sind."
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
            "hinweis": "Die Hauptstandorte sind Campusstandorte. Andere Orte sind eher Lern- oder Projektstandorte."
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
            "hinweis": "In Lemgo gibt es den InnovationSPIN."
        },
        {
            "frage": "Welche Aussage passt zum Studienangebot der TH OWL?",
            "antworten": [
                "Nur Master",
                "Nur Ausbildung",
                "Bachelor & Master",
                "Nur Zertifikate"
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
            "frage": "Welche Aussage zur Studienorganisation in Herford ist am passendsten?",
            "antworten": [
                "Täglich vor Ort",
                "Nur Labor",
                "Digital mit Präsenz",
                "Ohne Digital"
            ],
            "richtig": "Digital mit Präsenz",
            "hinweis": "Man kann an den Vorlesungen flexibel teilnehmen."
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
            "hinweis": "Der BildungsCampus befindet sich auf einem ehemaligen Militärgelände."
        },
        {
            "frage": "Welche Zuordnung von Campusname und Stadt ist korrekt?",
            "antworten": [
                "Sustainable Campus Herford",
                "Sustainable Campus Detmold",
                "Sustainable Campus Höxter",
                "Sustainable Campus Lemgo"
            ],
            "richtig": "Sustainable Campus Höxter",
            "hinweis": "Ein Standort ist besonders nachhaltig ausgerichtet."
        }
    ]
}


# =========================
# Globale Spielvariablen
# =========================

# Enthält alle Spieler mit Name und erreichtem Punktestand.
spieler_liste = []

# Index des aktuell spielenden Spielers in der spieler_liste.
aktueller_spieler_index = 0

# Name des Spielers, der aktuell an der Reihe ist.
spieler_name = ""

# Aktuell gewählter Spielmodus.
modus = "Fair"

# Enthält die neun ausgewählten Fragen der aktuellen Spielerrunde.
spiel_fragen = []

# Index der aktuellen Frage. Index 0 entspricht Frage 1.
frage_index = 0

# Aktueller Punktestand des Spielers.
punkte = 0

# Verbleibende Zeit der aktuellen Frage in Sekunden.
timer = 0

# ID des mit root.after() geplanten Timer-Aufrufs.
# Dadurch kann der Timer später mit after_cancel() gestoppt werden.
timer_id = None

# True = Joker noch verfügbar, False = bereits benutzt
joker_5050_verfuegbar = True
joker_anruf_verfuegbar = True
joker_zeit_verfuegbar = True
joker_switch_verfuegbar = True

# Verhindert mehrere Antworten oder Joker-Aktionen nach einer Antwort.
# False = Eingabe möglich, True = weitere Eingaben gesperrt.
antwort_gesperrt = False

# Tastatursteuerung ist nur während einer aktiven Frage erlaubt.
# Dadurch lösen Tasten in Eingabefenstern keine Joker aus.
tastatur_aktiv = False

# Enthält die vier Antwortfelder der Oberfläche
antwort_buttons = []


# =========================
# Highscore-Funktionen
# =========================

def lade_highscores():
    # Diese Funktion lädt die gespeicherten Highscores aus der JSON-Datei.
    # Wenn die Datei fehlt, ungültiges JSON enthält
    # oder die geladene Hauptstruktur keine Liste ist,
    # wird eine leere Liste zurückgegeben.
    if not os.path.exists(HIGHSCORE_DATEI):
        return []

    try:
        with open(HIGHSCORE_DATEI, "r", encoding="utf-8") as datei:
            # Liest die JSON-Datei und wandelt den Inhalt
            # in eine passende Python-Datenstruktur um.
            daten = json.load(datei)

            # Prüft, ob die geladenen Highscores als Liste vorliegen.
            if isinstance(daten, list):
                return daten #Gibt die gelesenen Highscores zurück.

            return []


    # Ungültiges JSON oder Probleme beim Dateizugriff abfangen.
    except (json.JSONDecodeError, OSError):

        return []


def speichere_highscores(daten):
    # Öffnet die Highscore-Datei im Schreibmodus.
    # Falls sie noch nicht existiert, wird sie automatisch erstellt.
    with open(HIGHSCORE_DATEI, "w", encoding="utf-8") as datei:
        # Speichert die Python-Daten im JSON-Format.
        # indent=4 sorgt für lesbare Einrückung.
        # ensure_ascii=False erhält Umlaute und Sonderzeichen.
        json.dump(daten, datei, indent=4, ensure_ascii=False)


def speichere_highscore(name, punkte_anzahl, spielmodus): # Neuer Punktestand wird zur Rangliste hinzugefügt.
    daten = lade_highscores()

    # Fügt einen neuen Highscore als Dictionary zur Liste hinzu.
    daten.append({
        "name": name,
        "punkte": punkte_anzahl,
        "modus": spielmodus
    })

    # Höchste Punktzahl steht oben.
    # get("punkte", 0) verwendet 0 als Standardwert,
    # falls bei einem Dictionary-Eintrag das Feld "punkte" fehlt.
    daten = sorted(
        daten,
        key=lambda eintrag: eintrag.get("punkte", 0),
        reverse=True
    )

    speichere_highscores(daten)

def zeige_highscores():
    global timer_id

    # global erlaubt das Verändern der außerhalb definierten timer_id

    # Wenn die Rangliste während einer Frage geöffnet wird,
    # pausieren wir den Timer.
    timer_war_aktiv = False

    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None
        timer_war_aktiv = True

    # Gespeicherte Highscores aus der JSON-Datei laden.
    daten = lade_highscores()

    # Eigenes Fenster für die Rangliste.
    rangliste_fenster = tk.Toplevel(root)
    rangliste_fenster.title("Rangliste")
    rangliste_fenster.geometry("460x420")
    rangliste_fenster.configure(bg="#001f3f")

    # Fenster nach vorne holen.
    rangliste_fenster.lift()
    rangliste_fenster.attributes("-topmost", True)
    rangliste_fenster.after(
        200,
        lambda: rangliste_fenster.attributes("-topmost", False)
    )

    titel = tk.Label(
        rangliste_fenster,
        text="RANGLISTE",
        font=("Arial", 22, "bold"),
        fg="gold",
        bg="#001f3f"
    )
    titel.pack(pady=15)

    if not daten:
        text = "Noch keine Highscores vorhanden.\nSpiele zuerst eine Runde."
    else:
        text = ""

        # daten[:10] nimmt nur die zehn besten Einträge.
        # enumerate(..., start=1) erzeugt Platznummern ab 1.
        for platz, eintrag in enumerate(daten[:10], start=1):
            # get() verwendet einen Standardwert, falls ein Feld fehlt.
            # So wird z. B. bei fehlendem Modus "Unbekannt" angezeigt.
            name = eintrag.get("name", "Unbekannt")
            punkte_wert = eintrag.get("punkte", 0)
            modus_wert = eintrag.get("modus", "Unbekannt")

            text += (
                f"{platz}. {name} - "
                f"{punkte_wert} Punkte ({modus_wert})\n"
            )

    rangliste_label = tk.Label(
        rangliste_fenster,
        text=text,
        font=("Arial", 20),
        fg="white",
        bg="#001f3f",
        justify="left"
    )
    rangliste_label.pack(pady=10)

    schliessen_button = tk.Button(
        rangliste_fenster,
        text="Schließen",
        font=("Arial", 13),
        command=rangliste_fenster.destroy
    )
    schliessen_button.pack(pady=15)

    # Warten, bis das Ranglistenfenster geschlossen wurde.
    root.wait_window(rangliste_fenster)

    # Timer nur fortsetzen, wenn er vorher wirklich aktiv war
    # und noch keine Antwort gegeben wurde.
    if timer_war_aktiv and not antwort_gesperrt:
        starte_timer()


def zeige_regeln():
    global timer_id

    # Wenn die Regeln während einer aktiven Frage geöffnet werden,
    # soll der Timer nicht weiterlaufen.
    # Der Spieler kann während des Regeln-Fensters nicht antworten.
    timer_war_aktiv = False

    # Wenn gerade ein Timer läuft, wird er gestoppt.
    # Die ID des Timers wird mit after_cancel() abgebrochen.
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None
        timer_war_aktiv = True

    # Diese Funktion zeigt die Spielregeln in einem eigenen Fenster an.
    regeln =  (
        "SPIELREGELN\n\n"

        "ABLAUF:\n"
        "• Es können 1 oder 2 Spieler spielen.\n"
        "• Jeder Spieler spielt eine eigene Runde.\n"
        "• Pro Runde gibt es 9 Fragen.\n"
        "• Die ersten 3 Fragen sind einfach.\n"
        "• Die nächsten 3 Fragen sind mittel.\n"
        "• Die letzten 3 Fragen sind schwer.\n"
        "• Jede Frage hat 4 Antwortmöglichkeiten.\n"
        "• Die Antwortmöglichkeiten werden zufällig gemischt.\n\n"

        "EINGABEN BEIM START:\n"
        "• Spieleranzahl: 1, 2, 01, 02, eins oder zwei.\n"
        "• Spielernamen dürfen nicht leer sein.\n"
        f"• Spielernamen dürfen maximal {MAX_NAME_LAENGE} Zeichen lang sein.\n"
        "• Doppelte Spielernamen sind nicht erlaubt.\n"
        "• Beim Spielmodus sind Fair, F, Hard oder H möglich.\n\n"

        "PUNKTE:\n"
        "• Einfache Fragen geben 10 Punkte.\n"
        "• Mittlere Fragen geben 20 Punkte.\n"
        "• Schwere Fragen geben 30 Punkte.\n"
        "• Pro Runde sind maximal 180 Punkte möglich.\n"
        "• Eine falsche Antwort beendet die Runde.\n"
        "• Wenn die Zeit abläuft, endet die Runde.\n\n"

        "MODI:\n"
        "• Fair: mehr Zeit pro Frage.\n"
        "• Hard: weniger Zeit pro Frage.\n"
        "• Im Hard-Modus ist der Timer kürzer.\n\n"

        "JOKER:\n"
        "• Jeder Joker darf nur einmal pro Runde benutzt werden.\n"
        "• Joker können nur vor einer Antwort benutzt werden.\n"
        "• 50:50 entfernt zwei falsche Antworten.\n"
        "• Anrufjoker zeigt einen Hinweis zur aktuellen Frage.\n"
        "• Zeitjoker gibt 10 Sekunden extra.\n"
        "• Frage wechseln ersetzt die aktuelle Frage.\n"
        "• Die neue Frage hat die gleiche Schwierigkeit.\n"
        "• Beim Fragewechsel startet der Timer für die neue Frage neu.\n\n"

        "STEUERUNG:\n"
        "• Antworten können angeklickt werden.\n"
        "• Tasten 1-4 wählen eine Antwort.\n"
        "• F nutzt den 50:50 Joker.\n"
        "• A nutzt den Anrufjoker.\n"
        "• Z nutzt den Zeitjoker.\n"
        "• W nutzt den Frage-wechseln-Joker.\n"
        "• Während Eingabefenstern ist die Quiz-Tastatur deaktiviert.\n\n"

        "RANGLISTE:\n"
        "• Nach jeder Runde wird der Punktestand gespeichert.\n"
        "• Die Rangliste zeigt die 10 besten Ergebnisse.\n"
        "• Gespeichert werden Name, Punkte und Spielmodus.\n"
        "• Die Rangliste wird nach Punkten sortiert.\n\n"

        "SPIELENDE:\n"
        "• Nach allen Spielern wird ein Endergebnis angezeigt.\n"
        "• Bei zwei Spielern wird der Gewinner angezeigt.\n"
        "• Bei gleicher Punktzahl gibt es ein Unentschieden.\n"
        "• Danach kann ein neues Spiel gestartet werden."
    )

    # Erstellt ein zusätzliches Fenster für die Spielregeln.
    regeln_fenster = tk.Toplevel(root)
    regeln_fenster.title("Spielregeln")
    regeln_fenster.geometry("650x720")
    regeln_fenster.configure(bg="#001f3f")

    # Fenster nach vorne holen.
    regeln_fenster.lift()
    regeln_fenster.attributes("-topmost", True)
    regeln_fenster.after(
        200,
        lambda: regeln_fenster.attributes("-topmost", False)
    )

    titel = tk.Label(
        regeln_fenster,
        text="SPIELREGELN",
        font=("Arial", 22, "bold"),
        fg="gold",
        bg="#001f3f"
    )
    titel.pack(pady=15)

    # Frame für Regeltext und Scrollbar.
    # Dadurch kann der längere Regeltext gescrollt werden.
    text_frame = tk.Frame(regeln_fenster, bg="#001f3f")
    text_frame.pack(padx=25, pady=10, fill="both", expand=True)

    # Scrollbar für den Regeltext.
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side="right", fill="y")

    # Textfeld für die Regeln.
    # yscrollcommand verbindet das Textfeld mit der Scrollbar.
    regeln_text = tk.Text(
        text_frame,
        width=72,
        height=22,
        font=("Arial", 15),
        fg="white",
        bg="#001f3f",
        wrap="word",
        relief="flat",
        borderwidth=0,
        yscrollcommand=scrollbar.set
    )

    regeln_text.insert("1.0", regeln)

    # Das Textfeld ist nur zum Lesen da.
    # Deshalb wird es nach dem Einfügen deaktiviert.
    regeln_text.config(state="disabled")
    regeln_text.pack(side="left", fill="both", expand=True)

    # Scrollbar steuert das Textfeld.
    scrollbar.config(command=regeln_text.yview)

    schliessen_button = tk.Label(
        regeln_fenster,
        text="Schließen",
        font=("Arial", 13, "bold"),
        bg="#004C99",
        fg="white",
        width=16,
        height=2,
        relief="raised",
        bd=4,
        cursor="hand2"
    )
    schliessen_button.pack(pady=15)

    schliessen_button.bind(
        "<Button-1>",
        lambda event: regeln_fenster.destroy()
    )

    # Das Fenster bleibt aktiv, bis es geschlossen wird.
    # Das Regeln-Fenster wird in den Vordergrund gesetzt.
    # Durch grab_set() kann der Nutzer erst weiter im Spiel klicken,
    # wenn das Regeln-Fenster geschlossen wurde.
    regeln_fenster.grab_set()

    # wait_window() wartet, bis das Regeln-Fenster geschlossen wird.
    # Erst danach läuft der Code darunter weiter.
    root.wait_window(regeln_fenster)

    # Wenn vor dem Öffnen der Regeln ein Timer aktiv war
    # und noch keine Antwort gegeben wurde,
    # wird der Timer nach dem Schließen der Regeln wieder gestartet.
    if timer_war_aktiv and not antwort_gesperrt:
        starte_timer()

# =========================
# Hilfsfunktionen
# =========================

def waehle_spiel_fragen():
    # random.sample() wählt je drei unterschiedliche Fragen zufällig aus.
    # Insgesamt entstehen 9 Fragen mit steigender Schwierigkeit.
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

    # Alle Joker für eine neue Spielerrunde wieder freigeben.

    joker_5050_verfuegbar = True
    joker_anruf_verfuegbar = True
    joker_zeit_verfuegbar = True
    joker_switch_verfuegbar = True

    # Joker-Buttons in der Oberfläche wieder aktivieren.
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
    global spieler_liste, modus, tastatur_aktiv

    # Während der Startabfragen soll die Quiz-Tastatur deaktiviert sein.
    tastatur_aktiv = False

    # Die Variable "schritt" merkt sich, in welchem Teil der Abfrage wir sind.
    # Dadurch kann Cancel zu einem vorherigen Schritt zurückgehen.

    spieler_liste = []
    anzahl = None
    schritt = "spieleranzahl"

    # Wiederholt die Eingaben, bis gültige Werte vorliegen.
    # continue startet den nächsten Schleifendurchlauf,
    # break beendet die Schleife.
    while True:

        # =========================
        # Schritt 1: Spieleranzahl
        # =========================
        if schritt == "spieleranzahl":
            anzahl_text = simpledialog.askstring( # Fragt den Spieler, wie viele Personen mitspielen sollen (1 oder 2).
                "Spieleranzahl", # Die Eingabe erfolgt über ein Eingabefenster (GUI).
                "Wie viele Spieler? Bitte 1 oder 2 eingeben:",
                parent=root
            )

            # Bei der ersten Abfrage gibt es kein vorheriges Fenster. Deshalb beendet Cancel hier das Programm.
            if anzahl_text is None:
                programm_beenden()

            # strip() entfernt Leerzeichen.
            # lower() macht Groß-/Kleinschreibung egal.
            anzahl_text = anzahl_text.strip().lower()

            # 1, 01 und eins werden als ein Spieler akzeptiert.
            if anzahl_text in ["1", "01", "eins"]:
                anzahl = 1
                spieler_liste = []
                schritt = "namen"
                continue

            # 2, 02 und zwei werden als zwei Spieler akzeptiert.
            if anzahl_text in ["2", "02", "zwei"]:
                anzahl = 2
                spieler_liste = []
                schritt = "namen"
                continue

            messagebox.showwarning(
                "Ungültige Eingabe",
                "Bitte nur 1 oder 2 eingeben.",
                parent=root
            )

        # =========================
        # Schritt 2: Spielernamen
        # =========================
        elif schritt == "namen":
            # Anzahl bereits gespeicherter Spieler bestimmt,
            # welcher Spielername als Nächstes abgefragt wird.
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

            # Entfernt Leerzeichen am Anfang und Ende des Namens.
            name = name.strip()

            if not name: # not name bedeutet: Der Name ist leer.
                messagebox.showwarning(
                    "Ungültiger Name",
                    "Bitte einen Namen eingeben.",
                    parent=root
                )
                continue

            if len(name) > MAX_NAME_LAENGE: # len(name) zählt die Zeichen & prüft, ob der Name zu lang ist.
                messagebox.showwarning(
                    "Name zu lang",
                    f"Der Name darf maximal {MAX_NAME_LAENGE} Zeichen haben.",
                    parent=root
                )
                continue

            # Für den Vergleich entfernen wir Leerzeichen und ignorieren Groß-/Kleinschreibung.
            # Dadurch gelten "Helin Dursun", "helin dursun" und "HelinDursun" als gleicher Name.
            vergleichs_name = name.replace(" ", "").lower()

            # Merkt sich, ob ein gleicher Name bereits existiert.
            name_schon_vergeben = False

            for spieler in spieler_liste:
                gespeicherter_name = spieler["name"].replace(" ", "").lower()

                if gespeicherter_name == vergleichs_name:
                    name_schon_vergeben = True

            if name_schon_vergeben:
                messagebox.showwarning(
                    "Name schon vergeben",
                    "Dieser Name wurde bereits eingegeben. Bitte einen anderen Namen wählen.",
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
                "Bitte Fair oder Hard eingeben.",
                parent=root
            )


# =========================
# Oberfläche
# =========================

root = tk.Tk() # Erstellt das Hauptfenster der Anwendung

# Das Hauptfenster wird beim Programmstart zunächst versteckt.
# Dadurch sieht der Nutzer zuerst nur das Startmenü
# und nicht schon die spätere Quizoberfläche im Hintergrund.
root.withdraw()
# Legt Fenstertitel, Größe und Hintergrundfarbe fest.
root.title("QuizMaster - TH OWL & Herford Edition")
root.geometry("950x720")
root.configure(bg="#001f3f")

# Zentraler Container für die sichtbaren Spielelemente.
main_frame = tk.Frame(root, bg="#001f3f")

# Platziert den Container ungefähr mittig im Hauptfenster.
main_frame.place(relx=0.5, rely=0.48, anchor="center")

# =========================
# Titelbereich
# =========================
titel_label = tk.Label( # Haupttitel des Spiels
    main_frame,
    text=PROJEKTNAME,
    font=("Arial", 30, "bold"),
    fg="gold",
    bg="#001f3f"
)
titel_label.pack(pady=10)

untertitel_label = tk.Label( # Untertitel unter dem Haupttitel
    main_frame,
    text="TH OWL & Herford Edition",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#001f3f"
)
untertitel_label.pack()

# Zeigt den Projektslogan unter dem Untertitel.
slogan_label = tk.Label(
    main_frame,
    text=SLOGAN,
    font=("Arial", 14, "italic"),
    fg="gold",
    bg="#001f3f"
)
slogan_label.pack(pady=5)

# Zeigt aktuellen Spieler, Modus und Schwierigkeitsgrad.
info_label = tk.Label(
    main_frame,
    text="",
    font=("Arial", 15),
    fg="white",
    bg="#001f3f"
)
info_label.pack(pady=10)

punkte_label = tk.Label( # Anzeige der aktuellen Punkte
    main_frame,
    text="Punkte: 0",
    font=("Arial", 16),
    fg="white",
    bg="#001f3f"
)
punkte_label.pack()

timer_label = tk.Label( # Anzeige des Timers für die aktuelle Frage
    main_frame,
    text="Zeit: 0",
    font=("Arial", 18, "bold"),
    fg="red",
    bg="#001f3f"
)
timer_label.pack(pady=10)

frage_label = tk.Label( # Anzeige der aktuellen Frage
    main_frame,
    text="",
    wraplength=800,
    font=("Arial", 20),
    fg="white",
    bg="#001f3f"
)
frage_label.pack(pady=20)

# =========================
# Antwortbereich
# =========================

# Container für die vier klickbaren Antwortfelder.
antwort_frame = tk.Frame(main_frame, bg="#001f3f")
antwort_frame.pack()

# Erstellt vier klickbare Antwortfelder als Labels.
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

    button.grid(row=i // 2, column=i % 2, padx=15, pady=15) # Positionierung im Raster (2x2 Layout)
    # Speichert alle Antwortfelder für spätere Änderungen.
    antwort_buttons.append(button)

# =========================
# Joker-Bereich
# =========================

joker_frame = tk.Frame(main_frame, bg="#001f3f") #Box für Joker-Buttons
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

joker_switch_button = tk.Button( # Fragewechsel-Joker Button
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
    main_frame,
    text="Rangliste anzeigen",
    font=("Arial", 14),
    command=zeige_highscores
)
highscore_button.pack(pady=5)

# =========================
# Regeln Button
# =========================

regeln_button = tk.Button( # Öffnet die Regeln
    main_frame,
    text="Regeln anzeigen",
    font=("Arial", 14),
    command=zeige_regeln
)
regeln_button.pack(pady=5)

# =========================
# Hilfe / Steuerung
# =========================

hilfe_label = tk.Label( # Zeigt Tastenkürzel für das Spiel an
    main_frame,
    text="Tasten: 1-4 Antworten | F = 50:50 | A = Anrufjoker | Z = Zeitjoker | W = Frage wechseln",
    font=("Arial", 14),
    fg="white",
    bg="#001f3f"
)
hilfe_label.pack(pady=5)


# =========================
# Effekt-Funktionen
# =========================

def farbe_zuruecksetzen():
    # Standard-Hintergrundfarbe der Anwendung.
    normale_farbe = "#001f3f"

    # Setzt Hauptfenster und zentrale UI-Bereiche wieder auf Dunkelblau.
    root.configure(bg=normale_farbe)
    main_frame.config(bg=normale_farbe)
    titel_label.config(bg=normale_farbe)
    untertitel_label.config(bg=normale_farbe)
    slogan_label.config(bg=normale_farbe)
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
    if richtig:
        farbe = "#0b5c0b"
        text = "✅ RICHTIG!"
    else:
        farbe = "#7a0000"
        text = "❌ FALSCH!"

    root.bell() # Gibt einen kurzen Soundeffekt aus (System-Bell)

    # Ändert die Hintergrundfarben der zentralen UI-Bereiche.
    root.configure(bg=farbe)
    main_frame.config(bg=farbe)
    titel_label.config(bg=farbe)
    untertitel_label.config(bg=farbe)
    slogan_label.config(bg=farbe)
    info_label.config(bg=farbe)
    punkte_label.config(bg=farbe)
    timer_label.config(bg=farbe)
    frage_label.config(bg=farbe)
    antwort_frame.config(bg=farbe)
    joker_frame.config(bg=farbe)
    hilfe_label.config(bg=farbe)

    # Zeigt eine auffällige Rückmeldung direkt nach der Antwort.
    frage_label.config(text=text, font=("Arial", 28, "bold"))
 
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

    # Namen des aktuell ausgewählten Spielers laden.
    spieler_name = spieler_liste[aktueller_spieler_index]["name"]

    # Rundenwerte zurücksetzen.
    punkte = 0
    frage_index = 0

    # Neun neue zufällige Fragen auswählen.
    spiel_fragen = waehle_spiel_fragen()

    if timer_id is not None: # Stoppt eventuell laufenden Timer aus vorheriger Runde
        root.after_cancel(timer_id)
        timer_id = None

    reset_joker() # Setzt alle Joker zurück

    messagebox.showinfo("Spielstart", f"{spieler_name} ist dran!") # Informiert den Spieler, dass seine Runde beginnt

    zeige_frage() # Zeigt die erste Frage


def zeige_frage(): # Zeigt die aktuelle Frage und die Antwortmöglichkeiten an.
    global timer, timer_id, antwort_gesperrt, tastatur_aktiv

    # Bei jeder neuen Frage darf wieder geantwortet werden.
    antwort_gesperrt = False
    tastatur_aktiv = True

    # Alte Timer werden gestoppt, damit nicht mehrere Timer gleichzeitig laufen.
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    # Holt die aktuelle Frage aus der Rundenliste.
    frage = spiel_fragen[frage_index]
    schwierigkeitsgrad = aktuelle_schwierigkeit()  # Bestimmt die aktuelle Schwierigkeit

    info_label.config( # Aktualisiert Infoanzeige (Spieler, Modus, Schwierigkeit)
        text=f"Spieler: {spieler_name} | Modus: {modus} | Schwierigkeit: {schwierigkeitsgrad}"
    )

    punkte_label.config(text=f"Punkte: {punkte}") # Aktualisiert Punktestand im UI

    frage_label.config( # Zeigt Frage im Label an
        text=f"Frage {frage_index + 1}/9:\n{frage['frage']}",
        font=("Arial", 20)
    )

    # Erstellt eine Kopie der Antwortliste,
    # damit die Originaldaten nicht verändert werden.
    antworten = frage["antworten"][:]

    # Mischt die Reihenfolge der kopierten Antworten zufällig.
    random.shuffle(antworten)

    # Aktualisiert die vier vorhandenen Antwortfelder.
    for i in range(4):
        # Alte Klick-Verbindungen werden zuerst entfernt.
        # Dadurch bleibt pro Antwortfeld immer nur eine aktuelle Klickaktion aktiv.
        antwort_buttons[i].unbind("<Button-1>")

        antwort_buttons[i].antwort_wert = antworten[i]

        antwort_buttons[i].config(
            text=f"{i + 1}. {antworten[i]}",
            bg="#004C99",
            fg="white",
            relief="raised",
            bd=4
        )

        # Bei Labels gibt es kein command=...
        # Deshalb verbinden wir den Mausklick mit bind().
        # "<Button-1>" steht für einen Klick mit der linken Maustaste.
        antwort_buttons[i].bind(
            "<Button-1>",
            lambda event, antwort=antworten[i]: pruefe_antwort(antwort)
        )

    timer = ZEITLIMIT[modus][schwierigkeitsgrad] # Setzt Timer abhängig von Modus und Schwierigkeit
    # Startzeit direkt in der Oberfläche anzeigen.
    timer_label.config(text=f"Zeit: {timer}")

    starte_timer() # Startet den Countdown


def starte_timer(): # Verwaltet den Countdown-Timer für jede Frage
    global timer, timer_id, antwort_gesperrt

    timer_label.config(text=f"Zeit: {timer}")

    if timer <= 0: # Wenn Zeit abgelaufen ist
        antwort_gesperrt = True # keine Antwort mehr möglich
        timer_id = None

        for button in antwort_buttons:
            # Bei Labels entfernen wir die Klick-Funktion mit unbind().
            button.unbind("<Button-1>")
 
        frage_label.config(text="⏰ ZEIT VORBEI!\n\nDas Spiel endet.") # Zeigt Zeit-abgelaufen Nachricht
        messagebox.showerror("Zeit vorbei", "Du warst zu langsam!")
        root.after(1000, spieler_runde_beenden)
    else:
        # Eine Sekunde von der Restzeit abziehen.
        timer -= 1
        # Funktion nach 1000 ms erneut aufrufen und ID speichern.
        timer_id = root.after(1000, starte_timer)


def pruefe_antwort(auswahl): # Prüft, ob die ausgewählte Antwort richtig oder falsch ist
    global punkte, frage_index, timer_id, antwort_gesperrt

    # Falls bereits geantwortet wurde, wird die Funktion sofort beendet.
    if antwort_gesperrt:
        return

    # Ab jetzt werden weitere Antworten und Joker blockiert.
    antwort_gesperrt = True

    if timer_id is not None: # Stoppt den Timer
        root.after_cancel(timer_id)
        timer_id = None

    frage = spiel_fragen[frage_index] # Aktuelle Frage und richtige Antwort
    richtige_antwort = frage["richtig"]
    schwierigkeitsgrad = aktuelle_schwierigkeit()

    for button in antwort_buttons:
        # Nach einer Antwort sollen die Antwortfelder nicht mehr klickbar sein.
        button.unbind("<Button-1>")

    if auswahl == richtige_antwort:
        # Passende Punkte aus dem PUNKTE-Dictionary addieren.
        punkte += PUNKTE[schwierigkeitsgrad]
        punkte_label.config(text=f"Punkte: {punkte}")

        # Das Feld der richtigen Antwort grün markieren.
        # Verglichen wird der interne Antwortwert ohne sichtbare Nummer.
        for button in antwort_buttons:
            if button.antwort_wert == auswahl:
                button.config(bg="green", fg="white")

        zeige_effekt(True)

        # Nach kurzer Verzögerung die Erfolgsmeldung anzeigen.
        root.after(
            600,
            lambda: frage_label.config(
                text=f"✅ RICHTIG!\n\n+{PUNKTE[schwierigkeitsgrad]} Punkte"
            )
        )

        # Genau einmal nach 1600 ms zur nächsten Frage wechseln.
        root.after(1600, naechste_frage)



    else:
        # Gewählte falsche Antwort rot markieren
        # und die richtige Antwort grün anzeigen.
        for button in antwort_buttons:
            if button.antwort_wert == auswahl:
                button.config(bg="red", fg="white")

            if button.antwort_wert == richtige_antwort:
                button.config(bg="green", fg="white")

        zeige_effekt(False)

        # Nach kurzer Verzögerung die richtige Antwort anzeigen.
        root.after(

            600,
            lambda: frage_label.config(
                text=f"❌ FALSCH!\n\nRichtige Antwort: {richtige_antwort}"
            )
        )

        # Nach 2000 ms die Spielerrunde beenden.
        root.after(2000, spieler_runde_beenden)


def naechste_frage(): # Wechselt zur nächsten Frage im Spiel
    global frage_index

    frage_index += 1

    if frage_index >= len(spiel_fragen):  # Wenn keine Fragen mehr übrig sind, Runde beenden
        spieler_runde_beenden()
    else: # Sonst nächste Frage anzeigen
        zeige_frage()


def spieler_runde_beenden(): # Beendet die Runde eines Spielers
    global aktueller_spieler_index, tastatur_aktiv

    # Nach einer Runde sollen keine Tastatur-Joker mehr ausgelöst werden.
    tastatur_aktiv = False

    spieler_liste[aktueller_spieler_index]["punkte"] = punkte # Speichert Punkte des Spielers

    speichere_highscore(spieler_name, punkte, modus) # Speichert Highscore in Datei

    messagebox.showinfo( # Zeigt Ergebnis der Runde
        "Runde beendet",
        f"{spieler_name} hat {punkte} Punkte erreicht."
    )

    aktueller_spieler_index += 1 # Nächster Spieler ist dran
    starte_spieler_runde()


def spiel_neu_starten():
    global spieler_liste, aktueller_spieler_index
    global spieler_name, modus, spiel_fragen, frage_index, punkte, timer, timer_id
    global joker_5050_verfuegbar, joker_anruf_verfuegbar
    global joker_zeit_verfuegbar, joker_switch_verfuegbar
    global antwort_gesperrt, tastatur_aktiv

    # Setzt die aktuelle Partie zurück.
    # Dauerhaft gespeicherte Highscores bleiben erhalten.
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    spieler_liste = []
    aktueller_spieler_index = 0

    spieler_name = ""
    modus = "Fair"

    spiel_fragen = []
    frage_index = 0
    punkte = 0
    timer = 0

    joker_5050_verfuegbar = True
    joker_anruf_verfuegbar = True
    joker_zeit_verfuegbar = True
    joker_switch_verfuegbar = True

    antwort_gesperrt = False
    tastatur_aktiv = False

    # Anzeige wieder neutral setzen.
    info_label.config(text="")
    punkte_label.config(text="Punkte: 0")
    timer_label.config(text="Zeit: 0")
    frage_label.config(text="", font=("Arial", 20))

    for button in antwort_buttons:
        button.unbind("<Button-1>")
        button.config(text="", bg="#004C99", fg="white")

    # Startmenü für eine neue Partie erneut anzeigen.
    startmenue()

    # Danach werden wieder Spieleranzahl, Namen und Modus abgefragt.
    start_abfragen()
    starte_spieler_runde()

def spiel_komplett_beenden():
    # Sortiert die Spieler nach Punkten, höchste Punktzahl zuerst.
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

    messagebox.showinfo("Spiel beendet", text, parent=root)

    # Nach dem Endergebnis wird die Rangliste angezeigt.
    zeige_highscores()

    # Danach kann der Nutzer entscheiden, ob er nochmal spielen möchte.
    nochmal_spielen = messagebox.askyesno(
        "Nochmal spielen?",
        "Möchtest du nochmal spielen?",
        parent=root
    )

    if nochmal_spielen:
        spiel_neu_starten()
    else:
        root.destroy()

# =========================
# Joker
# =========================

def joker_5050():
    global joker_5050_verfuegbar

    if antwort_gesperrt:
        return

    if not joker_5050_verfuegbar: # Prüft, ob der Joker bereits verwendet wurde
        messagebox.showwarning("Joker", "50:50 Joker wurde schon benutzt!")
        return

    frage = spiel_fragen[frage_index]  # Holt die aktuelle Frage und die richtige Antwort
    richtige_antwort = frage["richtig"]

    falsche_buttons = [] # Speichert alle Buttons mit falschen Antworten

    # Sammelt nur Antwortfelder,
    # deren interner Antwortwert falsch und noch sichtbar ist.
    for button in antwort_buttons:
        if (
                button.antwort_wert != richtige_antwort
                and button.antwort_wert != "---"
        ):
            falsche_buttons.append(button)

    # Zwei falsche Antworten werden entfernt.
    for button in random.sample(falsche_buttons, 2):
        button.config(
            text="---",
            bg="#333333",
            fg="white"
        )

        # Auch der interne Antwortwert wird als entfernt markiert.
        # Dadurch kann die Antwort nicht über die Tastatur gewählt werden.
        button.antwort_wert = "---"

        # Entfernte Antwort darf nicht mehr anklickbar sein.
        button.unbind("<Button-1>")

    joker_5050_verfuegbar = False
    joker_5050_button.config(state="disabled")


def anrufjoker():
    global joker_anruf_verfuegbar

    # Wenn schon eine Antwort gegeben wurde,
    # darf kein Joker mehr benutzt werden.
    # Dadurch kann der Spieler nachträglich keinen Vorteil bekommen.
    if antwort_gesperrt:
        return

    # Prüft, ob der Anrufjoker in dieser Runde bereits benutzt wurde.
    # Jeder Joker darf pro Runde nur einmal verwendet werden.
    if not joker_anruf_verfuegbar:
        messagebox.showwarning(
            "Joker",
            "Anrufjoker wurde schon benutzt!"
        )
        return

    # Holt die aktuelle Frage aus der Liste der Spiel-Fragen.
    frage = spiel_fragen[frage_index]

    # Zu jeder Frage gibt es im Dictionary einen eigenen Hinweis.
    # Dieser Hinweis wird hier angezeigt.
    messagebox.showinfo(
        "Anrufjoker",
        "📞 Dein Anrufjoker sagt:\n\n" + frage["hinweis"]
    )

    # Nach der Nutzung wird der Anrufjoker als nicht mehr verfügbar markiert.
    joker_anruf_verfuegbar = False

    # Der Button wird deaktiviert, damit der Nutzer sieht,
    # dass der Joker bereits verwendet wurde.
    joker_anruf_button.config(state="disabled")


def zeitjoker():
    global timer, joker_zeit_verfuegbar

    if antwort_gesperrt:
        return

    if not joker_zeit_verfuegbar: # Prüft, ob der Joker bereits verwendet wurde
        messagebox.showwarning("Joker ", "Zeitjoker wurde schon benutzt!")
        return

    # Zehn Sekunden zur aktuellen Restzeit addieren.
    timer += 10

    # Neue Restzeit sofort anzeigen.
    timer_label.config(text=f"Zeit: {timer}")

    joker_zeit_verfuegbar = False # Joker als benutzt markieren und Button deaktivieren
    joker_zeit_button.config(state="disabled")

    messagebox.showinfo("Zeitjoker", "Du hast 10 Sekunden extra bekommen!") # Informiert den Spieler über die zusätzliche Zeit

def frage_wechseln_joker():
    global joker_switch_verfuegbar, spiel_fragen

    if antwort_gesperrt:
        return

    if not joker_switch_verfuegbar: # Prüft, ob der Joker bereits verwendet wurde
        messagebox.showwarning("Joker", "Frage-wechseln-Joker wurde schon benutzt!")
        return

    schwierigkeitsgrad = aktuelle_schwierigkeit() # Ermittelt die Schwierigkeit der aktuellen Frage

    # Sammelt noch nicht verwendete Fragen derselben Schwierigkeit.
    moegliche_fragen = []

    for frage in fragen[schwierigkeitsgrad]: # Es wird eine neue Frage mit derselben Schwierigkeit gesucht.
        if frage not in spiel_fragen:
            moegliche_fragen.append(frage)

    if not moegliche_fragen: # Falls keine passende Ersatzfrage vorhanden ist, wird der Spieler informiert.
        messagebox.showwarning(
            "Joker",
            "Keine weitere Frage auf diesem Niveau verfügbar!"
        )
        return

    # Wählt zufällig eine mögliche Ersatzfrage aus.
    neue_frage = random.choice(moegliche_fragen)

    # Ersetzt die aktuelle Frage an derselben Position.
    spiel_fragen[frage_index] = neue_frage

    joker_switch_verfuegbar = False # Joker als benutzt markieren und Button deaktivieren
    joker_switch_button.config(state="disabled")

    messagebox.showinfo( # Informiert den Spieler über den Fragenwechsel
        "Frage wechseln",
        "Die Frage wurde durch eine neue Frage im gleichen Schwierigkeitsgrad ersetzt."
    )

    # Ersatzfrage anzeigen und Zeitlimit für die neue Frage neu setzen.
    zeige_frage()


# =========================
# Tastatursteuerung
# =========================

def taste(event):
    # Tastatursteuerung nur erlauben, wenn gerade eine Frage aktiv ist.
    if not tastatur_aktiv:
        return

    taste = event.char.lower() # Liest die gedrückte Taste ein und wandelt sie in Kleinbuchstaben um

    if taste in ["1", "2", "3", "4"]: # Tasten 1 bis 4 wählen die entsprechende Antwort aus
        # Listen beginnen bei Index 0, deshalb wird 1 abgezogen.
        index = int(taste) - 1
        antwort = antwort_buttons[index].antwort_wert

        if antwort != "---":
            pruefe_antwort(antwort)

    elif taste == "f": # Tastenkürzel für 50:50 Joker
        joker_5050()

    elif taste == "a": # Tastenkürzel für Anruf Joker
        anrufjoker()

    elif taste == "z": # Tastenkürzel für Zeit Joker
        zeitjoker()

    elif taste == "w": # Tastenkürzel für Frage wechseln Joker
        frage_wechseln_joker()

def startmenue():
    # Dieses Fenster erscheint vor den Startabfragen.
    # Der Spieler kann hier die Regeln lesen oder direkt das Spiel starten.
    # Toplevel erstellt ein zusätzliches Fenster neben dem Hauptfenster.
    start_fenster = tk.Toplevel(root)
    start_fenster.title("Startmenü")
    start_fenster.geometry("560x420")
    start_fenster.configure(bg="#001f3f")

    # Holt das Startfenster kurz sicher in den Vordergrund.
    start_fenster.lift()
    start_fenster.attributes("-topmost", True)
    start_fenster.after(
        200,
        lambda: start_fenster.attributes("-topmost", False)
    )

    titel = tk.Label(
        start_fenster,
        text=PROJEKTNAME,
        font=("Arial", 35, "bold"),
        fg="gold",
        bg="#001f3f"
    )
    titel.pack(pady=15)

    slogan = tk.Label(
        start_fenster,
        text=SLOGAN,
        font=("Arial", 20, "italic"),
        fg="gold",
        bg="#001f3f"
    )
    slogan.pack(pady=5)

    text = tk.Label(
        start_fenster,
        text="Willkommen!\nDu kannst zuerst die Regeln lesen oder direkt starten.",
        font=("Arial", 15),
        fg="white",
        bg="#001f3f",
        justify="center",
        wraplength=430

    )
    text.pack(pady=10)

    regeln_button = tk.Label(
        start_fenster,
        text="Regeln anzeigen",
        font=("Arial", 14, "bold"),
        bg="#004C99",
        fg="white",
        width=22,
        height=2,
        relief="raised",
        bd=4,
        cursor="hand2"
    )
    regeln_button.pack(pady=10)

    starten_button = tk.Label(
        start_fenster,
        text="Spiel starten",
        font=("Arial", 14, "bold"),
        bg="#0b5c0b",
        fg="white",
        width=22,
        height=2,
        relief="raised",
        bd=4,
        cursor="hand2"
    )
    starten_button.pack(pady=10)

    regeln_button.bind(
        "<Button-1>",
        lambda event: zeige_regeln()
    )

    # Diese Funktion wird beim Klick auf "Spiel starten" ausgeführt.
    # Zuerst wird das Startmenü geschlossen.
    # Danach wird das vorher versteckte Hauptfenster wieder sichtbar.
    def spiel_starten():
        start_fenster.destroy()
        root.deiconify()

    starten_button.bind(
        "<Button-1>",
        lambda event: spiel_starten()
    )

    # Wenn das Startmenü über X geschlossen wird, wird das Programm beendet.
    start_fenster.protocol("WM_DELETE_WINDOW", programm_beenden)

    # Sperrt die Bedienung anderer App-Fenster, solange das Startmenü offen ist.
    start_fenster.grab_set()
    # Erst nach dem Schließen des Startmenüs läuft der Programmablauf weiter.
    root.wait_window(start_fenster)


# =========================
# Programmstart
# =========================

root.bind_all("<Key>", taste) # Aktiviert die Tastatursteuerung für das gesamte Fenster

startmenue() # Zuerst nur Startmenü anzeigen

start_abfragen() # Fragt die Spielerinformationen und den Spielmodus ab
starte_spieler_runde() # Startet die erste Spielrunde

root.mainloop() # Startet die Ereignisschleife von Tkinter. Das Fenster bleibt geöffnet und reagiert auf Eingaben.
