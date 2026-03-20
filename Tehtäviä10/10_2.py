# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. 
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero 
# sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän
# hissejä. Hissien lista tallennetaan talon ominaisuutena. 
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron
# ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja 
# talon hisseillä ajelemiseksi.

class Building:
    def __init__(self, top_floor, lowest_floor, num_elevators):
        self.top_floor = top_floor
        self.lowest_floor

class Elevator:
    def __init__(self, ground_floor, roof_floor):
        self.ground = ground_floor
        self.roof = roof_floor
        self.floor = ground_floor

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
