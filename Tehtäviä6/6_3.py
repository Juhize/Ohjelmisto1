# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

gallonaM = 1

def muunnos():
    gallona = float(input("Gallonat: "))
    litra = gallona * 3.785
    if gallona > 0:
        print(str(litra) + " litraa")
    return gallona

while gallonaM >= 0:
    gallonaM = muunnos()