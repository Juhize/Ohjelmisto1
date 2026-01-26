#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
#suuruusjärjestyksessä suurimmasta alkaen. 
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
#argumentiksi reverse=True.

silmukassa = False
lukuStr = input ("Anna luku: ")
if lukuStr != "":
    lukuInt = int(lukuStr)
    silmukassa = True
luvut = []
while lukuStr!="":
    lukuStr = input ("Anna luku: ")
    if lukuStr != "":
        lukuInt = int(lukuStr)
    luvut.append(lukuInt)
if silmukassa == True:
    luvut.sort (reverse=True)
    print("Viisi suurinta: " + str(luvut[:5]))
else:
    print("Lopetit ennen lukuja")