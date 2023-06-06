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
  
def text_in_bestandteile(text,zu_loeschende_woerter):
    bausteine_benutzereingabe = text.split(" ", ",", "!", "?")
    for wort in bausteine_benutzereingabe:
        if wort in zu_loeschende_woerter:
            bausteine_benutzereingabe.remove(wort)
    return bausteine_benutzereingabe        
    #überarbeiten-todo
    
def chatbot_frage():
    benutzereingabe = ask_question("Wie kann ich Ihnen helfen?")
    bausteine_benutzereingabe = text_in_bestandteile(benutzereingabe, fuellwoerter)
    print(bausteine_benutzereingabe) #todo nur zu demo zwecken
    #Todo
    
    print("todo")
    
def datenbank_speichern(kategorie, text):
    print("todo")
    #todo
    
#Variable

rechnungsliste = ["22056348","23018349"]

fuellwoerter = [",", "!", "?", "also", "eigentlich", "wirklich", "irgendwie", "halt", "eben", "sozusagen", "quasi", "wie gesagt", "na", "genau", "ja",
                "ganz", "sicherlich", "offensichtlich", "nun", "doch", "aber", "dennoch", "trotzdem", "allerdings", "jedenfalls", "sowieso",
                "vielleicht", "eventuell", "möglicherweise", "wohl", "vermutlich", "wohl", "eher", "kaum", "weniger", "einigermaßen", "ziemlich",
                "extrem", "absolut", "total", "völlig", "wahrscheinlich", "in",  "der", "Regel", "normalerweise", "meistens","üblicherweise", "häufig",
                "selten", "manchmal", "gelegentlich", "hin", "und", "wieder", "oft", "fast", "immer", "im", "grunde", "grundsätzlich", "prinzip"]

kategorieliste = {"Begrueßung": ["moin", "hallo", "servus"] }
#die kategorieliste ist wie folgt aufgebaut: Kategorie: [Schlagwort(e)]

antwortliste = {"Begrueßung", "Moin, wie kann ich helfen?"}
#die antwortliste ist wie folgt aufgebaut: Kategorie: [Antwort(en)]
#ACHTUNG es müssen alle Kategorien in aus der kategorieliste hier einen gegenpart haben

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
    gewaehrleistungsanspruch = pruefe_gewaehrleistungsanspruch()

if gewaehrleistungsanspruch:
    trial = 0
    while trial < 4:
        chatbot_frage()