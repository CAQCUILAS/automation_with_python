"""
def moyenne(notes):
    moy = sum(notes) / len(notes)
    return moy

try:
    print("Entrez vos notes séparées par un espace")
    notes = list(map(int, input().split()))
    resultat = moyenne(notes)
    print("La moyenne est :", resultat)
except ValueError:
    print("Veuillez entrer des valeurs valides")
"""


def moyenne(*notes):
    moy = sum(notes) / len(notes)
    return moy

try:
    print("Entrez vos notes séparées par un espace")
    notes = list(map(int, input().split()))
    resultat = moyenne(*notes)
    print("La moyenne est :", resultat)
except ValueError:
    print("Veuillez entrer des valeurs valides")

