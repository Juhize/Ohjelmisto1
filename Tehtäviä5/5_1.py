#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
#Käytä for-toistorakennetta.

import random
lkm = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0 
#Jotta summa voidaan laskea se täytyy määritellä luvuksi 0
for nopan_nro in range(lkm): 
    #Jokaista nopan numeroa kohden jonossa, joka päättyy arpakuutioiden lukumäärään
    d6 = random.randint(1,6) 
    #Määritellään noppa 6 numeroiseksi randint(1,6)
    summa +=d6 
    #Summaan lisätään arvotut luvut yhdestä kuuteen loopin sisällä
    print(f"noppa {nopan_nro +1}, tulos = {d6}") 
    #Esitetään loopin sisällä missä kohtaa lkm rangea luvut on arvottu ja arvotut "nopat"
print(f"Noppien summa on {summa}")
#Nyt loopin ulkopuolella esitetään arvottujen lukujen yhteenlaskettu summa