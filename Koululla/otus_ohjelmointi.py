class Kissa:
    tehty = 0
    def __init__(self, nimi, rotu="kotikissa"):
        self.nimi = nimi
        self.rotu = rotu
        Kissa.tehty = Kissa.tehty +1

kissa1 = Kissa("Ensimmäinen", "Ragdol")
kissa2 = Kissa("Naksu")
kissa3 = Kissa("Kolmas", "Siaamilainen")

print(f"{kissa1.nimi} on {kissa1.rotu}")
print(f"{kissa2.nimi} on {kissa2.rotu}")
print(f"{kissa3.nimi} on {kissa3.rotu}")
print(f"\nKissoja on nyt tehty {Kissa.tehty}.")
if Kissa.tehty > 2:
    print("Tarvitset nyt useamman hiekkalaation.")
