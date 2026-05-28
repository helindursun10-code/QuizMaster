import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json
import os

# =========================
# Einstellungen
# =========================
ZEITLIMIT = {
    "einfach": 20,
    "mittel": 15,
    "schwer": 10
}

HIGHSCORE_DATEI = "highscores.json"

# =========================
# Fragen
# =========================
fragen = {
    "einfach": [
        {
            "frage": "Wo befindet sich die TH OWL?",
            "antworten": ["Lemgo", "Berlin", "Hamburg", "München"],
            "richtig": "Lemgo"
        },
        {
            "frage": "Welcher Campus gehört zur TH OWL?",
            "antworten": ["Herford", "Köln", "Bremen", "Leipzig"],
            "richtig": "Herford"
        },
        {
            "frage": "Wie viele Antworten gibt es pro Frage?",
            "antworten": ["2", "3", "4", "5"],
            "richtig": "4"
        }
    ],

    "mittel": [
        {
            "frage": "Welche Sprache wird hier programmiert?",
            "antworten": ["Java", "Python", "C++", "HTML"],
            "richtig": "Python"
        },
        {
            "frage": "Was bedeutet GUI?",
            "antworten": [
                "Grafisches User Interface",
                "Großes User Internet",
                "Game Utility Input",
                "Keine Antwort"
            ],
            "richtig": "Grafisches User Interface"
        },
        {
            "frage": "Welcher Joker entfernt 2 falsche Antworten?",
            "antworten": [
                "Anrufjoker",
                "50:50 Joker",
                "Publikumsjoker",
                "Zeitjoker"
            ],
            "richtig": "50:50 Joker"
        }
    ],

    "schwer": [
        {
            "frage": "Welche Datei speichert die Rangliste?",
            "antworten": [
                "fragen.txt",
                "ranking.py",
                "highscores.json",
                "musik.mp3"
            ],
            "richtig": "highscores.json"
        },
        {
            "frage": "Welche Funktion macht Antworten zufällig?",
            "antworten": [
                "random.shuffle()",
                "sort()",
                "append()",
                "print()"
            ],
            "richtig": "random.shuffle()"
        },
        {
            "frage": "Wie oft darf ein Joker benutzt werden?",
            "antworten": [
                "Unendlich",
                "2x",
                "1x",
                "Nie"
            ],
            "richtig": "1x"
        }
    ]
}

# =========================
# Fragen mischen
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
root.title("Wer wird Millionär - TH OWL Edition")
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
    text="WER WIRD MILLIONÄR?",
    font=("Arial", 28, "bold"),
    fg="gold",
    bg="#001f3f"
)
titel.pack(pady=20)

# =========================
# Spielername
# =========================
spieler_label = tk.Label(
    root,
    text=f"Spieler: {spieler}",
    font=("Arial", 16),
    fg="white",
    bg="#001f3f"
)
spieler_label.pack()

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
    wraplength=700,
    font=("Arial", 20),
    fg="white",
    bg="#001f3f"
)
frage_label.pack(pady=30)

# =========================
# Antwortbuttons
# =========================
antwort_buttons = []

button_frame = tk.Frame(root, bg="#001f3f")
button_frame.pack()

# =========================
# Timer Funktion
# =========================
def starte_timer():
    global timer

    timer -= 1
    timer_label.config(text=f"Zeit: {timer}")

    if timer <= 0:
        messagebox.showerror(
            "Zeit vorbei",
            "Du warst zu langsam!"
        )
        naechste_frage()
    else:
        global timer_id
        timer_id = root.after(1000, starte_timer)

# =========================
# Frage anzeigen
# =========================
def zeige_frage():
    global timer

    frage = spiel_fragen[frage_index]

    frage_label.config(
        text=f"Frage {frage_index + 1}:\n{frage['frage']}"
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

    # Zeit je Schwierigkeit
    if frage_index < 3:
        timer = ZEITLIMIT["einfach"]
    elif frage_index < 6:
        timer = ZEITLIMIT["mittel"]
    else:
        timer = ZEITLIMIT["schwer"]

    timer_label.config(text=f"Zeit: {timer}")

    starte_timer()

# =========================
# Antwort prüfen
# =========================
def pruefe_antwort(auswahl):
    global punkte

    root.after_cancel(timer_id)

    richtige = spiel_fragen[frage_index]["richtig"]

    if auswahl == richtige:
        punkte += 10

        print("RICHTIG!")

        messagebox.showinfo(
            "Richtig!",
            "Sehr gut!"
        )

        for btn in antwort_buttons:
            if btn["text"] == auswahl:
                btn.config(bg="green")

    else:
        print("FALSCH!")

        messagebox.showerror(
            "Falsch!",
            f"Richtige Antwort: {richtige}"
        )

        for btn in antwort_buttons:
            if btn["text"] == auswahl:
                btn.config(bg="red")

    punkte_label.config(text=f"Punkte: {punkte}")

    root.after(1500, naechste_frage)

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

    falsche = []

    for btn in antwort_buttons:
        if btn["text"] != richtige:
            falsche.append(btn)

    entfernen = random.sample(falsche, 2)

    for btn in entfernen:
        btn.config(state="disabled")

    joker_5050 = False

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
        width=30,
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

root.bind("<Key>", taste)

# =========================
# Highscore speichern
# =========================
def speichere_highscore():

    daten = []

    if os.path.exists(HIGHSCORE_DATEI):

        with open(HIGHSCORE_DATEI, "r") as f:
            daten = json.load(f)

    daten.append({
        "name": spieler,
        "punkte": punkte
    })

    daten = sorted(
        daten,
        key=lambda x: x["punkte"],
        reverse=True
    )

    with open(HIGHSCORE_DATEI, "w") as f:
        json.dump(daten, f, indent=4)

# =========================
# Rangliste anzeigen
# =========================
def zeige_highscores():

    if not os.path.exists(HIGHSCORE_DATEI):
        return

    with open(HIGHSCORE_DATEI, "r") as f:
        daten = json.load(f)

    text = "RANGLISTE\n\n"

    for eintrag in daten[:10]:
        text += (
            f"{eintrag['name']} "
            f"- {eintrag['punkte']} Punkte\n"
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