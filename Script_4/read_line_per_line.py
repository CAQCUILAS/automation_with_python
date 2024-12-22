with open("fichier_txt/mon_fichier.txt", "r") as fichier:
    for ligne in fichier:
        print(ligne.strip())  # `strip()` supprime les espaces ou sauts de ligne.
