try:
    largeur = int(input("Entrez la largeur du triangle inversé : "))
    if largeur <= 0:
        print("⚠ Veuillez entrer un nombre positif.")
    else:
        for i in range(largeur, 0, -1):  # Partir de 'largeur' et aller jusqu'à 1
            for j in range(i):  # Afficher 'i' étoiles à chaque ligne
                print("*", end="")
            print()  # Passer à la ligne suivante après chaque rangée

except ValueError:
    print("❌ Veuillez entrer un entier naturel.")
