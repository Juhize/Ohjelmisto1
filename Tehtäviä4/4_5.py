#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin,
#tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

käyttäjä = str
salasana = str
kerrat = 0
while käyttäjä != str("python") or salasana != str("rules"):
    if kerrat >=5:
        break
    käyttäjä = str(input("Käyttäjätunnus: "))
    salasana = str(input("Salasana: "))
    if käyttäjä != str("python") or salasana != str("rules"):
        print("Pääsy evätty.")
    else: print("Tervetuloa!")
    kerrat = kerrat + 1
