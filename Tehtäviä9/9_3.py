#Laajenna ohjelmaa siten, että mukana on kulje-metodi, 
#joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa
#sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
#Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
#Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun 
#matkan lukemaan 2090 km.

class Car:
    def __init__(self, plate, max_speed, current_speed = 0, distance = 2000):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance = distance

    def kulje(self, hours, speed):
        self.distance = hours * speed + self.distance
        return self.distance

    def accelerate(self, v0, v1):
        self.current_speed = self.current_speed + v1
        self.current_speed = min(self.current_speed, self.max_speed)
        self.current_speed = max(0, self.current_speed)

        if v1 < 0:
            print("Auto hidastaa")
        elif v1 > 0:
            print("Auto kiihdyttää")
        else:
            print("Auton kiihtyvyys on 0")
        return self.current_speed

car1 = Car("ABC-123", 142)

car1.kulje(1.5, 60)
print(f"Auton 1 kuljettu matka on nyt {car1.distance:.0f} km")
