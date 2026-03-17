#Laajenna ohjelmaa siten, että mukana on kulje-metodi, 
#joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa
#sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
#Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
#Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun 
#matkan lukemaan 2090 km.

class Car:
    def __init__(self, plate, max_speed, current_speed = 0, distance = 0):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance = distance

def kulje(self, hours, speed):
    self.distance = hours * speed

    def accelerate(self, v0, v1):
        self.current_speed = self.current_speed + v1
        if self.current_speed < 0:
            self.current_speed=0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

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