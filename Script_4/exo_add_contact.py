def add_contact(nom, telephone, email):
    with open("fichier_txt/mes_contacts.txt", "a") as fichier:
        fichier.write(f"\nNom : {nom}, Téléphone : {telephone}, E-mail : {email}")

try:
    while True:
        print("Tapez 1 pour enregistrer un contact \n Tapez 2 pour afficher la liste des contacts \n Tapez 0 pour quitter le programme")
        choix = int(input())
        if choix == 1:
            name = input("Nom du contact : ")
            contact = input("Téléphone de la personne : ")
            mail = input("Email : ")
            add_contact(name, contact, mail)
        elif choix == 2 :

            print("******Liste des contacts ********")
            with open("fichier_txt/mes_contacts.txt", "r") as fichier:
                contenu = fichier.read()
                print(contenu)
        else:
            break
except ValueError:
    print("Entrez des valeurs valides")
