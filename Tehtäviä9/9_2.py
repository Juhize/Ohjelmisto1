#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
#joka saa parametrinaan nopeuden muutoksen (km/h).
#Jos nopeuden muutos on negatiivinen, auto hidastaa. 
#Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
#Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa
#pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan
#ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
#Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä
#nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa 
#ei tarvitse vielä päivittää.

class Car:
    def __init__(self, plate, max_speed):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, v0, v1):
        self.current_speed = self.current_speed + v1
        #Saimpas tehtyä näin
        self.current_speed = min(self.current_speed, self.max_speed)
        self.current_speed = max(0, self.current_speed)
        #Jätän nämä kommentteihin, jos jostain syystä tuo aikaisempi ei toimi.
        # if self.current_speed < 0:
        #     self.current_speed=0
        # if self.current_speed > self.max_speed:
        #     self.current_speed = self.max_speed

        if v1 < 0:
            print("Auto hidastaa")
        elif v1 > 0:
            print("Auto kiihdyttää")
        else:
            print("Auton kiihtyvyys on 0")
        return self.current_speed

car1 = Car("ABC-123", 142)

car1.accelerate(car1.current_speed, 30)
print(f"{car1.current_speed}")
car1.accelerate(car1.current_speed, 70)
print(f"{car1.current_speed}")
car1.accelerate(car1.current_speed, -200)
print(f"{car1.current_speed}")