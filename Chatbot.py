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
  
def text_in_bestandteile(benutzereingabe,fuellwoerter):
    bausteine_benutzereingabe = benutzereingabe.split(" ", ",", "!", "?")
    for wort in bausteine_benutzereingabe:
        if wort in fuellwoerter:
            bausteine_benutzereingabe.remove(wort)
    return bausteine_benutzereingabe        
    #überarbeiten-todo
    
def chatbot_frage():
    benutzereingabe = ask_question("Wie kann ich Ihnen helfen?")
    
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

#Begrüßung
print("Willkomen beim Chatbot")
print("Um Ihre Identität zu bestimmen, geben Sie bitte Ihre 8 stellige Rechnungsnummer ein")
rechnungsnummer = ask_question("Sollten Sie keine haben geben Sie bitte 1234 ein")
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
    gewaehleistungsanspruch = pruefe_gewaehrleistungsanspruch()

if gewaehleistungsanspruch:
    trial = 0
    while trial < 4:
        chatbot_frage()