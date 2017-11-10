import requests

auth_details = ('max.bosch@student.hu.nl','9bftbs4MpvNZ2Q-WJe70aKE1c3gm4Kef23ekTq6r9-U8ddVTNWUkYw')
api_url = ('http://webservices.ns.nl/ns-api-avt?station=ut')

response = requests.get(api_url, auth=auth_details)

print(response.text)
# voor het printen van de xml file

#with open('vertrektijden.xml', 'w') as myXMLFile:
#   myXMLFile.write(response.text)
#om de info in een bestand op te slaan

#import xmltodict
#print('Dit zijn de vertrekkende treinen: ')
#for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
#   eindbestemming = vertrek['EindBestemming']
#   vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
#   vertrektijd = vertrektijd[11:16] # 18:36
#   print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)

