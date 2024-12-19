# Entrée utilisateur
phrase = input("Entrez une phrase : ")

# Diviser la phrase en mots et les mettre en minuscules
mots = phrase.lower().split()

# Dictionnaire pour stocker les statistiques des mots
dico_mots = {}

# Parcourir les mots
for mot in mots:
    # Si le mot est déjà dans le dictionnaire, augmenter son compteur
    if mot in dico_mots:
        dico_mots[mot] += 1
    else:
        # Si le mot n'est pas dans le dictionnaire, l'ajouter avec une occurrence de 1
        dico_mots[mot] = 1

# Afficher les statistiques des mots
print("Statistiques des mots :")
for mot, count in dico_mots.items():
    print(f"{mot}: {count}")
