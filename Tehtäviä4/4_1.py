#Kirjoita while-toistorakennetta käyttävä ohjelma, 
#joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

luku = 0
while luku <= 1000:
    print(f"{luku:d}")
    luku = luku + 3
print("kolmella jaollise 1-1000")