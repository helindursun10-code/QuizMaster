import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json
import os


# =========================
# Einstellungen
# =========================

HIGHSCORE_DATEI = "highscores.json"

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

PUNKTE = {
    "einfach": 10,
    "mittel": 20,
    "schwer": 30
}


# =========================
# Fragen
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
# Hilfsfunktionen
# =========================

def lade_highscores():
    if not os.path.exists(HIGHSCORE_DATEI):
        return []

    try:
        with open(HIGHSCORE_DATEI, "r", encoding="utf-8") as datei:
            return json.load(datei)
    except json.JSONDecodeError:
        return []


def speichere_highscores(daten):
    with open(HIGHSCORE_DATEI, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, indent=4, ensure_ascii=False)


def waehle_spiel_fragen():
    return (
        random.sample(fragen["einfach"], 3) +
        random.sample(fragen["mittel"], 3) +
        random.sample(fragen["schwer"], 3)
    )


def frage_schwierigkeit(frage_index):
    if frage_index < 3:
        return "einfach"
    elif frage_index < 6:
        return "mittel"
    else:
        return "schwer"


# =========================
# Spielklasse
# =========================

class QuizMaster:
    def __init__(self, fenster):
        self.root = fenster
        self.root.title("QuizMaster - TH OWL & Herford Edition")
        self.root.geometry("950x720")
        self.root.configure(bg="#001f3f")

        self.spieler_liste = []
        self.aktueller_spieler_index = 0
        self.spiel_fragen = []

        self.frage_index = 0
        self.punkte = 0
        self.timer = 0
        self.timer_id = None

        self.joker_5050 = True
        self.joker_anruf = True

        self.antwort_buttons = []

        self.spieler = "Gast"
        self.modus = "Fair"

        self.setup_start()
        self.setup_gui()
        self.starte_spieler_runde()

    # =========================
    # Startabfragen
    # =========================

    def setup_start(self):
        spieleranzahl = simpledialog.askinteger(
            "Spieleranzahl",
            "Wie viele Spieler? 1 oder 2:"
        )

        if spieleranzahl not in [1, 2]:
            spieleranzahl = 1

        for nummer in range(spieleranzahl):
            name = simpledialog.askstring(
                "Name",
                f"Name Spieler {nummer + 1}:"
            )

            if not name:
                name = f"Spieler {nummer + 1}"

            self.spieler_liste.append({
                "name": name,
                "punkte": 0
            })

        modus = simpledialog.askstring(
            "Spielmodus",
            "Wähle Modus: Fair oder Hard"
        )

        if modus not in ["Fair", "Hard"]:
            modus = "Fair"

        self.modus = modus

    # =========================
    # Oberfläche
    # =========================

    def setup_gui(self):
        self.titel = tk.Label(
            self.root,
            text="QUIZMASTER",
            font=("Arial", 30, "bold"),
            fg="gold",
            bg="#001f3f"
        )
        self.titel.pack(pady=10)

        self.untertitel = tk.Label(
            self.root,
            text="TH OWL & Herford Edition",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#001f3f"
        )
        self.untertitel.pack()

        self.info_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 15),
            fg="white",
            bg="#001f3f"
        )
        self.info_label.pack(pady=10)

        self.punkte_label = tk.Label(
            self.root,
            text="Punkte: 0",
            font=("Arial", 16),
            fg="white",
            bg="#001f3f"
        )
        self.punkte_label.pack()

        self.timer_label = tk.Label(
            self.root,
            text="Zeit: 0",
            font=("Arial", 18, "bold"),
            fg="red",
            bg="#001f3f"
        )
        self.timer_label.pack(pady=10)

        self.frage_label = tk.Label(
            self.root,
            text="",
            wraplength=800,
            font=("Arial", 20),
            fg="white",
            bg="#001f3f"
        )
        self.frage_label.pack(pady=20)

        self.button_frame = tk.Frame(self.root, bg="#001f3f")
        self.button_frame.pack()

        for i in range(4):
            btn = tk.Label(
                self.button_frame,
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
            btn.grid(row=i // 2, column=i % 2, padx=15, pady=15)
            self.antwort_buttons.append(btn)

        self.joker_frame = tk.Frame(self.root, bg="#001f3f")
        self.joker_frame.pack(pady=20)

        self.joker1 = tk.Button(
            self.joker_frame,
            text="50:50 Joker",
            font=("Arial", 14),
            command=self.joker_5050_funktion
        )
        self.joker1.grid(row=0, column=0, padx=10)

        self.joker2 = tk.Button(
            self.joker_frame,
            text="Anrufjoker",
            font=("Arial", 14),
            command=self.anrufjoker
        )
        self.joker2.grid(row=0, column=1, padx=10)

        self.joker3 = tk.Button(
            self.joker_frame,
            text="Zeitjoker +10s",
            font=("Arial", 14),
            command=self.zeitjoker
        )
        self.joker3.grid(row=0, column=2, padx=10)

        self.joker4 = tk.Button(
            self.joker_frame,
            text="Frage wechseln",
            font=("Arial", 14),
            command=self.frage_wechseln_joker
        )
        self.joker4.grid(row=0, column=3, padx=10)

        self.hilfe_label = tk.Label(
            self.root,
            text="Bedienung: Antwort anklicken oder Taste 1-4 nutzen | F = 50:50 | A = Anruf | Z = Zeit | W = Wechsel",
            font=("Arial", 12),
            fg="white",
            bg="#001f3f"
        )
        self.hilfe_label.pack(pady=5)

        self.root.bind_all("<Key>", self.taste)
        self.root.focus_force()

    # =========================
    # Spielstart pro Spieler
    # =========================

    def starte_spieler_runde(self):
        if self.aktueller_spieler_index >= len(self.spieler_liste):
            self.spiel_komplett_beenden()
            return

        aktueller = self.spieler_liste[self.aktueller_spieler_index]
        self.spieler = aktueller["name"]
        self.punkte = 0
        self.frage_index = 0
        self.timer_id = None
        self.joker_5050 = True
        self.joker_anruf = True
        self.spiel_fragen = waehle_spiel_fragen()

        self.joker1.config(state="normal")
        self.joker2.config(state="normal")

        messagebox.showinfo(
            "Spielstart",
            f"{self.spieler} ist dran!"
        )

        self.zeige_frage()

    # =========================
    # Timer
    # =========================

    def starte_timer(self):
        self.timer -= 1
        self.timer_label.config(text=f"Zeit: {self.timer}")

        if self.timer <= 0:
            self.timer_id = None
            self.frage_label.config(
                text="⏰ ZEIT VORBEI!\n\nDas Spiel endet."
            )
            messagebox.showerror(
                "Zeit vorbei",
                "Du warst zu langsam!"
            )
            self.root.after(1000, self.spieler_runde_beenden)
        else:
            self.timer_id = self.root.after(1000, self.starte_timer)

    # =========================
    # Frage anzeigen
    # =========================

    def zeige_frage(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        frage = self.spiel_fragen[self.frage_index]
        schwierigkeitsgrad = frage_schwierigkeit(self.frage_index)

        self.info_label.config(
            text=f"Spieler: {self.spieler} | Modus: {self.modus} | Schwierigkeit: {schwierigkeitsgrad}"
        )

        self.punkte_label.config(text=f"Punkte: {self.punkte}")

        self.frage_label.config(
            text=f"Frage {self.frage_index + 1}/9:\n{frage['frage']}"
        )

        antworten = frage["antworten"][:]
        random.shuffle(antworten)

        for i in range(4):
            self.antwort_buttons[i].config(
                text=antworten[i],
                bg="#004C99",
                fg="white",
                cursor="hand2"
            )

            self.antwort_buttons[i].bind(
                "<Button-1>",
                lambda event, a=antworten[i]: self.pruefe_antwort(a)
            )

        self.timer = ZEITLIMIT[self.modus][schwierigkeitsgrad]
        self.timer_label.config(text=f"Zeit: {self.timer}")

        self.starte_timer()

    # =========================
    # Antwort prüfen
    # =========================

    def pruefe_antwort(self, auswahl):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        frage = self.spiel_fragen[self.frage_index]
        richtige = frage["richtig"]
        schwierigkeitsgrad = frage_schwierigkeit(self.frage_index)

        for btn in self.antwort_buttons:
            btn.unbind("<Button-1>")
            btn.config(cursor="")

        if auswahl == richtige:
            self.punkte += PUNKTE[schwierigkeitsgrad]

            for btn in self.antwort_buttons:
                if btn["text"] == auswahl:
                    btn.config(bg="green")

            self.punkte_label.config(text=f"Punkte: {self.punkte}")

            self.frage_label.config(
                text=f"✅ RICHTIG!\n\n+{PUNKTE[schwierigkeitsgrad]} Punkte"
            )

            self.root.after(1200, self.naechste_frage)

        else:
            for btn in self.antwort_buttons:
                if btn["text"] == auswahl:
                    btn.config(bg="red")

                if btn["text"] == richtige:
                    btn.config(bg="green")

            self.frage_label.config(
                text=f"❌ FALSCH!\n\nRichtige Antwort: {richtige}"
            )

            self.root.after(1600, self.spieler_runde_beenden)

    # =========================
    # Nächste Frage
    # =========================

    def naechste_frage(self):
        self.frage_index += 1

        if self.frage_index >= len(self.spiel_fragen):
            self.spieler_runde_beenden()
        else:
            self.zeige_frage()

    # =========================
    # Runde beenden
    # =========================

    def spieler_runde_beenden(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        self.spieler_liste[self.aktueller_spieler_index]["punkte"] = self.punkte

        self.speichere_highscore(
            self.spieler,
            self.punkte,
            self.modus
        )

        messagebox.showinfo(
            "Runde beendet",
            f"{self.spieler} hat {self.punkte} Punkte erreicht."
        )

        self.aktueller_spieler_index += 1
        self.starte_spieler_runde()

    # =========================
    # Spiel komplett beenden
    # =========================

    def spiel_komplett_beenden(self):
        ergebnis = "ENDERGEBNIS\n\n"

        sortierte_spieler = sorted(
            self.spieler_liste,
            key=lambda x: x["punkte"],
            reverse=True
        )

        for platz, spieler in enumerate(sortierte_spieler, start=1):
            ergebnis += f"{platz}. {spieler['name']} - {spieler['punkte']} Punkte\n"

        if len(sortierte_spieler) == 2:
            if sortierte_spieler[0]["punkte"] > sortierte_spieler[1]["punkte"]:
                ergebnis += f"\nGewinner: {sortierte_spieler[0]['name']}"
            else:
                ergebnis += "\nUnentschieden"

        messagebox.showinfo(
            "Spiel beendet",
            ergebnis
        )

        self.zeige_highscores()
        self.root.destroy()

    # =========================
    # 50:50 Joker
    # =========================

    def joker_5050_funktion(self):
        if not self.joker_5050:
            messagebox.showwarning(
                "Joker",
                "50:50 Joker wurde schon benutzt!"
            )
            return

        frage = self.spiel_fragen[self.frage_index]
        richtige = frage["richtig"]

        falsche_buttons = []

        for btn in self.antwort_buttons:
            if btn["text"] != richtige and btn["text"] != "---":
                falsche_buttons.append(btn)

        if len(falsche_buttons) >= 2:
            entfernen = random.sample(falsche_buttons, 2)

            for btn in entfernen:
                btn.unbind("<Button-1>")
                btn.config(text="---", bg="#555555", cursor="")

        self.joker_5050 = False
        self.joker1.config(state="disabled")

    # =========================
    # Anrufjoker
    # =========================

    def anrufjoker(self):
        if not self.joker_anruf:
            messagebox.showwarning(
                "Joker",
                "Anrufjoker wurde schon benutzt!"
            )
            return

        frage = self.spiel_fragen[self.frage_index]
        richtige = frage["richtig"]

        messagebox.showinfo(
            "Anrufjoker",
            f"Ich glaube, die richtige Antwort ist:\n{richtige}"
        )

        self.joker_anruf = False
        self.joker2.config(state="disabled")

    def zeitjoker(self):
        if not self.joker_zeit:
            messagebox.showwarning(
                "Joker",
                "Zeitjoker wurde schon benutzt!"
            )
            return

        self.timer += 10
        self.timer_label.config(text=f"Zeit: {self.timer}")

        self.joker_zeit = False
        self.joker3.config(state="disabled")

        messagebox.showinfo(
            "Zeitjoker",
            "Du hast 10 Sekunden extra bekommen!"
        )

    def frage_wechseln_joker(self):
        if not self.joker_switch:
            messagebox.showwarning(
                "Joker",
                "Frage-wechseln-Joker wurde schon benutzt!"
            )
            return

        schwierigkeitsgrad = frage_schwierigkeit(self.frage_index)

        moegliche_fragen = []

        for frage in fragen[schwierigkeitsgrad]:
            if frage not in self.spiel_fragen:
                moegliche_fragen.append(frage)

        if not moegliche_fragen:
            messagebox.showwarning(
                "Joker",
                "Keine weitere Frage auf diesem Niveau verfügbar!"
            )
            return

        neue_frage = random.choice(moegliche_fragen)
        self.spiel_fragen[self.frage_index] = neue_frage

        self.joker_switch = False
        self.joker4.config(state="disabled")

        messagebox.showinfo(
            "Frage wechseln",
            "Die Frage wurde durch eine neue Frage im gleichen Niveau ersetzt."
        )

        self.zeige_frage()


    # =========================
    # Tastenkombinationen
    # =========================

    def taste(self, event):
        taste = event.char.lower()

        if taste in ["1", "2", "3", "4"]:
            index = int(taste) - 1
            antwort = self.antwort_buttons[index]["text"]

            if antwort != "---" and antwort != "":
                self.pruefe_antwort(antwort)

        elif taste == "f":
            self.joker_5050_funktion()

        elif taste == "a":
            self.anrufjoker()

        elif taste == "z":
            self.zeitjoker()

        elif taste == "w":
            self.frage_wechseln_joker()

    # =========================
    # Highscore
    # =========================

    def speichere_highscore(self, name, punkte, modus):
        daten = lade_highscores()

        daten.append({
            "name": name,
            "punkte": punkte,
            "modus": modus
        })

        daten = sorted(
            daten,
            key=lambda x: x["punkte"],
            reverse=True
        )

        speichere_highscores(daten)

    def zeige_highscores(self):
        daten = lade_highscores()

        if not daten:
            return

        text = "RANGLISTE\n\n"

        for eintrag in daten[:10]:
            text += (
                f"{eintrag['name']} - "
                f"{eintrag['punkte']} Punkte "
                f"({eintrag.get('modus', 'Fair')})\n"
            )

        messagebox.showinfo(
            "Highscores",
            text
        )


# =========================
# Programmstart
# =========================

root = tk.Tk()
app = QuizMaster(root)
root.mainloop()