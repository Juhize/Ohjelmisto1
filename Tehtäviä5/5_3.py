#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. 
#Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
on_alkuluku = True
#tee input osio, mikä kysyy lukua
luku = int(input("Anna luku: "))
#lisää listaan kaikki luvut 2-ja input luvun välillä olevat luvut
#vihje for .range
#jaa input luku jokaisella listan luvulla
#jos prosessi saa aikaiseksi kokonaisluvun ilmoitettu luku ei ole alkuluku
#tarvitaanko uusi lista minkä lukuja tarkastellaan?