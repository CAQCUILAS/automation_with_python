# Liste initiale pour les courses
course = []

# Fonction pour ajouter des commandes
def add_commande(x, y, z):
    course.append(x)
    course.append(y)
    course.append(z)

# Fonction pour supprimer des commandes
def delete_commande(x, y, z):
    # Vérifier si chaque élément est dans la liste avant de le supprimer
    if x in course:
        course.remove(x)
    if y in course:
        course.remove(y)
    if z in course:
        course.remove(z)

# Boucle principale
while True:
    print("\nQue voulez-vous faire ?")
    print("1. Ajouter des commandes")
    print("2. Supprimer des commandes")
    print("3. Voir la liste actuelle")
    print("4. Quitter le programme")
    
    try:
        choice = int(input("Votre choix : "))

        if choice == 1:
            # Ajouter des commandes
            x = input("Course 1 : ")
            y = input("Course 2 : ")
            z = input("Course 3 : ")
            add_commande(x, y, z)
            print("\nCommandes ajoutées avec succès.")
        
        elif choice == 2:
            # Supprimer des commandes
            x = input("Course 1 à supprimer : ")
            y = input("Course 2 à supprimer : ")
            z = input("Course 3 à supprimer : ")
            delete_commande(x, y, z)
            print("\nCommandes supprimées (si elles existaient).")
        
        elif choice == 3:
            # Afficher la liste des courses
            if course:
                print("\nVoici la liste actuelle de vos courses :")
                for i in course:
                    print(i, end=", ")
                print()
            else:
                print("\nVotre liste de courses est vide.")
        
        elif choice == 4:
            # Quitter le programme
            print("\nMerci d'avoir utilisé le programme !")
            break
        
        else:
            print("\nVeuillez entrer un choix valide (1, 2, 3, ou 4).")
    
    except ValueError:
        print("\nErreur : Veuillez entrer un nombre valide.")
