try :
    def total_cmd_restau(prix1, prix2,prix3, pourboire = 0.1) :
        somme_repas = prix1+prix2+prix3
        frais_pourboire = somme_repas*pourboire
        somme_cmd = somme_repas+frais_pourboire
        return somme_cmd

    print("Entrez le montant des repas : ")
    prix_repas1 = int(input())
    prix_repas2 = int(input())
    prix_repas3 = int(input())

    print("Le total des vos dépenses fait : ",total_cmd_restau(prix_repas1,prix_repas2,prix_repas3))

except ValueError : 
        print("Veuillez entrer un montant valide")

