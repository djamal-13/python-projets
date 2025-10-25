# Demander le MDP
print("Votre MDP doit contenir au moins 8 caractères, dont un chiffre et une majuscule.")
mdp = input("Saisissez un nouveau mot de passe : ")

# Vérification
if len(mdp) < 8:
    print("Mot de passe trop court ❌")
elif not any(caractere.isdigit() for caractere in mdp):
    print("Mot de passe sans chiffre ❌")
elif not any(caractere.isupper() for caractere in mdp):
    print("Mot de passe sans majuscule ❌")
else:
    print("Mot de passe valide ✅")
