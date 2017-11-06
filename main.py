import requests
import xmltodict
import time


def get_stations(station):  # Haalt de actuele NS reisinformatie
    auth_details = ('max.bosch@student.hu.nl', '9bftbs4MpvNZ2Q-WJe70aKE1c3gm4Kef23ekTq6r9-U8ddVTNWUkYw') # Inloggegevens API
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station  # URL van API die opgehaald moet worden
    response = requests.get(api_url, auth = auth_details)   # Wat de API terug geeft
    vertrekXML = xmltodict.parse(response.text)
    print(response.text)

    print('Vertrekkende treinen:')
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        vertrektijd = vertrektijd.time.strptime(str,fmt='%H:%M')
        eindbestemming = vertrek['EindBestemming']
        vertrektijd = vertrek['VertrekTijd']    # Vertrektijd van de treinen
        vertrektijd = vertrektijd[vertrektijd]    # Vertrektijd treinen
    print('Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming)

get_stations('ut')    # Naam van  het vertrekpunt