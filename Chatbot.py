#Imports
#Eigentlich import from util.py
def ask_question(question):
    print(question)
    response = input()
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
    print("HHIER DIE KONTAKTMÖGLICHKEITEN ANGEBEN")

def pruefe_gewaehrleisttungsanspruch(rechnungsnummer):
    #Todo 
    #Abgleich ob der Anspruch schon verjährt ist
    #funktion bekommt rechnungsnummer und gibt true/false aus
    #funktion informiert anwender ob er noch anspruch hat und wenn ja wie lange 
    print("unfug") 

def chatbot_frage():
    #Todo
    print("unfug")
    
#Variable

rechnungsliste = ["11221234", "01183579"]

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
    gewaehleistungsanspruch = pruefe_gewaehrleisttungsanspruch()

if gewaehleistungsanspruch:
    trial = 0
    while trial < 4:
        chatfrage()