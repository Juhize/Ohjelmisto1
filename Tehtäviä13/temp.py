import mysql.connector

yhteys_sql = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='osku',
    password='1230',
    autocommit=True
)

kursori = yhteys_sql.cursor()
while True:   
    icao = input("Syötä ICAO-koodi: ")
    if icao=="":
        break
    kursori.execute(f"SELECT name, iso_country from airport WHERE ident = '{icao}'")
    print(kursori.fetchall())
