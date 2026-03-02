#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
#jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). 
#Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina 
#monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden 
#mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

kuukausi_nro = int(input("Kuukausi numero: "))
kuukaudet =["talvi","talvi","kevät","kevät","kevät","kesä", "kesä","kesä","syksy","syksy","syksy","talvi"]
vuodenaika = kuukaudet[kuukausi_nro-1]
print (f"Vuodenaika on {vuodenaika}.")