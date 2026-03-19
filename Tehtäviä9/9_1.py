#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus,
#huippunopeus, tämänhetkinen nopeus ja kuljettu matka. 
#Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin
#mainittua parametreina saatuihin arvoihin. Uuden auton nopeus
#ja kuljetut matka on asetettava automaattisesti nollaksi.
#Kirjoita pääohjelma, jossa luot uuden auton 
#(rekisteritunnus ABC-123, huippunopeus 142 km/h).
#Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:

    def __init__(self, plate, max_speed):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

car1 = Car("ABC-123", "142 km/h")

print(f"Plate: {car1.plate}\nMax Speed: {car1.max_speed}")
