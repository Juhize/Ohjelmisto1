#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. 
#Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
#hakea jo syötetyn lentoaseman tiedot vai lopettaa. 
#Jos käyttäjä valitsee uuden lentoaseman syöttämisen, 
#ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
#Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä 
#vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, 
#ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten
#monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. 
#(ICAO-koodi on lentoaseman yksilöivä tunniste. 
#Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. 
#Löydät koodeja helposti selaimen avulla.)

def lisää(lentoasemat):
    nimi = input("Syötä kentän nimi: ")
    ICAO = input("Syötä kentän IACAO: ")
    lentoasemat[ICAO] = nimi
def hae():
    ICAO = input("Syötä ICAO: ")
    print(lentoasemat[ICAO])
def tulosta_valikko():
    print
    print
    print

lentoasemat = {"EFHK": "Helsinki-Vantaa"}

toiminto = int(input("Syötä toiminto: "))
tulosta_valikko()

while toiminto !=9:
    if toiminto ==1:
        lisää(lentoasemat)
    elif toiminto == 2:
        hae()