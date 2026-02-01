#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista 
#paitsi että siitä on karsittu pois kaikki parittomat luvut.
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

jono = []

def lista():
    syöte = input("Luku: ")
    if syöte != str(""):
        luku = int(syöte)
        if luku%2 == 0:
            jono.append (luku)
        return True
    else:
        return False
syöte = True
while syöte == True:
    syöte = lista()

summa = sum(jono)
print ("Syötit parilliset luvut: " + str(jono))
print ("Näiden summa on: " + str(summa))