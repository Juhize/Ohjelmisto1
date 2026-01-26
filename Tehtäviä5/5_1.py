#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
#Käytä for-toistorakennetta.

import random
lkm = int(input("Anna arpakuutioiden lukumäärä: "))
#annetaan silmälukujen summaksi 0
summa = 0
#Heitetään noppia haluttu lkm
#Muuttuja nopan_nro on ns. kierroslaskuri
for nopan_nro in range(lkm):
    #Heitetään noppaa yhden kerran
    d6 = random.randint(1,6)
    #Lisätään saatu silmäluku muuttujan summa arvoon
    summa +=d6 # +=summan uusi arvo on summa + d6
    print(f"noppa {nopan_nro +1}, tulos = {d6}")
print(f"Noppien summa on {summa}")