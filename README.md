# QuizMaster
QuizMaster ist ein Python-Quizspiel im Stil von „Wer wird Millionär?“.

## Thema
Das Spiel enthält Fragen zur TH OWL und zur Stadt Herford.

## Zielgruppe
Das Spiel richtet sich an:
- potenzielle Studierende
- Studierende
- Personen mit Interesse an TH OWL und Herford

## Projektziel
Ziel des Projekts ist es, ein spielbares Quiz in Python zu entwickeln.  
Dabei sollen typische Elemente eines Quizspiels umgesetzt werden, zum Beispiel Fragen mit vier Antwortmöglichkeiten, Joker, Zeitlimit, Punkte und Highscore.

## Funktionen
- 4 Antwortmöglichkeiten pro Frage
- Fragen zu TH OWL und Herford
- zufällige Reihenfolge der Fragen
- zufällige Reihenfolge der Antworten
- steigende Schwierigkeit
- 3 einfache Fragen
- 3 mittlere Fragen
- 3 schwere Fragen
- 50:50-Joker
- Anrufjoker
- Hinweis Joker
- Tausch Joker
- Timer Joker
- jeder Joker nur einmal pro Spiel
- Zeitlimit pro Frage
- Benutzername
- Punkteberechnung
- Highscore-Rangliste
- Speicherung der Rangliste
- Zweier-Modus
- einfache grafische Oberfläche mit Tkinter

## Spielregeln
Der Spieler beantwortet insgesamt 9 Fragen.
Die Schwierigkeit steigt im Spielverlauf:
1. zuerst 3 einfache Fragen
2. danach 3 mittlere Fragen
3. zuletzt 3 schwere Fragen

Zu jeder Frage gibt es vier Antwortmöglichkeiten.  
Bei einer richtigen Antwort erhält der Spieler Punkte.  
Bei einer falschen Antwort endet das Spiel.

## Joker
Im Spiel gibt es zwei Joker:
- 50:50-Joker: Zwei falsche Antworten werden entfernt.
- Hinweis Joker: Tipp für das Lösungswort
- Tausch Joker: Frage mit einer anderen aus der selben Kategorie tauschen
- Timer Joker: +10 Sekunden extar Zeit 

## Zeitlimit
Für jede Frage gibt es ein Zeitlimit.  
Das Zeitlimit hängt vom Schwierigkeitsgrad ab:
- einfache Fragen: 20 Sekunden
- mittlere Fragen: 15 Sekunden
- schwere Fragen: 10 Sekunden

## Highscore
Die Ergebnisse werden in der Datei `highscores.json` gespeichert.  
Dadurch bleibt die Rangliste auch nach dem Schließen des Spiels erhalten.

## Dateien
- `QuizMaster.py`: Hauptprogramm des Spiels
- `highscores.json`: gespeicherte Rangliste
- `README.md`: Projektbeschreibung
- `.gitignore`: Dateien, die Git ignorieren soll

## Starten des Spiels
python QuizMaster.py
