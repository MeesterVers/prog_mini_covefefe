stations = ['Utrecht Centraal', 'Amsterdam Amstel', 'Amsterdam Centraal', 'Den Bosch']

def gebruikers_input(stations):
    while True:
        station = input('Bij welk station bevindt u zich: ')
        if station not in stations:
            print('Geef een geldig station AUB!')
        else:
            print('U bevindt zich bij {}'.format(station))
            break
gebruikers_input(stations)
