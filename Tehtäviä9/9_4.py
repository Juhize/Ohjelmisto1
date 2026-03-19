#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan
#automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu 
#kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton
#huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus
#luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. 
#Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#     Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan 
#     väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.

#     Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. 
#     Tämä tehdään kutsumalla kulje-metodia.

#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
#Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi
#muotoiltuna.
import random
race_cars = []
class Car:
    def __init__(self, plate, max_speed=(None), current_speed = 0, distance = 0):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance = distance
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
        race_cars.append(Car(f"ABC-{i+1}"))
    return race_cars
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