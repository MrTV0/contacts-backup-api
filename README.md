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
Hierdoor word een enkele gebruiker getoond met al de contacten van die gebruiker en al de telefoonnummers van de contacten van die gebruiken.

![Get_User](https://user-images.githubusercontent.com/57659923/210568730-454a58d5-5e6c-4904-be1d-41850a5517a5.png)

### Get al de contacten
Hierdoor worden al de contacten en al de telefoonnummers van die contacten getoont.

![Get_Contacts](https://user-images.githubusercontent.com/57659923/211242827-64b647c0-31be-4926-95fd-ca52e0cb8a35.png)

### Get al de telefoonnummers
Hierdoor worden al de telefoonnummers en hun label getoont.

![Get_Numbers](https://user-images.githubusercontent.com/57659923/211242836-00a6b1c5-b394-4b92-8e5d-e3faf7a165b1.png)

### Update (PUT) een telefoonnummer
Bij deze PUT moet je een telefoonnummer en het label voor dat telefoonnummer meegeven als body.

![Put_Number](https://user-images.githubusercontent.com/57659923/211242844-326a732e-cf4b-45ba-999a-9c790dcc5820.png)

### Delete een gebruiker
Bij het deleten van een gebruiker word de gebruiker, al de contacten van die gebruiker en al de telefoonnummers van die contacten van die gebruiker verwijderd.

![Delete_User](https://user-images.githubusercontent.com/57659923/211247413-70807dc0-12fd-4927-b61c-e45f290bcb40.png)

## Tests
Al de GET en niet GET (POST, PUT, DELETE) endpoints zijn getest op meerdere scenarios.

![All_Tests](https://user-images.githubusercontent.com/57659923/211242569-1d2dbee0-0053-46c3-b333-a46bd417d3e4.png)

## FastAPI
![screencapture-contacts-backup-mrtv0-cloud-okteto-net-docs-2023-01-09-05_44_57](https://user-images.githubusercontent.com/57659923/211242502-2bc28413-1e61-405d-900a-18e81d7a2d64.png)

