import requests
import xmltodict


def get_stations(station):  # Haalt de actuele NS reisinformatie
    auth_details = ('max.bosch@student.hu.nl', '9bftbs4MpvNZ2Q-WJe70aKE1c3gm4Kef23ekTq6r9-U8ddVTNWUkYw') # Inloggegevens API
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station  # URL van API die opgehaald moet worden
    response = requests.get(api_url, auth = auth_details)   # Wat de API terug geeft
    print(response.text)



get_stations('Utrecht Centraal')    # Naam van  het vertrekpunt