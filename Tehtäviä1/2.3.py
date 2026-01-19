#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
#Ohjelma tulostaa suorakulmion piirin ja pinta-alan.

print("Hei!\nVoin laskea suorakulmion pinta-alan, kun kerrot sen kannan ja korkeuden.")
korkeus = float(input("korkeus: "))
kanta = float(input("kanta: "))
pinta = (kanta)*(korkeus)

print("Suorakulmion pinta-ala on: " + str(pinta))