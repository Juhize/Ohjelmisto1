#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten
#mittojen mukaan leivisköinä, nauloina ja luoteina.
#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä
#ilmoittaa tuloksen käyttäjälle.

#    Yksi leiviskä on 20 naulaa.
#    Yksi naula on 32 luotia.
#    Yksi luoti on 13,3 grammaa.

leivi_str = input("Anna leiviskät. ")
leivi = int(leivi_str)
naula_str = input("Anna naulat. ")
naula = int(naula_str)
luoti_str = input("Anna luodit. ")
luoti = int(luoti_str)

massa = (leivi*20*32*13.3)+(naula*32*13.3)+(luoti*13.3)
kilo_str = (massa/1000)
kilo = int(kilo_str)
gramma = (massa % 1000)

print("Massa nykymittojen mukaan: " + str(kilo) + " kilogrammaa" f" ja {gramma:.2f} ""grammaa.")
