#Imports
from datetime import datetime

#Eigentlich import from util.py
def ask_question(question):
    print(question)
    response = input().lower()
    return response

def ask_yes_no(question):
    while True:
        response = input(question).lower()
        if response in ['y', 'yes', 'ja']:
            return True
        elif response in ['n', 'no', 'nein']:
            return False
        else:
            print("Invalid response. Please answer with 'y', 'yes', 'ja', 'n', 'no' or 'nein'.")

def kontakt():
    print("HIER DIE KONTAKTMÖGLICHKEITEN ANGEBEN")
    #todo
    
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
  
def text_keyword(text, keywordliste):
    schlagwoerter = []
    textfragmente = text.replace(",", "").split(" ") #Todo ergänzen FEhler bei mehr (TypeError: split() takes at most 2 arguments (5 given))
    for fragment in keywordliste:
        for keyword in fragment:
            if keyword in textfragmente:
                if keyword not in schlagwoerter:
                    schlagwoerter.append(keyword)
    return schlagwoerter        
    #überprüfen-todo
    
def chatbot_frage():
    benutzereingabe = ask_question("Wie kann ich Ihnen helfen?")
    schlagwoerter = text_keyword(benutzereingabe, keywordliste)
    print("das sind die gefundenen Schlagwörter", schlagwoerter) #todo nur zu demo zwecken
    if len(schlagwoerter) != 0:
        for tupil in keywordliste:
            for keyword in tupil:
                if keyword in schlagwoerter:
                    print(keywordliste[tupil])
    else: #todo  logging
        print("Leider habe ich das nicht vertsanden, könnten Sie das bitte wiederholen")        
        
def datenbank_speichern(kategorie, text):
    print("todo")
    #todo
    
#Variable

rechnungsnummer_vorhanden = False

rechnungsliste = ["22056348","23018349"]

keywordliste = {("moin", "hallo", "gott", "servus"): "Moin, wie kann ich Ihnen helfen?",
                ("wetter",): "Das kann ich Ihnen nicht beantworten. Schauen Sie doch aus dem Fenster oder lesen Sie das Thermometer ab.",
                ("öffnungszeiten", "oeffnungszeiten"): "Unsere Öffnungszeiten sind 24 Stunden und 7 Tage die Woche. Wir sind ein OnlineShop. Bitte beachten Sie, dass unser Lager nicht am Wochenende arbeitet und dementsprechend es über das Wochenende zu längeren Lieferzeiten kommen kann.",
                ("vergessen", "zurücksetzen", "zuruecksetzen"): "Gehen Sie auf den Link 'Passwort vergessen'. Darüber können Sie ihr Passwort zurücksetzen. Schauen Sie dazu bitte in Ihren Posteingang.",
                ("zahlungsmethode",): "Wir akzeptieren bei uns im Onlineshop Visa, PayPal und Vorkasse.",
                ("abholen",): "Eine Abholung vor Ort ist bei uns leider nicht möglich, da wir ein reines Onlinegeschäft sind.",
                ("zurückgeben", "zurueckgeben", "umtauschen"): "Ja, das ist unter bestimmten Begebenheiten möglich. Schauen Sie bitte dazu in unsere Allgemeinen Geschäftsbedingungen (AGB) unter den Abschnitt Widerrufsrecht.",
                ("versand",): "Der Versand dauert 1-3 Werktage. Ab 50€ Bestellwert ist der Versandt kostenlos. Anderfalls fallen 4,90€ Versandkosten an.",
                ("benutzerkonto",): "Ein Konto können Sie direkt bei der ersten Bestellung anlegen.",
                ("versandoptionen"): "Wir versenden unsere Ware nach Wunsch per Hermes, DHL und DPD.",
                ("verfolgung",): "Ja eine Verfolgung des Pakets ist möglich. Einen entsprechenden Link erhalten Sie von dem von Ihrem gewählten Paketzusteller. Es können dabei zusätzliche Kosten anfallen.",
                ("kundenbewertung", "rezession", "rezesszionen", "kundenbewertungen"): "Ja die gibt es. Scrollen Sie dafür bei dem gewünschten Produkt ein wenig nach unten.",
                ("kundenservice", "support", "kundensupport"): "Haben Sie es schon mit einem Neustart des Geräts versucht? Ist das Betriebssystem aktuell und sind alle Treiber auf dem aktuellen Stand? Ist dies der Fall, kontaktieren Sie bitte unseren Kundensupport unter folgender Telefonnummer: 040 66969 666. Alternativ sind wir auch per Mail unter folgender E-Mail-Adresse zu erreichen: support@group20.com.",
                ("beschädigt", "beschaedigt", "kaputt"): "Bitte wenden Sie sich dafür an unseren Kundensupport per E-Mail unter support@group20.com. Bitte in der Betreffzeile: Ware beschädigt, Rechnungsnummer. Außerdem Bitte wir Sie gleich ein paar Bilder mitzuschicken, damit wir den Fehler möglichst schnell beheben können.",
                ("treueprogramm", "treue", "prämie", "praemie", "prämien", "praemien"): "Nein, so etwas haben wir leider nicht."
                }

#Begrüßung
print("Willkommen beim Chatbot")
print("Um Ihre Identität zu bestimmen, geben Sie bitte Ihre 8 stellige Rechnungsnummer ein")
rechnungsnummer = ask_question("Sollten Sie keine haben, geben Sie bitte 1234 ein")
rechnn = False
if rechnungsnummer == "1234":
    kontakt()
else:
    if rechnungsnummer in rechnungsliste:
        print("Vielen Dank!")
        rechnungsnummer_vorhanden = True
    else:
        print("Leider ist die Rechnungsnummer uns nicht bekannt")
        kontakt()
        
if rechnungsnummer_vorhanden:
    gewaehrleistungsanspruch = pruefe_gewaehrleistungsanspruch(rechnungsnummer)
else:
    print("Leider besteht kein Gewähleistungsanspruch")

if gewaehrleistungsanspruch:
    trial = 0
    while trial < 4:
        chatbot_frage()
        trial + 1
    else:
        print("Anscheinend konnte ich Ihnen nach 3 VErsuchen nicht helfen")
        print("ich bitte wenden Sie sich an den Kundensupport")
        kontakt