#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
silmukassa = False
lukuStr = input ("Anna luku: ")
if lukuStr != "":
    lukuInt = int(lukuStr)
    pienin = lukuInt
    suurin = lukuInt
    silmukassa = True
while lukuStr!="":
    if lukuInt > suurin:
        suurin = lukuInt
    if lukuInt < pienin:
        pienin = lukuInt
    lukuStr = input ("Anna luku: ")
    if lukuStr != "":
        lukuInt = int(lukuStr)
if silmukassa == True:
    print("Suurin luku: " + str(suurin))
    print("Pienin luku: " + str(pienin))
else:
    print("lopetit ennen lukuja")