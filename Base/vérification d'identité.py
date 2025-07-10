# Nous allons faire un scrip qui d'authentification pour Admin dont le mdp sera toto123

User = input("Saisissez le nom d'utilisateur ")
MDP = input("Saissiez le MDP ")

if User == "Admin" and MDP == "toto123" :
    print("Connexion reussi bievenue")
else:
    print("Nom d'utilisateur ou mdp incorect")
 