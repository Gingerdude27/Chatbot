#v 0.1 = Erster Commit; Begrüßung und erste Abfrage
#v 0.2 = Abfrage Passwort
#v 0.3 = Anfordern eines Kundenpasswortes als Service
#v 0.4 = Beenden des Bots und weiterleiten an Support

#Begrüßung des Users
print("Willkomen beim Chatbot der Gruppe 20")

#Abfrage ob der Benutzer berechtig ist
authentification = False
while authentification == False:
    print("Um ihre Identität festzustellen, geben Sie bitte Ihr 4 stelliges Passwort ein")
    print("Solten Sie keins haben geben Sie bitte 0000 ein")
    user_passwort = input();
    if (user_passwort == "1234"):
        print("Vielen Dank")
        authentification = True
#Hier wird abgefragt ob der Benutzer Kunde ist und nur nen Passwort braucht oder ob wir einen Neukunden gewinnen können
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
            exit #soll programm beenden
        else:
            print("Bitte teilen sie uns Ihre E-mail Adresse mit und wir melden uns bei Ihnen")
            kundenmail = input() #In Liste eintragen
            print("Vielen Dank und bis bald")
            exit #soll programm beenden
    else:
        print("Das war falsch")

#Ab hier bbeginnt der Chat Teil
print("Zum beenden schreiben sie bitte ENDE")

#Benutzereingabe
trialcount = 0
while trialcount < 3: #Hier würd überprüft ob der Benutzer schon mehr als 3 Anläufe braucht
    print("Wie kann ich Ihnen weiterhelfen")
    frage = input()
    if frage != "ENDE":
        print("Hallo") #Hier Frage Antwort
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