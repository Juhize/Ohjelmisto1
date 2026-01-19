#kysytään käyttäjältä ikä ja rahamäärä
ikä = int(input("Anna ikäsi:"))
rahat = float(input("paljonko on rahaa mukana? "))

#jos käyttäjä on täysi-ikäinen ja rahaakin riittää
#vähintään 10€, niin pääsee bileisiin
#tai jos rahaa on enemmän kuin 1000€ alaikäinenkin pääsee
if ikä >= 18 and rahat >= 10 or rahat >=1000:
     print("Tervetuloa bileisiin!")
     vip = str(input("Onko Vip lippua: "))
     if vip==str("kyllä"):
          print("Tervetuloa vip loungeen")
     else:
          print("Mene jonoon!")
else:
     print("Et pääse bileisiin")
#a or b and c
#a or (b and c):
#lauseke on tosi kun
#a on tosi tai b ja c on tosi