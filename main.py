import requests
import xmltodict

def get_hudige_station():
    read_settings_file = open('settings.txt', 'r')
    settings = read_settings_file.readlines()
    read_settings_file.close()
    return settings[1]
# get_hudige_station def

def update_settings():
    settings_lijst = []
    username = input("Username: ")
    wachtwoord = input("Wachtwoord: ")
    login_credentials = username + ";" + wachtwoord + "\n"
    login_status = "failed"

    read_settings_file = open('settings.txt', 'r')
    settings = read_settings_file.readlines()
    read_settings_file.close()

    if login_credentials == settings[0]:
        print("login good")
        automaat_station = input("Naam van het station: ")

        settings_lijst.append(login_credentials)
        settings_lijst.append(automaat_station)

        write_to_settings = open('settings.txt', 'w')
        for setting in settings_lijst:
            write_to_settings.write(setting)
        write_to_settings.close()
    else:
        print("login failed")
# einde update_settings def

def get_stations(station):  # Haalt de actuele NS reisinformatie
    auth_details = ('max.bosch@student.hu.nl', '9bftbs4MpvNZ2Q-WJe70aKE1c3gm4Kef23ekTq6r9-U8ddVTNWUkYw') # Inloggegevens API
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station  # URL van API die opgehaald moet worden
    response = requests.get(api_url, auth = auth_details)   # Wat de API terug geeft
    # print(response.text)

    vertrekXML = xmltodict.parse(response.text)
    print('\nDit zijn de vertrkkende treinen:')
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:

        # XML key routetekst is in een try omdat het er niet altijd is
        try:
            trein_tussen_stops = ",\nVia " + vertrek['RouteTekst']
        except KeyError:
            trein_tussen_stops = ""
        # XML key routetekst is in een try omdat het er niet altijd is

        # XML key reistip is in een try omdat het er niet altijd is
        try:
            reis_tip = "\nReistip: " + vertrek['ReisTip']
        except KeyError:
            reis_tip = ""    
        # XML key reistip is in een try omdat het er niet altijd is    

        type_trein = vertrek['TreinSoort'] #XML key de trein soort
        vertrekspoor = vertrek['VertrekSpoor']['#text'] #Haal van Key vertrek de kee #Text
        eindbestemming = vertrek['EindBestemming'] #XML key
        vertrektijd = vertrek['VertrekTijd'] #XML key no sliced string dus bv. 016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16] #slice die string naar bv. 18:36.
        print("Om {} van spoor {} vertrekt een {} naar {}{}{} \n" .format(vertrektijd, vertrekspoor, type_trein, eindbestemming, trein_tussen_stops,reis_tip))
# einde get_stations def

get_stations(get_hudige_station())    # Naam van  het vertrekpunt