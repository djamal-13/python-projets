# detecteur_password.py

# On demande à l'utilisateur d'entrer un mot de passe
mot_de_passe = input("Entrez votre mot de passe : ")

# On vérifie si le mot de passe est trop court
if len(mot_de_passe) < 8:
    print("Mot de passe trop court !")

# On vérifie s'il manque un chiffre
elif not any(caractere.isdigit() for caractere in mot_de_passe):
    print("Mot de passe doit contenir au moins un chiffre !")

# On vérifie s'il manque une majuscule
elif not any(caractere.isupper() for caractere in mot_de_passe):
    print("Mot de passe doit contenir une majuscule !")

# Si toutes les conditions sont remplies
else:
    print("Mot de passe sécurisé ✅")
