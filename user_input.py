def user_input():
    while True:
        print("\nWelkom bij de NS, Bij welk station bevindt u zich?.")  # Opties vertonen en vragen aan gebruiker
        print("1: Utrecht Centraal")
        print("2: Amsterdam Centraal")
        print("3: Amsterdam Amstel")
        print("4: Rotterdam Centraal")
        print("5: Afsluiten")

        try:
            optie = eval(input("Optie: "))
            if optie == 1:  # API vanaf UC starten
                print("\nU bevindt zich op station: Utrecht Centraal")
                break
            elif optie == 2:    # API vanaf AC starten
                print("\nU bevindt zich op station: Amsterdam Centraal")
                break
            elif optie == 3:    # API vanaf Amsterdam Amstel starten
                print("\nU bevindt zich op station: Amsterdam Amstel")
                break
            elif optie == 4:    # API vanaf Rotterdam Centraal starten
                print("\nU bevindt zich op station: Rotterdam Centraal")
                break
            elif optie == 5:    # Systeem afsluiten en clearen
                print("Totziens")
                break
            else:      # Niet valide nummer
                print("Oops het ingevoerd getal is geen menu optie")
        except NameError:   #Gebruiker vult woord in ipv. nummer
            print("Oops u moet alleen een getal van de menu optie invoeren.")

user_input()