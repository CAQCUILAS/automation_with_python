try:
    hauteur = int(input("Quelle est la hauteur du triangle ? "))
    if hauteur <= 0:
        print("⚠ La hauteur doit être un entier positif.")
    else:
        n = 1
        for i in range(hauteur):
            for j in range(n):
                print("*", end="")
            print()
            n += 1
except ValueError:
    print("❌ Veuillez entrer un entier naturel.")
