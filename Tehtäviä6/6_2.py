#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan 
#nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä 
#esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä 
#poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan 
#nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman 
#suorituksen alussa.

import random
dice = int(input("Nopan suuruus: "))
heitot = 0

def heitto(koko):
     dice = random.randint (1,koko +1)
     print(dice)
     return dice
tulos = 0
while tulos != dice:
    tulos = heitto(dice)
    heitot = heitot +1
print("Tarvittiin yhteensä: " + str(heitot) + " heittoa.")

#Lisäsin heittolaskurin, tehdäkseni ohjelmasta mielenkiintoisemman