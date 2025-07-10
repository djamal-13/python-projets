#Calcul de la moyenne
note_1 = int(input("Saissez votre 1re note "))
note_2 = int(input("Saissez votre 2eme note "))
note_3 = int(input("Saissez votre 3eme note "))

Moyenne = (note_1 + note_2 + note_3) /3
if Moyenne >= 10 :
    print("Vous êtes admis ")
else :
    print("Vous êtes recaler ") 