#Imports
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
    textfragmente = text.replace(",", "", "?", ".", "!", "-").split(" ") if " " in text else [text]
    for fragment in keywordliste:
        for keyword in fragment:
            if keyword in textfragmente:
                if keyword not in schlagwoerter:
                    schlagwoerter.append(keyword)
    return schlagwoerter        

#Funktion erstellt eine Frage, fasst den Text in Schlagworte zusammen und gibt eine Antwort, welche er aus einer Liste auswählt
def chatbot_frage(): #todo logging 
    benutzereingabe = ask_question("Wie kann ich Ihnen helfen?")
    schlagwoerter = text_keyword(benutzereingabe, keywordliste)
    print("[Debug] das sind die gefundenen Schlagwörter", schlagwoerter)
    if len(schlagwoerter) != 0:
        for tupil in keywordliste:
            for keyword in tupil:
                if keyword in schlagwoerter:
                    print(keywordliste[tupil])
    else: #todo  logging
        print("Leider habe ich hierzu keine Informationen. Bitte versuchen Sie es erneut.")        
       
def datenbank_speichern(kategorie, text): #todo 
    print("todo")
    #todo


#Variablen

rechnn = False

rechnungsnummer_vorhanden = False

gewaehrleistungsanspruch = False

trial = 0

rechnungsliste = ["22056348","23018349"]

keywordliste = {("moin", "hallo", "gott", "servus"): "Moin, wie kann ich Ihnen helfen?",
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
        print("Anscheinend konnte ich Ihnen nach 3 Versuchen nicht helfen,")
        print("bitte wenden Sie sich an den Kundensupport")
        kontakt()
elif rechnungsnummer_vorhanden:
    print("Leider besteht kein Gewährleistungsanspruch")