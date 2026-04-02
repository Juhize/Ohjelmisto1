#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def prime(luku):
    luku = int(luku)
    response = True
    if luku >= 2:
        for i in range(2, luku):
            if luku%i == 0:  
                response = False
                break

    return str(f"Number: {luku} isPrime: {response}")

app.run(use_reloader=True, host='127.0.0.1', port=3000)