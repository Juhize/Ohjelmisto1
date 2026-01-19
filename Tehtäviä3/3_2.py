#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) 
#ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. 
#Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#   LUX on parvekkeellinen hytti yläkannella.
#    A on ikkunallinen hytti autokannen yläpuolella.
#    B on ikkunaton hytti autokannen yläpuolella.
#    C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

hytti = input("Anna hyttiluokka ")
if hytti == "LUX" or hytti=="lux" or hytti=="Lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A" or hytti=="a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B"or hytti=="b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C"or hytti=="c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Vireellinen hyttiluokka")