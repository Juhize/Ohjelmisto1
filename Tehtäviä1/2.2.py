#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

import math
säde = float(input("Ilmoita ympyrän säde, niin lasken sen pinta-alan: "))
pinta = (säde**2)*math.pi
print("Ympyrän pinta-ala on: " + str(pinta))
