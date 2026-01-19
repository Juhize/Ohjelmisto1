#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Sukupuoli m vai n? ")
hb = int(input("Mikä on rauta-arvosi kokonaislukuna? "))

if sukupuoli =="m" and 134 <= hb <=  195:
    print("Hemoglobiinisi on viitearvossa")
elif sukupuoli =="n" and 117 <= hb <= 175:
    print("Hemoglobiinisi on viitearvossa")
else:
    print("Hemoglobiinisi ei ole viitearvossa")