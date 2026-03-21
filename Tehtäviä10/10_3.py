# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton
# metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa 
# siten, että talossasi tulee palohälytys.

class Building:
    def __init__(self, lowest_floor, top_floor, num_elevators):
        self.elevators = []
        self.top_floor = top_floor
        self.lowest_floor = lowest_floor
        self.num_elevators = num_elevators
        for i in range(0, num_elevators):
            self.build_elevators(lowest_floor, top_floor, num_elevators)

    def build_elevators(self, lowest_floor, top_floor, num_elevators):
        self.elevators.append(Elevator(f"Elevator{Elevator.noe +1}", self.lowest_floor, self.top_floor))

    def use_elevator(name, floor):
        Elevator.ride(name, floor)

    def fire_alarm(self):
        print("!")
        for elevator in self.elevators:
            Elevator.ride(elevator, self.lowest_floor)
        return

class Elevator:
    noe = 0 #number of elevators
    def __init__(self, name, ground_floor, roof_floor):
        self.name = name
        self.ground = ground_floor
        self.roof = roof_floor
        self.floor = ground_floor
        Elevator.noe += 1

    def __str__(self):
        return f"{self.name} is currently in floor: {self.floor}"

    def ride_up(self):
        self.floor = self.floor +1
        return self.floor
    
    def ride_down(self):
        self.floor = self.floor - 1
        return self.floor

    def ride(self, floor):
        while floor < self.floor:
            if self.floor == self.ground:
                print("This model cannot go bellow ground")
                break
            self.ride_down()
            print(self.floor)
        while floor > self.floor:
            if self.floor == self.roof:
                print("This model cannot fly")
                break
            self.ride_up()
            print(self.floor)
            
building1 = Building(-2, 10, 2)
Building.use_elevator(building1.elevators[0], -5)
Building.use_elevator(building1.elevators[1], 12)
building1.fire_alarm()
for elevator in building1.elevators:
    print(f"{elevator}")