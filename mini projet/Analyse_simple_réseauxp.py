# ---------------------------------------------------
# Mini projet : Vérification d'adresses IP
# Auteur : Djamal Mohamed Massoundi
# ---------------------------------------------------

# Import du module pour vérifier les IP
import ipaddress

# Création d'une liste vide pour stocker les IP valides
ip_valides = []

print("=== Vérificateur d'adresses IP ===")
print("Saisis 'fin' pour arrêter la saisie.\n")

while True:
    ip = input("Entrez une adresse IP : ")

    if ip.lower() == "fin":
        break  # On arrête la boucle

    try:
        # Vérifie si l'adresse IP est valide
        ipaddress.ip_address(ip)
        print(f"✅ {ip} est une adresse IP valide.")
        ip_valides.append(ip)
    except ValueError:
        print(f"❌ {ip} n'est pas une adresse IP valide.")

# Enregistrement dans un fichier texte
with open("ips_valides.txt", "w") as f:
    for ip in ip_valides:
        f.write(ip + "\n")

print("\n📁 Les adresses valides ont été enregistrées dans 'ips_valides.txt'")
