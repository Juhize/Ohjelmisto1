#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

yksi = random.randint(0, 9)
kaksi = random.randint(0, 9)
kolme = random.randint(0, 9)

nyksi = random.randint(0, 6)
nkaksi = random.randint(0, 6)
nkolme = random.randint(0, 6)
nneljä = random.randint(0, 6)

print(str(yksi) + str(kaksi) + str(kolme) + "\n" + str(nyksi) + str(nkaksi) + str(nkolme) + str(nneljä))