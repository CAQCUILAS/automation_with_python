n=1
x= int(input("Entrer la hauteur du triangle : "))
for i in range(x):
    for j in range(n):
        print("*", end="")
    print()
    n += 1
    #print(n)