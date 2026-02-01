# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math
pizzat = []
määrä = 0

def pizza():
    halkaisija = float(input("Pizzan halkaisija: "))
    hinta = float(input("Hinta: "))
    arvo = (halkaisija/2)**2*math.pi/hinta
    pizzat.append(arvo)

while määrä<2:
    määrä = määrä + 1
    pizza()

if pizzat[0] < pizzat[1]:
    print(f"Ensimmäinen pizza antaa paremman vastineen rahalle ({pizzat[0]:.2f}€)")
else:
    print(f"Toinen pizza antaa paremman vastineen rahalle ({pizzat[1]:.2f}€)")