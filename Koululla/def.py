käyttäjä = input("Kuka: ")
kerrat = int(input("Monta: "))
def tervehdi (käyttäjä):
    for i in range (kerrat):
        print("moi! " + käyttäjä +" "+str(i+1) + ". kerran.")
    return
tervehdi(käyttäjä)