
while True :
    try :
        a = int(input("Veuiilez entrer un nombre entier : "))
        b = int(input("veuillez entrer un nombre entier : "))

        def soustraction (c,d):
            return c-d
        resultat = soustraction(a,b)
        print("Le résultat est",resultat )

        
        if resultat < 0 :
            print("Veuillez Entrer le nombre le plus grand en premier")
            continue
        
    except ValueError :
        print("Veuillez entrer des eniters positifs")
        continue
    break