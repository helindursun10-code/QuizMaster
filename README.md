# QuizMaster

QuizMaster ist ein lokales Python-Quizspiel mit grafischer Benutzeroberfläche.  
Das Spiel verbindet Fragen zur TH OWL und zur Stadt Herford mit verschiedenen Quizmechaniken wie Zeitlimit, Jokern, Punkteberechnung und einer dauerhaft gespeicherten Rangliste.

## Thema

Das Spiel enthält Fragen zur:

- TH OWL
- Stadt Herford

## Zielgruppe

Das Spiel richtet sich insbesondere an:

- potenzielle Studierende
- Studierende
- Personen mit Interesse an der TH OWL und Herford

## Projektziel

Ziel des Projekts ist die Entwicklung eines verständlich bedienbaren Quizspiels in Python.

Dabei werden verschiedene typische Funktionen eines Quizspiels miteinander verbunden. Dazu gehören unter anderem:

- vier Antwortmöglichkeiten pro Frage
- zufällige Fragen
- gemischte Antwortreihenfolge
- steigende Schwierigkeit
- verschiedene Spielmodi
- Zeitlimit
- Joker
- Punkteberechnung
- Rangliste
- dauerhafte Highscore-Speicherung
- Maus- und Tastatursteuerung
- Ein- und Zwei-Spieler-Modus

## Funktionen

- 4 Antwortmöglichkeiten pro Frage
- sichtbare Nummerierung der Antworten von 1 bis 4
- Fragen zur TH OWL und Herford
- zufällige Auswahl der Fragen
- zufällige Reihenfolge der Antworten
- steigende Schwierigkeit
- 3 einfache Fragen pro Runde
- 3 mittlere Fragen pro Runde
- 3 schwere Fragen pro Runde
- insgesamt 9 Fragen pro Runde
- Fair-Modus
- Hard-Modus
- 50:50-Joker
- Anrufjoker
- Zeitjoker
- Frage-wechseln-Joker
- jeder Joker nur einmal pro Runde
- Zeitlimit pro Frage
- Eingabe und Prüfung von Spielernamen
- Punkteberechnung
- Highscore-Rangliste
- Speicherung der Rangliste in `highscores.json`
- Anzeige der 10 besten Ergebnisse
- Ein-Spieler-Modus
- Zwei-Spieler-Modus
- Maussteuerung
- Tastatursteuerung
- Startmenü
- Regelanzeige
- grafische Benutzeroberfläche mit Tkinter

## Spielregeln

Eine Runde besteht aus insgesamt 9 Fragen.

Die Schwierigkeit steigt im Spielverlauf:

1. zuerst 3 einfache Fragen
2. danach 3 mittlere Fragen
3. zuletzt 3 schwere Fragen

Zu jeder Frage gibt es vier Antwortmöglichkeiten.

Die sichtbaren Antwortfelder sind mit den Nummern 1 bis 4 gekennzeichnet. Dadurch können Antworten sowohl per Maus als auch über die entsprechenden Zahlentasten ausgewählt werden.

Bei einer richtigen Antwort erhält der Spieler Punkte.

Die Punkte hängen von der Schwierigkeitsstufe ab:

- einfache Frage: 10 Punkte
- mittlere Frage: 20 Punkte
- schwere Frage: 30 Punkte

Bei einer falschen Antwort endet die aktuelle Spielerrunde.

Auch wenn die Zeit abläuft, endet die aktuelle Spielerrunde.

## Spielmodi

QuizMaster besitzt zwei Spielmodi:

### Fair-Modus

- einfache Fragen: 30 Sekunden
- mittlere Fragen: 25 Sekunden
- schwere Fragen: 20 Sekunden

### Hard-Modus

- einfache Fragen: 20 Sekunden
- mittlere Fragen: 15 Sekunden
- schwere Fragen: 10 Sekunden

## Joker

Im Spiel gibt es vier Joker:

