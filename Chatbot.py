#Imports
import sqlite3
from datetime import datetime

#Funktion erstellt eine Frage (Variable) und gibt einen String mit der Antwort zurück
def ask_question(question): 
    print(question)
    response = input().lower()
    return response

#Funktion erstellt eine Frage und gibt ein Boolean zurück
def ask_yes_no(question): 
    print(question)
    while True:
        response = input().lower()
        if response in ['y', 'yes', 'ja']:
            return True
        elif response in ['n', 'no', 'nein']:
            return False
        else:
            print("Bitte antworten Sie mit 'y', 'yes', 'ja', 'n', 'no' or 'nein'.")

#Funktion gibt Kontaktmöglichkeiten aus
def kontakt():
    print("Bitte kontaktieren Sie uns unter folgender E-Mail oder Telefonnummer:")
    print("E-Mail: support@sehrwichtigefirma.de")
    print("Telefon: 040 123456789")

#Funktion bekommt eine Variable und überprüft ob noch ein Anspruch besteht; gibt einen Boolean zurück
def pruefe_gewaehrleistungsanspruch(rechnungsnummer): 
    #Jahr und Monat aus Rechnungsnummer herausfinden
    rechnungs_jahr = int(rechnungsnummer[0:2]) + 2000
    rechnungs_monat = int(rechnungsnummer[2:4]) 

    #Berechne das Datum
    heute = datetime.now()
    vor_zwei_jahren = heute.replace(year = heute.year - 2)

    #Erstellt ein Datum-Objekt mit Jahr und Monat aus der Rechnungsnummer
    rechnungs_datum = vor_zwei_jahren.replace(year = rechnungs_jahr, month = rechnungs_monat)

    #Überprüfung
    return rechnungs_datum > vor_zwei_jahren
 

#Funktion bekommt einen String und zerlegt diesen in einzelne Worte, diese werden dann mit der Keywortliste abgeglichen und wenn sie vorhanden sind als Liste ausgegeben
def text_keyword(text, keywordliste): 
    schlagwoerter = []
    textfragmente = text.replace(",", "").replace("?", "").replace("!", "").replace("-", "").replace(".", "").split(" ")
    for fragment in keywordliste:
        for keyword in fragment:
            if keyword in textfragmente:
                if keyword not in schlagwoerter:
                    schlagwoerter.append(keyword)
    return schlagwoerter        

#Funktion erstellt eine Frage, fasst den Text in Schlagworte zusammen und gibt eine Antwort, welche er aus einer Liste auswählt
def chatbot_frage():
    benutzereingabe = ask_question("Wie kann ich Ihnen helfen?")
    schlagwoerter = text_keyword(benutzereingabe, keywordliste)
    print("[Debug] gefundene Schlagwörter", schlagwoerter)
    if len(schlagwoerter) != 0:
        for tupil in keywordliste:
            for keyword in tupil:
                if keyword in schlagwoerter:
                    print(keywordliste[tupil])
    else:
        save_unrecognized_input(benutzereingabe)
        print("Leider habe ich hierzu keine Informationen. Bitte versuchen Sie es erneut.")        

