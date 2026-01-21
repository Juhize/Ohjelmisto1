#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
#niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

sentti = float(input("Tuumat: "))
while sentti > 0:
    print(f"Tuuman senteissä {sentti * 2.54:.2f}")
    sentti = float(input("Tuumat: "))
print("error")