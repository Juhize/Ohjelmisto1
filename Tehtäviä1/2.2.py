#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

import math
säde_str = input("Ilmoita ympyrän säde, niin lasken sen pinta-alan: ")
säde = float(säde_str)
pinta = (säde**2)*math.pi
print("Ympyrän pinta-ala on: " + str(pinta))
