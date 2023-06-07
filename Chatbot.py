#Imports
from datetime import datetime
import random

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
        print("Leider konnte ich das  ")        
    
    #for word in schlagwoerter:
     #   print(word)
      #  if word in keywordliste:
       #     print(keywordliste[word]) 
    #Todo
        
def datenbank_speichern(kategorie, text):
    print("todo")
    #todo
    
#Variable

rechnungsnummer_vorhanden = False

rechnungsliste = ["22056348","23018349"]

keywordliste = {("moin", "hallo"): "Moin, wie kann ich helfen?",
                ("router","monitor"): "Neustart",
                ("wetter"): "Das kann ich Ihnen nicht beantworten. Schauen Sie doch aus dem Fenster oder lesen Sie das Thermometer ab."}

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

if gewaehrleistungsanspruch:
    trial = 0
    while trial < 4:
        chatbot_frage()
        trial + 1