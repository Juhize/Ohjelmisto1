# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. 
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas
# lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat. Tee 
# aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot. 

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja 
# Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki
# tiedot toteuttamiesi metodien avulla.

ankka = Lehti("Aku_Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:0 6", "Rosa Liksom","200")

print(f"Lehti: {ankka.nimi}\nPäätoimittaja: {ankka.päätoimittaja}")
print(f"Kirja: {kirja.nimi}\nKirjailija: {kirja.kirjoittaja}\nSivumäärä: {kirja.sivumäärä}")