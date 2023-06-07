# Chatbot
Chatbot vom Lernfeld 6

In der Datei tags.json wird eine Liste mit den Tags und Antworten gebaut, die die AI zum lernen braucht.
Ergänzungen werden gerne gesehen.
Der bereich Tag gibt die KAtegorie an, hier bitte etwas sinnvoles wählen.
Patterns gibt die benutzereingabe wieder, je mehr desto besser, hieraus lernt die AI.
Responses gibt die Antworten wieder, sollte es hier mehrere geben, wird wilkürlich ausgewählt

TODO: 
#Passwort Richard 
#Service verkaufen Richard
Liste implementieren mit kundenanfragen ?
antworten Jan
Switchcase Leon
Texterkennung Jonas

Aufgabenstellung:

Must have (max. Note 3)

Der Chatbot ist sinnvoll in den Service Level Prozess integriert (d.h. er passt zum erstellten EPK). 
Der Chatbot sollte genaue und relevante Informationen liefern.
Der Code des Chatbots wird in einem online Repository (Gitlab, Github, …) bereitgestellt und per Link an das Lehrer:innen-Team in KW 22 kommuniziert
mind. 5 Commits (klar ersichtlich) von jedem Teammitglied

Should have (max. Note 2)

Der Code ist nachvollziehbar dokumentiert
Gelingt es dem Chatbot nicht, eine Anfrage zu lösen, leitet er diese an eine:n Mitarbeiter:in weiter oder gibt alternative Kontaktmöglichkeiten an.
Die Readme-Datei im Repository ist sinnvoll mit nachhaltigem Inhalt gepflegt
Der Optimierungsprozess (des Chatbots) wird über Issues geregelt bzw. dokumentiert (mind. 3)

Could have (Note 1)

Supportanfragen, die der Chatbot nicht erfolgreich lösen konnte, werden in einer Datenbank protokolliert.
Die Sicherstellung der Qualität der Integration des verwendeten Chatbots kann durch eine Teststrategie erläutert werden.

# Gingerdude27/Chatbot

## Einführung

Gingerdude27/Chatbot ist ein in Python geschriebenes Chatbot-Programm, das darauf ausgelegt ist, mit Nutzern zu interagieren, indem es Fragen beantwortet und Antworten basierend auf Schlüsselwortübereinstimmungen bietet. Das Chatbot verwendet SQLite3 als Datenbank, um nicht erkannte Benutzereingaben für weitere Analysen und Verbesserungen zu verfolgen.

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

## Mitwirken

Beiträge sind willkommen! Zögern Sie nicht, ein Issue zu eröffnen oder einen Pull Request einzureichen, wenn Sie Verbesserungen oder Feature-Anfragen haben.

Bitte beachten Sie, dass dieses Projekt mit einem Verhaltenskodex für Mitwirkende veröffentlicht wird. Durch die Teilnahme an diesem Projekt erklären Sie sich damit einverstanden, dessen Bedingungen einzuhaltenquote("Imports\n\nimport sqlite3\n\nfrom datetime", "Bitte antworten Sie mit 'y', 'yes', 'ja', 'n', 'no' or 'nein'.")
quote("def kontakt():\n\nprint(\"Bitte kontaktieren Sie", "E-Mail: support@sehrwichtigefirma.de\n\nprint(\"Telefon: 040 123456789\")")
quote("def pruefe_gewaehrleistungsanspruch(rechnungsnummer):\n\n#Jahr und Monat aus", "return rechnungs_datum > vor_zwei_jahren")
quote("def text_keyword(text, keywordliste):\n\nschlagwoerter = []", "return schlagwoerter")
quote("def chatbot_frage():\n\nbenutzereingabe = ask_question(\"Wie kann", "Leider habe ich hierzu keine Informationen. Bitte versuchen Sie es erneut.\"")
quote("def initialize_database():\n\ntry:\n\n# Connect to", "finally:\n\nconn.close()")
quote("def save_unrecognized_input(input_text):\n\ntry:\n\n# Connect to", "finally:\n\nconn.close()")
quote("#Variablen\n\n\nrechnn = False\n\n\nrechnungsnummer_vorhanden = False", "\"beschädigt\", \"beschaedigt\", \"kaputt\"): \"Haben Sie es schon mit einem Neustart des Geräts versucht? Ist das Betriebssystem aktuell und sind alle Treiber auf dem aktuellen Stand? Ist dies der Fall, wenden Sie sich bitte dafür an unseren Kundensupport per E-Mail unter support@group20.com. Bitte in der Betreffzeile: Ware beschädigt, Rechnungsnummer. Außerdem Bitte wir Sie gleich ein paar Bilder mitzuschicken, damit wir den Fehler möglichst schnell beheben können.\",\n\n(\"treueprogramm\", \"treue\", \"prämie\", \"praemie\", \"prämien\", \"praemien\"): \"Nein, so etwas haben wir leider nicht.")
