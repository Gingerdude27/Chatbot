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

#Variable

rechnungsliste = []
#Begrüßung
print("Willkomen beim Chatbot")
print("Um Ihre Identität zu bestimmen, geben Sie bitte Ihre Rechnungsnummer ein")
rechnungsnummer = ask_question("Sollten Sie keine haben geben Sie bitte 1234 ein")
rechnn = False
if rechnungsnummer == "1234":
    kontakt()
else:
    if rechnungsnummer in rechnungsliste:
        print("Vielen Dank!")
        rechnn = True
    else:
        print("Leider ist die Rechnungsnummer uns nicht bekannt")
        kontakt()
        
if rechnn:
    