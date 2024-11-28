try:
    hauteur = int(input("Entrez la hauteur de l'escalier : "))
    if hauteur <= 0:
        print("⚠ Veuillez entrer un entier positif.")
    else:
        for i in range(hauteur):
            # Ajouter des espaces pour le décalage
            for j in range(i):
                print(" ", end="")
            # Ajouter les étoiles pour chaque rangée
            print("*")

except ValueError:
    print("❌ Veuillez entrer un entier naturel.")
