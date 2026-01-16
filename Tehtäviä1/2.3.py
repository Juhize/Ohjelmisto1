#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
#Ohjelma tulostaa suorakulmion piirin ja pinta-alan.

print("Hei!\nVoin laskea suorakulmion pinta-alan, kun kerrot sen kannan ja korkeuden.")
korkeus_str = input("korkeus: ")
korkeus = float(korkeus_str)
kanta_str = input("kanta: ")
kanta = float(kanta_str)
pinta = (kanta)*(korkeus)

print("Suorakulmion pinta-ala on: " + str(pinta))