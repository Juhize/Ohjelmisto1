#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin,
#tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

käyttäjä = str
salasana = str
while käyttäjä != str("python") or salasana != str("rules"):
    käyttäjä = str(input("Käyttäjätunnus: "))
    salasana = str(input("Salasana: "))
    if käyttäjä != str("python") or salasana != str("rules"):
        print("Pääsy evätty.")
print("Tervetuloa!")