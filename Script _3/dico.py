contacts = {}

# Function to add a contact
def add_contact(name, tel, email):
    contacts[name] = {"téléphones": tel, "emails": email}

# Function to modify a contact
def modify_contact(name, key, new_value):
    if name in contacts:
        if key in contacts[name]:
            contacts[name][key] = new_value
            print(f"{key.capitalize()} de {name} a été modifié avec succès.")
        else:
            print(f"Clé '{key}' introuvable.")
    else:
        print(f"Le contact '{name}' n'existe pas.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Le contact '{name}' a été supprimé avec succès.")
    else:
        print(f"Le contact '{name}' n'existe pas.")

# Main program loop
while True:
    try:
        print("\n=== Menu ===")
        print("1. Ajouter un contact")
        print("2. Modifier un contact")
        print("3. Supprimer un contact")
        print("4. Afficher tous les contacts")
        print("5. Quitter")

        choice = int(input("Votre choix : "))

        if choice == 1:
            name = input("Nom : ")
            tel = input("Téléphone : ")
            email = input("Email : ")
            add_contact(name, tel, email)

        elif choice == 2:
            name = input("Nom du contact à modifier : ")
            print("Voulez-vous modifier le 'téléphones' ou 'emails' ?")
            key = input("Votre choix : ").lower()
            new_value = input("Nouvelle valeur : ")
            modify_contact(name, key, new_value)

        elif choice == 3:
            name = input("Nom du contact à supprimer : ")
            delete_contact(name)

        elif choice == 4:
            if not contacts:
                print("\nAucun contact enregistré.")
            else:
                print("\n=== Liste des contacts ===")
                for name, details in contacts.items():
                    print(f"{name} -> Téléphone : {details['téléphones']}, Email : {details['emails']}")

        elif choice == 5:
            print("Merci d'avoir utilisé le gestionnaire de contacts.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

    except ValueError:
        print("Veuillez entrer un nombre valide.")
