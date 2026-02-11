import mysql.connector

yhteys = mysql.connector.connect(
    host = 127.0.0.1.
    port = 3306
    database = 'flight_game',
    user ='juhani@localhost',
    password = 'r00t'
    autocommit = True
    )

def hae_työntekijät_sukunimellä(sukunimi):
    sql = f"SELECT name, continent FROM country where iso_country='{iso_country}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"lentokenttä, jonka isocountry koodi on {iso_country} sijaitsee maassa {rivi[0]}. Kyseinen maa sijaitsee maanosassa {rivi[1]}.")



sukunimi = input("Anna sukunimi: ")
hae_työntekijät_sukunimellä(sukunimi)