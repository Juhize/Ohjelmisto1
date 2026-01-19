#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#
#   Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#    Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Sukupuoli? ")
hb = int(input("Mikä on rauta-arvosi kokonaislukuna? "))

if sukupuoli =="mies" and 134 <= hb <=  195:
    print("ok")
    