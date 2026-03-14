# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. 
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
import mysql.connector
#Tämän kurssin projektissa ryhmässäni käytettiin käyttäjää osku tietokannassa, joten käytän myös tässä.
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='osku',
    password='1230',
)
kursori = yhteys.cursor()
while True:   
    icao = input("Syötä ICAO-koodi: ")
    if icao=="":
        break
    kursori.execute(f"SELECT name, iso_country from airport WHERE ident = '{icao}'")
    print(kursori.fetchall())
