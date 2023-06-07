# Gingerdude27/Chatbot

## Einführung

Gingerdude27/Chatbot ist ein in Python geschriebenes Chatbot-Programm welches für das Lernfeld 6 erstellt wurde.

## Funktionen

- **Interaktive Antworten**: Das Chatbot stellt dem Benutzer Fragen und reagiert auf Benutzereingaben.
- **Schlüsselwortanalyse**: Das Chatbot analysiert den Benutzereingabetext, extrahiert Schlüsselwörter und gleicht diese mit einer vordefinierten Liste ab, um entsprechende Antworten zu liefern.
- **Behandlung nicht erkannter Eingaben**: Nicht erkannte Benutzereingaben werden in einer SQLite3-Datenbank für weitere Analysen gespeichert.
- **Überprüfung von Garantieansprüchen**: Das Chatbot kann überprüfen, ob ein Garantieanspruch eines Benutzers noch gültig ist, basierend auf der Rechnungsnummer.

## Funktionen

- `ask_question(question: str) -> str`: Stellt eine Frage und gibt die Antwort des Benutzers zurück.
- `ask_yes_no(question: str) -> bool`: Stellt eine Ja/Nein-Frage und gibt die Antwort des Benutzers als booleschen Wert zurück.
- `kontakt()`: Gibt Kontaktinformationen aus.
- `pruefe_gewaehrleistungsanspruch(rechnungsnummer: str) -> bool`: Überprüft, ob der Garantieanspruch noch gültig ist.
- `text_keyword(text: str, keywordliste: list) -> list`: Zerlegt den Benutzereingabetext in einzelne Wörter und gleicht diese mit einer vordefinierten Schlüsselwortliste ab. Gibt eine Liste der gefundenen Schlüsselwörter zurück.
- `chatbot_frage()`: Stellt eine Frage, fasst den Text in Schlüsselwörtern zusammen und wählt eine Antwort aus einer vordefinierten Liste aus.
- `initialize_database()`: Initialisiert die SQLite3-Datenbank und erstellt eine neue Tabelle für nicht erkannte Eingaben, wenn sie nicht existiert.
- `save_unrecognized_input(input_text: str)`: Speichert nicht erkannte Benutzereingaben in der SQLite3-Datenbank.

## Erste Schritte

Um mit diesem Projekt zu beginnen, klonen Sie das Repository und führen Sie `Chatbot.py` aus. Das Chatbot startet im interaktiven Modus und Sie können anfangen, Fragen zu stellen.

## Abhängigkeiten

- Python 3.x
- SQLite3

