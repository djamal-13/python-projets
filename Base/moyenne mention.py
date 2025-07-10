#Calcul de la moyenne
note_1 = float(input("Saissez votre 1re note "))
note_2 = float(input("Saissez votre 2eme note "))
note_3 = float(input("Saissez votre 3eme note "))

Moyenne = (note_1 + note_2 + note_3) /3
if Moyenne >= 16 :
    print("Mention très bien ")
elif Moyenne >= 14 :
    print("Mention bien ") 
elif Moyenne >= 12 :
    print("Mention assez bien ") 
elif Moyenne >= 10 :
    print("Admis ")
else :
    print("Non admis") 
