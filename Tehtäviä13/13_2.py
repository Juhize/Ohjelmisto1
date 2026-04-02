#Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

import mysql.connector
from flask import Flask, Response
import json

yhteys_sql = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='osku',
    password='1230',
    autocommit=True
)

kursori = yhteys_sql.cursor()

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def prime(icao):
    try:
        kursori.execute(f"SELECT name, Municipality from airport WHERE ident = '{icao}'")
        data = (kursori.fetchall())
        name = data[0][0]
        muni = data[0][1]
    
        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "ICAO": icao,
            "Name": name,
            "Municipality": muni
            }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen ICAO"
        }
#    return str(f"ICAO: {icao} Name: {name} Municipality: {muni}")
    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")

app.run(use_reloader=True, host='127.0.0.1', port=3000)