#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan 
#(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
#Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa 
#järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen
#ja for/in toistorakennetta niiden läpikäymiseen.

kaupungit = []
#kaupungit määritellään listaksi
for i in range (5):
    #Määritellään for loopin pituudeksi 5, muuttujalla i ei ole tässä tehtävässä merkitystä
    kaupunki = str(input("Kaupunki: "))
    kaupungit.append(kaupunki)
    #Lisätään inputin kaupunki listaan kaupungit, mikä luotiin alussa
for a in kaupungit:
    #Pyydetään uutta silmukkaa kirjoittamaan lista kaupungit, milloin ne saadaan omille riveille
    print(a)