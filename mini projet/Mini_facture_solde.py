# --- Mini facture avec réduction ---

# Demande des informations
article = input("Nom de l'article : ").strip()
prix = float(input("Prix unitaire (€) : "))
quantite = int(input("Quantité achetée : "))

# Calcul du total brut
total = prix * quantite

# Application de la réduction
if total > 100:
    reduction = total * 0.10   # 10% de réduction
    total_final = total - reduction
    print(f"✅ Vous bénéficiez d'une réduction de 10% soit {reduction:.2f} €")
else:
    total_final = total
    print("Aucune réduction appliquée.")

# Affichage du résultat final
print(f"💰 Total à payer pour {quantite} {article}(s) : {total_final:.2f} €")
