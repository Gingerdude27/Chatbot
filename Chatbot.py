#v 0.1 = Erster Commit; Begrüßung und erste Abfrage
#v 0.2 = Abfrage Passwort
#v 0.3 = Anfordern eines Kundenpasswortes

#Begrüßung des Users
print("Willkommen beim Chatbot der Gruppe 20")

#Kundenfragen + Antworten
Keywords = ["Wo","Produkte","Öffnungszeiten","Wetter"]
Antworten_Keywords = ["Unsere Produkte finden Sie unter Beispiel.de.","Unsere Öffnungszeiten sind täglich von 9 bis 18 Uhr.","Das kann ich Ihnen nicht beantworten. Schauen Sie doch aus dem Fenster oder lesen Sie das Thermometer ab."

#Abfrage ob der Benutzer berechtigt ist
authentification = False
while authentification == False:
    print("Um ihre Identität festzustellen, geben Sie bitte Ihr 4 stelliges Passwort ein")
    print("Solten Sie keins haben geben Sie bitte 0000 ein")
    user_passwort = input();
    if (user_passwort == "1234"):
        print("Vielen Dank")
        authentification = True
#Hier wird abgefragt ob der Benutzer Kunde ist und nur ein Passwort braucht oder ob wir einen Neukunden gewinnen können
    elif (user_passwort == "0000"):
        print("Sie werden zu unseren Angeboten weitergeleitet")
        print("Wir bieten verschidene Service Optionen an")
        print("Sind Sie schon Kunde bei uns?")
        kundenstatus = input("y/n");
        if (kundenstatus ==  "y"):
            print("Bitte geben sie hier Ihre Kundennummer ein")
            kundennummer = input()
            print("Vielen Dank ein Kundenbetreuer meldet sich in Kürze bei Ihnen") #In Liste eintragen
            print("Vielen Dank und bis bald")
            exit #soll Programm beenden
        else:
            print("Bitte teilen sie uns Ihre E-mail Adresse mit und wir melden uns bei Ihnen")
            kundenmail = input() #In Liste eintragen
            print("Vielen Dank und bis bald")
            exit #soll Programm beenden
    else:
        print("Das war falsch")
#
print("Zum beenden schreiben sie bitte ENDE")
print("Wie kann ich Ihnen weiterhelfen")
print("")

#Benutzereingabe
user_input = input("Ihre Frage: ") #Hier wird der Input generiert
print(user_input) #Ausgabe der Benutzereingabe
