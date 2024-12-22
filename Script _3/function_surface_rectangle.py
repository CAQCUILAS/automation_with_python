try :
    longueur = int(input("Entrez la longueur du rectangle : "))
    largeur = int(input("Entrez la largeur du rectangle : "))

    def surface_rectangle(longueur = 5, largeur = 10) :
        return longueur*largeur
    
    surface = surface_rectangle(longueur, largeur)
    print("L'aire de la surface de votre rectangle est",surface)

except ValueError :
    print ("Entrez des entiers naturels")