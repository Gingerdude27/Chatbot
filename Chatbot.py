#v 0.1 = Erster Commit; Begrüßung und erste Abfrage
#v 0.2 = Abfrage Passwort
#v 0.3 = Anfordern eines Kundenpasswortes als Service
#v 0.4 = Beenden des Bots und weiterleiten an Support
#v 0.5 = Beginnen mit matchcase

#Begrüßung des Users
print("Willkommen beim Chatbot der Gruppe 20")

#Kundenfragen + Antworten
Keywords = ["Wo","Produkte","Öffnungszeiten","Wetter"]
Antworten_Keywords = ["Unsere Produkte finden Sie unter Beispiel.de.","Unsere Öffnungszeiten sind täglich von 9 bis 18 Uhr.","Das kann ich Ihnen nicht beantworten. Schauen Sie doch aus dem Fenster oder lesen Sie das Thermometer ab."]

#Abfrage ob der Benutzer berechtigt ist
authentification = False
while authentification == False:
    print("Um ihre Identität festzustellen, geben Sie bitte Ihr 4 stelliges Passwort ein")
    print("Solten Sie keins haben geben Sie bitte 0000 ein")
    kundennummer = input();
    if (kundennummer == "1234"):
        print("Vielen Dank")
        authentification = True
#Hier wird abgefragt ob der Benutzer Kunde ist und nur ein Passwort braucht oder ob wir einen Neukunden gewinnen können
    elif (kundennummer == "0000"):
        print("Sie werden zu unseren Angeboten weitergeleitet")
        print("Wir bieten verschidene Service Optionen an")
        print("Sind Sie schon Kunde bei uns?")
        kundenstatus = input("y/n");
        if (kundenstatus ==  "y"):
            print("Bitte geben sie hier Ihre Kundennummer ein")
            rechnungsnummer = input()
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

#Ab hier bbeginnt der Chat Teil
print("Zum beenden schreiben sie bitte ENDE")

#Benutzereingabe
trialcount = 0
while trialcount < 3: #Hier würd überprüft ob der Benutzer schon mehr als 3 Anläufe braucht
    print("Wie kann ich Ihnen weiterhelfen")
    frage = input()
    schlüsselwort = frage #Hier aus frage schlüsselworte beziehen
    if frage != "ENDE":
        match schlüsselwort: #Hier Frage Antwort
            case "öffnungszeiten":
                print("Antwort")
            case other:
                print("Das habe ich leider nicht verstanden")
        trialcount + 1
    else:
        trialcount = 2000
else:
    if trialcount < 2000:
        print("Es sieht so aus als ob ich nicht in der Lage bin das Problem zu lösen")
        print("Möchten Sie von einem Mitarbeiter kontaktiert werden?")
        print("ja/nein")
        antwort = input()
        if antwort == "ja":
            kontaktdaten = input()
        else:
            trialcount - 1
    else:
        print("Vielen Dank und bis bald")
