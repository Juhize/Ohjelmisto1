#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

kolme = random.randint(0, 9)
neljä = random.randint(0, 6)

print(str(kolme) + str(kolme) + str(kolme) + "\n" + str(neljä) + str(neljä) + str(neljä) + str(neljä))