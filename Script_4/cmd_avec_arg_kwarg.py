def total_cmd_restau(*prix, pourboire=0.1, **kwargs):
    somme_repas = sum(prix)
    frais_pourboire = somme_repas * pourboire
    reduction = kwargs.get('reduction', 0)
    frais_fixes = kwargs.get('frais_fixes', 0)
    somme_cmd = somme_repas + frais_pourboire - reduction + frais_fixes
    return somme_cmd


try:
    print("Entrez les montants des repas, séparés par des espaces : ")
    prix_repas = list(map(float, input().split()))  # Saisir plusieurs montants
    print("Souhaitez-vous ajouter une réduction ou des frais fixes ?")
    reduction = float(input("Réduction (laisser vide pour 0) : ") or 0)
    frais_fixes = float(input("Frais fixes (laisser vide pour 0) : ") or 0)
    print(
        "Le total de vos dépenses fait :",
        total_cmd_restau(*prix_repas, pourboire=0.1, reduction=reduction, frais_fixes=frais_fixes),
    )
except ValueError:
    print("Veuillez entrer des montants valides.")
