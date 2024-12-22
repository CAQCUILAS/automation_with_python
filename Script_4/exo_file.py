with open("fichier_txt/exo_fichier.txt", "r") as fichier:
    contenu = fichier.read()
    mot = contenu.split()
    print("Votre document compte",len(mot))