- **50:50-Joker:** Zwei falsche Antworten werden entfernt.
- **Anrufjoker:** Zeigt einen individuellen Hinweis zur aktuellen Frage.
- **Zeitjoker:** Fügt 10 Sekunden zur verbleibenden Zeit hinzu.
- **Frage-wechseln-Joker:** Ersetzt die aktuelle Frage durch eine andere Frage derselben Schwierigkeitsstufe.

Jeder Joker kann pro Runde nur einmal verwendet werden.

Nach einer bereits gegebenen Antwort können keine Joker mehr eingesetzt werden.

## Tastatursteuerung

Antworten:

- `1` = Antwort 1
- `2` = Antwort 2
- `3` = Antwort 3
- `4` = Antwort 4

Joker:

- `F` = 50:50-Joker
- `A` = Anrufjoker
- `Z` = Zeitjoker
- `W` = Frage-wechseln-Joker

Die Tastatursteuerung ist nur während aktiver Fragen aktiviert.

## Zwei-Spieler-Modus

Im Zwei-Spieler-Modus spielen beide Personen nacheinander.

Zuerst spielt Spieler 1 eine vollständige Runde. Danach spielt Spieler 2 eine vollständige Runde.

Nach beiden Runden werden die Ergebnisse miteinander verglichen.

## Highscore

Nach einer Spielerrunde werden folgende Daten gespeichert:

- Spielername
- Punktzahl
- Spielmodus

Die Ergebnisse werden lokal in der Datei `highscores.json` gespeichert.

Dadurch bleiben gespeicherte Ergebnisse auch nach dem Schließen und erneuten Starten des Programms erhalten.

Die Rangliste wird nach Punktzahl absteigend sortiert. In der sichtbaren Rangliste werden die 10 besten Ergebnisse angezeigt.

## Eingabeprüfung

Beim Start des Spiels werden verschiedene Eingaben geprüft.

### Spieleranzahl

Akzeptiert werden:

- `1`
- `01`
- `eins`
- `2`
- `02`
- `zwei`

### Spielernamen

- dürfen nicht leer sein
- dürfen maximal 15 Zeichen enthalten
- dürfen bei zwei Spielern nicht doppelt vergeben werden

Bei der Prüfung doppelter Namen werden Groß- und Kleinschreibung sowie Leerzeichen berücksichtigt.

### Spielmodus

Akzeptiert werden:

- `Fair`
- `F`
- `Hard`
- `H`

Groß- und Kleinschreibung spielen keine Rolle.

## Benutzeroberfläche

Die grafische Benutzeroberfläche wurde mit Tkinter umgesetzt.

Die Anwendung enthält unter anderem:

- Startmenü
- Regelanzeige
- Spielerinformationen
- Modusanzeige
- Schwierigkeitsanzeige
- Punkteanzeige
- Timer
- Fragetext
- nummerierte Antwortfelder
- Joker-Buttons
- Ranglistenfenster
- sichtbare Rückmeldungen bei richtigen und falschen Antworten

Bei einer richtigen Antwort wird eine grüne Rückmeldung angezeigt.

Bei einer falschen Antwort wird die gewählte Antwort rot und die richtige Antwort grün markiert. Zusätzlich wird ein auffälliger visueller Effekt angezeigt.

## Datenspeicherung

Die Highscores werden lokal in der Datei `highscores.json` gespeichert.

Das Programm verwendet:

- keine externe API
- keinen Server
- keine klassische Datenbank

## Dateien

- `QuizMaster.py`: Hauptprogramm des Spiels
- `highscores.json`: lokal gespeicherte Rangliste
- `README.md`: Projektbeschreibung
- `.gitignore`: Dateien, die von Git ignoriert werden sollen

## Voraussetzungen

Benötigt wird:

- Python 3
- Tkinter

Tkinter ist bei vielen Python-Installationen bereits enthalten.

## Starten des Spiels

Im Projektordner ausführen:

```bash
python QuizMaster.py
