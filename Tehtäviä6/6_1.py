# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan
# satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
d6 = random.randint (1,6)

def palautus():

while d6 == 6:
    print(d6)