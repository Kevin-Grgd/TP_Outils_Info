entree=input("Entrez le plus et la limite : ")
s = 0
nb = entree.split(" ")
plus = int(nb[0])
limite = int(nb[1])

while s <= limite:
    print(s)
    s = s + plus
