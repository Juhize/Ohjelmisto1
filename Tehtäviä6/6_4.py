# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
jono = []

def lista():
    syöte = input("Luku: ")
    if syöte != str(""):
        luku = int(syöte)
        jono.append (luku)
        return True
    else:
        return False
syöte = True
while syöte == True:
    syöte = lista()

summa = sum(jono)
print ("Syötit luvut: " + str(jono))
print ("Näiden summa on: " + str(summa))