# The Contacts Back-up API
Maakt u zich zorgen dat uw contacten zoek geraken door uw telefoon te verliezen?
Heeft u de gegevens van uw contacten ergens liggen maar vergeet u steeds waar u ze gelegd heeft?

De contacts back-up API is de API om al uw contacten op te slagen als back-up en op te vragen wanneer u maar wilt. Elke gebruiker kan een account aanmaken en heeft de mogelijkheid om al hun contacten in te geven met volledige naam, emailadres welke niet verplicht is en het telefoonnummer waar meerdere telefoonnummers ingeven zeker een mogelijk is. Bij elk telefoonnummer moet u enkel een label toevoegen. Zo weet u makkelijk of het een werk, thuis of andere telefoonnummer is.

## Postman
### Posten van een gebruiker
Bij het posten van een gebruiker moet er een body worden meegegeven met daarin de naam, het emailadres en wachtwoord welke de informatie minus het wachtwoord teruggeeft om validatie te tonen aan de gebruiker dat de post succesvol was.
![Post_User](https://user-images.githubusercontent.com/57659923/210564723-85d25431-8537-4a76-baa3-6ece9161b438.png)

### Posten van een contact
Bij het posten van een contact moet er een body worden meegegeven met daarin de naam en eventueel het emailadres welke de informatie teruggeeft om validatie te tonen aan de gebruiker dat de post succesvol was.
![Post_Contact](https://user-images.githubusercontent.com/57659923/210565320-79f7222a-e18e-4565-aece-06586f384587.png)

### Posten van een telefoonnummer
Bij het posten van een telefoonnummer moet er een body worden meegegeven met daarin het telefoonnummer en het label welke de informatie teruggeeft om validatie te tonen aan de gebruiker dat de post succesvol was.
![Post_Number](https://user-images.githubusercontent.com/57659923/210567365-3b282c2b-f069-431f-a69e-7333092d454b.png)

### Get al de gebruikers
Hierdoor worden al de gebruikers getoond met al de contacten van elke gebruiker en van elk contact al de telefoonnummers. De optie om te filteren op hoeveel gebruikers er getoond moeten worden is ook mogelijk.
![Get_Users](https://user-images.githubusercontent.com/57659923/210567530-317119e7-bbb2-4ff6-8e60-e13e617d2b15.png)

### Get een gebruiker
Hierdoor word een enkele gebruiker getoond met al de contacten van die gebruiker en al de nummers van de contacten van die gebruiken.
![Get_User](https://user-images.githubusercontent.com/57659923/210568730-454a58d5-5e6c-4904-be1d-41850a5517a5.png)

### Get al de contacten


### Get al de telefoonnummers


### Put als

![screencapture-api-db-mrtv0-cloud-okteto-net-docs-2023-01-03-21_52_50](https://user-images.githubusercontent.com/57659923/210560444-3c47f02e-16d0-499d-8f14-f47e90d71a2f.png)
