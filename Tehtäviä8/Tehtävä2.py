# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin. 
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector
#Tämän kurssin projektissa ryhmässäni käytettiin käyttäjää osku tietokannassa, joten käytän myös tässä.
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='osku',
    password='1230',
)
iso=input("Syötä maatunnus: ").upper()
kursori = yhteys.cursor()
kursori.execute(f"SELECT type FROM airport WHERE iso_country = '{iso}' AND type != 'closed' ORDER BY type;")
tulos = (kursori.fetchall())
airports = []
small_airports = []
medium_airports = []
large_airports = []
#Tämän hetkisessä tietokannassa ei ole helikopterikenttiä, mutta samaan tyyliin voisi lisätä, jos olisi

for airport in tulos:
    if airport[0] == "small_airport":
        small_airports.append(airport[0])
print(f"{len(small_airports)} kappaletta pientä lentokenttää.")

for airport in tulos:
    if airport[0] == "medium_airport":
        medium_airports.append(airport[0])
print(f"{len(medium_airports)} kappaletta keskikokoista lentokenttää.")

for airport in tulos:
    if airport[0] == "large_airport":
        large_airports.append(airport[0])
print(f"{len(large_airports)} kappaletta suurta lentokenttää.")
