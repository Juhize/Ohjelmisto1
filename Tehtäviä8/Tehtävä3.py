# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. 
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. 
import mysql.connector
from geopy import distance
#Tämän kurssin projektissa ryhmässäni käytettiin käyttäjää osku tietokannassa, joten käytän myös tässä.
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='osku',
    password='1230',
)

kursori = yhteys.cursor()
kentta1 = input("Syötä ensimmäisen kentän ICAO: ").upper()
kentta2 = input("Syötä toisen kentän ICAO: ").upper()
kursori.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{kentta1}'")
tulos1 = kursori.fetchall()
kursori.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{kentta2}'")
tulos2 = kursori.fetchall()
laskettu_matka = distance.distance(tulos1[0], tulos2[0]).km
print(f"Kenttien välinen etäisyys on {laskettu_matka:.1f}km")