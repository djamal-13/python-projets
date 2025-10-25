# Demande des informations à l'utilisateur
article = input("Nom de l'article : ")
prix = float(input("Prix unitaire (€) : "))
quantite = int(input("Quantité achetée : "))

# Calcul du total
total = prix * quantite

# Affichage du résultat
print("Vous avez acheté", quantite, article + "(s) pour un total de", total, "€")
