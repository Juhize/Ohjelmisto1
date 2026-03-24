# Tässä on esimerkki olio-ohjelmoinnin periytymisestä.

# Polkupyörä-luokalla on ominaisuudet polkupyörän merkki ja vaihteiden lukumäärä.
# Tee luokalle konstruktori, jossa voit asettaa nämä arvot.
# Tee luokalle myös metodi tulosta(), joka tulostaa polkupyörän kaikki tiedot.

# Tee myös luokka Sähköpyörä, joka periytyy Polkypyörä-luokasta.
# Sähköpolkupyörä-luokalla on lisäksi ominaisuudet omistaja sekä toimintasäde sähköllä.
# Hyödynnä aliluokassa (Sähköpolupyörä) sen yliluokan (Polupyörä) valmiita koodeja.

# Tee pääohjelma, jossa luot polkypyörän ja tulostat sen kaikki ominaisuudet.
# Tee lisäksi sähköpolupyörä ja tulosta sen kaikki ominaisuudet.


class Polkupyörä:
    def __init__(self, merkki, vaihteet):
        self.merkki = merkki
        self.vaihteet = vaihteet

    def tulosta(self):
        print(f"Polkupyörän merkki on: {self.merkki}\nVaihteiden lukumäärä on: {self.vaihteet}")
        return
    
class Sähköpyörä(Polkupyörä):
    def __init__(self, merkki, vaihteet, omistaja, toiminta_säde):
        super().__init__(merkki, vaihteet)
        self.omistaja = omistaja
        self.toiminta_säde = toiminta_säde

    def tulosta(self):
        super().tulosta()
        print(f"Tämän pyörän omistaa: {self.omistaja}")
        print(f"Pyörän toimintasäde on: {self.toiminta_säde}")
        
    #--Pääohjelma alkaa--

eka = Polkupyörä("Focus", "21")
toka = Sähköpyörä("Crescent", "16", "Jari", "2000km")
toka.tulosta()