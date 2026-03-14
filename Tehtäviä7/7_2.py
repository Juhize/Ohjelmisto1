#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
#kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen 
#ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
#syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet
#yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. 
#Käytä joukkotietorakennetta nimien tallentamiseen.

import random
nimet = []
nimi = "jotain"
while nimi != "":
    nimi = input("Anna nimi: ")
    if nimi == "":
        random.shuffle(nimet)
        for nimi in nimet:
            print(nimi)
            nimi=""
    elif nimi not in nimet:
        nimet.append(nimi)
        print("Syötit uuden nimen!")
    else:
        print("nimi on jo listassa")