entree=input("Entrez le mul et la limite : ")
s = 1
nb = entree.split(" ")
mul = int(nb[0])
limite = int(nb[1])
compte = 0

if mul == 1:
    print("Erreur, le programme va boucler à l'infini")
else:
    while s <= limite:
        print(s)
        s = s * mul
        compte = compte + 1
print("Nombre d'itération(s) :",compte)
