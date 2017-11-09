import requests
import xmltodict

def user_input(message, error_message):
    user_input = ""
    while user_input == "":
        user_input = input(message)
        if user_input == "":
            print(error_message)
    user_input = user_input.title() #laat alle woorden met hoofdletters beginnen
    return user_input
# einde get_stations def

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

def get_vertrek_informatie(station):  # Haalt de actuele NS reisinformatie
    reis_informatie_lijst = []
    auth_details = ('max.bosch@student.hu.nl', '9bftbs4MpvNZ2Q-WJe70aKE1c3gm4Kef23ekTq6r9-U8ddVTNWUkYw') # Inloggegevens API
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station  # URL van API die opgehaald moet worden
    response = requests.get(api_url, auth = auth_details)   # Wat de API terug geeft
    vertrek_xml = xmltodict.parse(response.text)

    for vertrek in vertrek_xml['ActueleVertrekTijden']['VertrekkendeTrein']:
        type_trein = vertrek['TreinSoort'] #XML key de trein soort
        vertrekspoor = vertrek['VertrekSpoor']['#text'] #Haal van Key vertrek de kee #Text
        eindbestemming = vertrek['EindBestemming'] #XML key
        vertrektijd = vertrek['VertrekTijd'] #XML key no sliced string dus bv. 016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16] #slice die string naar bv. 18:36.
        
        # XML key routetekst is in een try omdat het er niet altijd is
        try:
            trein_tussen_stops = vertrek['RouteTekst']
        except KeyError:
            trein_tussen_stops = ""
        # XML key routetekst is in een try omdat het er niet altijd is

        # XML key reistip is in een try omdat het er niet altijd is
        try:
            reis_tip = vertrek['ReisTip']
        except KeyError:
            reis_tip = ""    
        # XML key reistip is in een try omdat het er niet altijd is

        # XML key reistip is in een try omdat het er niet altijd is
        try:
            vertrek_vertraging_tekst = vertrek['VertrekVertragingTekst']
        except KeyError:
            vertrek_vertraging_tekst = ""    
        # XML key reistip is in een try omdat het er niet altijd is 

        # XML key reistip is in een try omdat het er niet altijd is
        try:
            opmerkingen = vertrek['Opmerkingen']['Opmerking']
        except KeyError:
            opmerkingen = ""    
        # XML key reistip is in een try omdat het er niet altijd is

        reis_informatie = [vertrektijd, vertrekspoor, type_trein, eindbestemming, trein_tussen_stops, vertrek_vertraging_tekst, reis_tip,opmerkingen]
        reis_informatie_lijst.append(reis_informatie)
    # for reis_informatie in reis_informatie_lijst:
    #     # print(reis_informatie)
    #     print("\n")
    #     print("Vertrektijd:" + reis_informatie[0])
    #     print("Spoor:" + reis_informatie[1])
    #     print("Trein type:" + reis_informatie[2])
    #     print("Eindbestemming:" + reis_informatie[3])
    #     print("Tussen stops:" + reis_informatie[4])
    #     if reis_informatie[5] != "":
    #         print("vertraging: " + reis_informatie[5])
    #     if reis_informatie[6] != "":
    #         print("Reis advies: " + reis_informatie[6])
    #     if reis_informatie[7] != "":
    #         print("Opmerking: " + reis_informatie[7])
    return reis_informatie_lijst
# einde get_vertrek_informatie def

def hudige_vertrek_station():
    read_settings_file = open('settings.txt', 'r')
    settings = read_settings_file.readlines()
    read_settings_file.close()
    hudige_station = settings[1]
    return get_vertrek_informatie(hudige_station)
# get_hudige_station def

def ander_vertrek_station():
    user_station = user_input("Van welk station wilt u reisinformatie? ", "Oops u heeft geen station ingevuld")
    mogelijke_stations = []
    auth_details = ('max.bosch@student.hu.nl', '9bftbs4MpvNZ2Q-WJe70aKE1c3gm4Kef23ekTq6r9-U8ddVTNWUkYw') # Inloggegevens API
    api_url = 'http://webservices.ns.nl/ns-api-stations-v2?_ga=2.25077050.162201735.1509967012-522547314.1504624410' # Station lijst API
    response = requests.get(api_url, auth = auth_details)   # Wat de API terug geeft
    stations_xml = xmltodict.parse(response.text)

    for station in stations_xml['Stations']['Station']:
        if user_station in station['Namen']['Lang']:
            mogelijke_stations.append(station['Namen']['Lang'])

    if len(mogelijke_stations) > 1:
        print("Oops er zijn meerdere stations met de naam {}" .format(user_station))
        for station in mogelijke_stations:
            print("{}.{}." .format(mogelijke_stations.index(station)+1 , station))
        user_station = user_input("Zou u een van de stations in het lijstje kunnen kiezen? ", "Oops u heeft geen station ingevuld")
        get_vertrek_informatie(user_station)
    elif len(mogelijke_stations) == 0:
        print("Oops station {} bestaat niet" .format(user_station))
    else:
        user_station = station['Namen']['Lang']
        get_vertrek_informatie(user_station)
# einde ander_vertrek_station def

# hudige_vertrek_station() #reis informatie hudige vertrek station werkt met settings file.. staat nu op utrecht.. settings md5 encrypten??
# ander_vertrek_station()  #reis informatie andere vertrek station