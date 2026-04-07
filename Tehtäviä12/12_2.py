# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. 
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä 
# vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan 
# dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat 
# rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat 
# Kelvin-asteet muunnettua Celsius-asteiksi.

import requests

key = "024b8ef3eb642620a0ff6b3f4b0a1bb4"
#key = "d5617b002ed2b89c33043122a30586b8"
city = input("Kaupunki: ")
country = "FI"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country},&appid={key}"
response = requests.get(url)

try: 
    response.raise_for_status()
    data = response.json()
    print(data["wind"]["deg"])

#print(f"Lämpötila kaupungissa {city} on: "{data["wind"]["deg"]})

except Exception as error:
    print(f"Error: {error}")