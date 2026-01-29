#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. 
#Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

luku = int(input("Anna luku: "))
#Annettu luku ei saa olla pienempi, kuin 2
if luku >= 2:
    for i in range(2, luku):
        if luku%i == 0:
            # jaetaan annettu luku kaikilla "rangella" olevilla luvuilla -1 (luku jää ilman -1 jo pois tästä joukosta)
            print("Luku ei ole alkuluku")
            break
        #Jos jossakin jakolaskussa on desimaaleja %, ohjelma kirjoittaa, että luku ei ole alkuluku, minkä jälkeen loopin suorittaminen pysäytetään
    else :
        print("Luku on alkuluku")
        #Jos if looppi ei keskeydy ohjelma tulostaa luvun olevan alkuluku