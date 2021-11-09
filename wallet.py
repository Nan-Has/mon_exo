

# place de cinema
age = int(input("Quel est votre age ? "))
if age < 18:
    prix_a_payer = 7
else:
    prix_a_payer = 12
pop_corn = input("Souhaitez vous du Pop corn ? " )
if pop_corn == "oui":
    prix_a_payer += 5
print("Vous devez payer {} £".format(prix_a_payer))