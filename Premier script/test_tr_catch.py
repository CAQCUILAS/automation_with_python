while True :
    try:
        #ask user to enter numbers
        print("entrez des nombres entiers")
        a=int(input("nombre 1 : "))
        b=int(input("nombre 2 : "))
        #make sum of two numbers
        somme=a+b
        print("La somme des deux valeurs est",somme)
        #condition when sum is big 20
        if somme>20:
            print("Votre somme est supérieur à 20, essayez avec d'autres valeurs")
            #Restart the boucle
            continue
    except ValueError : 
        print("veuillez entrez des nombres entiers ")
        #restat
        continue
    # Demander si l'utilisateur veut recommencer
    reponse = input("Voulez-vous essayer encore ? (oui/non) : ").lower()
    if reponse != "oui":
        print("Merci d'avoir utilisé ce programme !")
        break  # Sortir de la boucle principale
    else :
        continue
    
    


