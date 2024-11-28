try :
   hauteur = int(input("Hauteur de votre triangle"))
   largeur = int(input("Largeur de votre rectangle"))
   for i in range (hauteur) :
        for j in range (largeur) :
            print("*", end="")   
        print() 

except ValueError :
    print("Entrer des entiers naturels")