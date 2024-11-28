while True:
    try :
        hauteur = int(input("Hauteur du rectangle : "))
        largeur = int(input("Largeur du rectangle : "))
        character = input("Quel caractère souhaitez vous utilisez pour votre dessin : ")

        #check that the numbers are positif
        if hauteur <=0 or largeur<=0 : 
            print ("Entrez un nombre positif")
            continue

        #good data enter
        for i in range(hauteur) :
            for j in range (largeur) :
                print(character, end = "")
            print()

        reponse = input("Voulez vous dessinez un autre rectangle : ").lower()
        if reponse != "oui" :
            print ("Merci d'avoir essayer")  
            break
        
    except ValueError :
        print("Entrez des entiers")
