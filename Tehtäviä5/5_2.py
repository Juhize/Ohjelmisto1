#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
#suuruusjärjestyksessä suurimmasta alkaen. 
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
#argumentiksi reverse=True.

silmukassa = False
luku = input ("Anna luku: ")
#Luku pitää määritellä, että sitä voi käyttää while ehdossa ja myöhemmin
if luku != "":
    silmukassa = True
    #Luotiin rakenne, mikä kirjoittaa lopetit ennen lukuja, jos käyttäjä jättää ensimmäisen luvun tyhjäksi
luvut = []
#Määriteltiin luvut listaksi
while luku!="":
    #Looppi kestää, kunnes käyttäjä syöttää tyhjän syötteen
    if luku != "":
        luvut.append(luku)
        luku = input ("Anna luku: ")
    #Jos syöte on muuta kun tyhjä, se lisätään listaan luvut, tällä loopin järjestyksellä myös ensimmäinen luku tulee syötettyä listaan
if silmukassa == True:
    luvut.sort (reverse=True)
    #Tällä rakenteella saadaan luvut järjesteltyä suurimmasta pienimpään
    print("Viisi suurinta: " + str(luvut[:5]))
    #Pyydetään ohjelmaa kirjoittamaan 5 suurinta lukua str-muodossa (ei toimi pelkillä luvuilla)
else:
    print("Lopetit antamatta lukuja")