# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja 
# ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös
# ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle 
# hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu 
# joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy 
# viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen 
# ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa 
# luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi 
# kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

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

elevator1 = Elevator(-1, 10)

elevator1.ride(10)
elevator1.ride(-1)