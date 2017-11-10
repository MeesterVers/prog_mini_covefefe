# `Covfefe` NS Reis informatie
## Vak: Programmeren

**_De applicatie_**<br>
De applicatie is een reis informatie viewer die samen werkt met twee **NS-API'S** om de gebruikers van alle nodige informatie te voorzien. Deze applicatie moesten we bouwen i.v.m. met het mini-project voor het vak programmeren.

**_Over de API'S_**<br>
We waren verplicht om gebruik te maken van de **NS API: Actuele vertrektijden**, dit is de link naar de documentatie ervan: **[https://www.ns.nl/reisinformatie/ns-api/documentatie-actuele-vertrektijden.html]**. Deze API wordt gebruikt om de vetrektijden van de NS op te halen. Wij hebben ook gebruik gemaakt van de **NS API: Stationslijst** dit is de link naar de documentatie **[https://www.ns.nl/reisinformatie/ns-api/documentatie-stationslijst.html]**. Deze API hebben we gebruikt om de gebruiker te helpen bij het invoeren en zoeken van andere vertrek stations. 

**_Applicatie installatie_**<br>
Om de applicatie te installeren moet u de volgende stappen uitvoeren. Om te kunnen zien hoe de applicatie werkt hebben we een **_Screencast_** gemaakt die kan u vinden op de volgende link **[https://www.youtube.com/watch?v=Qzd6UK7b1Co&feature=youtu.be]**

1. De **Git repo [https://github.com/MeesterVers/prog_mini_covefefe]** moet gefetch of gepulled worden.

2. De volgende genoemde files en folders zijn nodig om de applicatie te draaien.
	<br>-`settings.txt`<br>
	-`main.py`<br>
	-`boot.py`<br>
	-`\images\`

3. Om de applicatie werkend te krijgen moet u enkele libaries installeren, behalve als uw computer of laptop ze al heeft.
	<br>-`Pillow (Pycharm)` for not pycharm users is het `image`<br>
	-`requests`<br>
	-`xmltodict`<br>

4. De `boot.py` is de file die u moet **Runnen** om de applicatie te kunnen gebruiken.

5. De `main.py` is de ondersteunde file, hier in zitten alle functies zoals API calls enz. De functies in de `main.py` returnen altijd lijsten met data naar de **GUI**

6. Na deze stappen te hebben uitgevoerd zou de applicatie moeten werken op uw laptop of computer.