#Initalisiert eine SQLite Datenbank
def initialize_database():
    try:
        # Connect to the database or create a new one if it doesn't exist
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Check if the table 'unrecognized_inputs' exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='unrecognized_inputs'")
        table_exists = cursor.fetchone()

        if not table_exists:
            # Create the 'unrecognized_inputs' table if it doesn't exist
            cursor.execute('''CREATE TABLE unrecognized_inputs
                              (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               UserInput TEXT,
                               Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        print("[Debug] Datenbank initialisiert")
        conn.commit()
    except Exception as e:
        print("[Debug] An error occurred while initializing the database:", str(e))
    finally:
        conn.close()
       
#Funktion bekommt einen String als Input und speichert den in der Datenbank
def save_unrecognized_input(input_text):
    try:
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Insert the unrecognized input into the table
        cursor.execute("INSERT INTO unrecognized_inputs (UserInput) VALUES (?)", (input_text,))

        # Save the changes and close the connection
        conn.commit()

        print("[Debug] Unbekannte Anfrage in Datenbank protokolliert")
    except Exception as e:
        print("[Debug] An error occurred while saving the unrecognized input:", str(e))
    finally:
        conn.close()



#Variablen

rechnn = False

rechnungsnummer_vorhanden = False

gewaehrleistungsanspruch = False

trial = 0

rechnungsliste = ["20056348", "22056348","23018349"]

#In diesem Dictonary werden alle Schlagwörter und Antworten gespeichert
keywordliste = {("moin", "hallo", "gott", "servus"): "Moin!",
                ("wetter",): "Das kann ich Ihnen nicht beantworten. Schauen Sie doch aus dem Fenster oder lesen Sie das Thermometer ab. Alternativ können wir noch einen Wetterbericht Ihrer Wahl empfehlen.",
                ("öffnungszeiten", "oeffnungszeiten"): "Unsere Öffnungszeiten sind 24 Stunden und 7 Tage die Woche. Wir sind ein OnlineShop. Bitte beachten Sie, dass unser Lager nicht am Wochenende arbeitet und es dementsprechend über das Wochenende zu längeren Lieferzeiten kommen kann.",
                ("vergessen", "zurücksetzen", "zuruecksetzen"): "Gehen Sie auf den Link 'Passwort vergessen' im Browser. Darüber können Sie ihr Passwort zurücksetzen. Schauen Sie anschließend bitte in Ihren Posteingang.",
                ("zahlungsmethode",): "Wir akzeptieren bei uns im Onlineshop Visa, PayPal und Vorkasse.",
                ("abholen",): "Eine Abholung vor Ort ist bei uns leider nicht möglich, da wir ein reines Onlinegeschäft sind.",
                ("zurückgeben", "zurueckgeben", "umtauschen"): "Ja, das ist unter bestimmten Begebenheiten möglich. Schauen Sie bitte dazu in unsere Allgemeinen Geschäftsbedingungen (AGB) unter den Abschnitt Widerrufsrecht.",
                ("versand",): "Der Versand dauert 1-3 Werktage. Ab 50€ Bestellwert ist der Versandt kostenlos. Anderfalls entstehen Versandkosten in Höhe von 4,90€.",
                ("benutzerkonto",): "Ein Konto können Sie direkt bei der ersten Bestellung anlegen.",
                ("versandoptionen"): "Wir versenden unsere Ware nach Wunsch per Hermes, DHL und DPD.",
                ("verfolgung",): "Ja eine Verfolgung des Pakets ist möglich. Einen entsprechenden Link erhalten Sie von dem von Ihrem gewählten Paketzusteller. Es können dabei zusätzliche Kosten anfallen.",
                ("kundenbewertung", "rezession", "rezessionen", "kundenbewertungen"): "Ja die gibt es. Scrollen Sie dafür bei dem gewünschten Produkt ein wenig nach unten.",
                ("kundenservice", "support", "kundensupport"): "Ja, unser Kundensupport ist unter folgender Telefonnummer erreichbar: 040 66969 666. Alternativ sind wir auch per Mail unter folgender E-Mail-Adresse zu erreichen: support@group20.com.",
                ("beschädigt", "beschaedigt", "kaputt"): "Haben Sie es schon mit einem Neustart des Geräts versucht? Ist das Betriebssystem aktuell und sind alle Treiber auf dem aktuellen Stand? Ist dies der Fall, wenden Sie sich bitte dafür an unseren Kundensupport per E-Mail unter support@group20.com. Bitte in der Betreffzeile: Ware beschädigt, Rechnungsnummer. Außerdem Bitte wir Sie gleich ein paar Bilder mitzuschicken, damit wir den Fehler möglichst schnell beheben können.",
                ("treueprogramm", "treue", "prämie", "praemie", "prämien", "praemien"): "Nein, so etwas haben wir leider nicht."
                }

initialize_database()

#Begrüßung
print("Willkommen beim Chatbot")

#Abfrage der Rechnungsnummer und Abgleich ob diese vorhanden ist, optional Möglichkeit direkt den Support zu kontaktieren
if ask_yes_no("Haben Sie eine Rechnungsnummer?"):
    rechnungsnummer = ask_question("Geben Sie bitte Ihre Rechnungsnummer(8 Zeichen) ein")
    if rechnungsnummer in rechnungsliste:
        print("Vielen Dank!")
        rechnungsnummer_vorhanden = True
    else:
        print("Leider ist uns diese Rechnungsnummer nicht bekannt")
        kontakt()
else:
    kontakt()

#Hier wird geprüft ob ein Gewährleistungsanspruch besteht       
if rechnungsnummer_vorhanden:
    gewaehrleistungsanspruch = pruefe_gewaehrleistungsanspruch(rechnungsnummer)
	
#Kunde fragt 3x den Chatbot, dann wird er zum Support weitergeleitet
if gewaehrleistungsanspruch:
    while trial < 4:
        chatbot_frage()
        trial += 1
    else:
        print("Es tut mir leid dass ich Ihnen mein auch weiterhin nicht helfen kann.")
        kontakt()
elif rechnungsnummer_vorhanden:
    print("Leider besteht kein Gewährleistungsanspruch mehr da ihr Kauf bereits mehr als zwei Jahre zurückliegt.")