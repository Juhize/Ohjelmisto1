# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka,
# jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien 
# autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän 
# ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

#   tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin 
#   välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu 
#   kullekin autolle kulje-metodia.

#   tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot 
#   selkeäksi taulukoksi muotoiltuna.
#   kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut 
#   vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". 
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa 
# tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa 
# tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, 
# onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla 
# kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

import random
race_cars = []
class Competition:
    def __init__(self, name, distance, competitors):
        self.name = name
        self.distance = distance
        competitors = race_cars

class Car:
    noc=0 #number of cars
    def __init__(self, plate, max_speed=(None)):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0
        Car.noc+=1
        if self.max_speed == None:
            self.max_speed = random.randint(100, 200)
    
    def kulje(self, hours, speed):
        self.distance = hours * speed + self.distance
        return self.distance

    def accelerate(self, v1):
        self.current_speed = self.current_speed + v1
# Funktio min vertaa arvoja self.current_speed ja self.max_speed ja valitsee näistä pienemmän.
        self.current_speed = min(self.current_speed, self.max_speed)
# Funktio max vertaa self.current_speediä arvoon 0 ja valitsee arvoista suuremman.
        self.current_speed = max(0, self.current_speed)
        return self.current_speed
    
    def __str__(self):
        return f"{self.plate}, Huippunopeus: {self.max_speed} km/h, Nopeus kilpailun päättyessä: {self.current_speed} km/h, Kuljettu matka: {self.distance}"
    
def build(how_many):
    for i in range(0, how_many):
        race_cars.append(Car(f"ABC-{Car.noc +1}"))

build(10)
race_time = 0
while max([car.distance for car in race_cars]) <= 10000:
    for car in race_cars:
        car.accelerate(random.randint(-10, 15))
    for car in race_cars:
        car.kulje(1, car.current_speed)
    race_time = race_time + 1
# Python ei osaa purkaa yksittäisiä arvoja suoraan olio listasta ilman funktiota.
# Opettelin tätä varten nyt lambdan käyttöä, jotta koodi pysyy yksinkertaisena.
# 1. key= määrittelee minkä mukaan lista järjestetään
# 2. key:nä käytetään minifunktiota lambda car: car.distance 
# -> car on tätä funktiota varten nimetty yksittäisen olion nimi (vaikka molemmat car:t korvaisi sanalla blep, funktio toimii)
# 3. funktio hakee jokaiselta listan oliolta ominaisuuden distance
# 4. Lopuksi määritellään pilkun jälkeen järjestys käänteiseksi
race_cars.sort(key=lambda car: car.distance, reverse=True)
print(f"Kisa päättyi ajassa: {race_time} tuntia.")
list_key=1
for car in race_cars:
    print(f"{list_key}. {car}")
    list_key += 1