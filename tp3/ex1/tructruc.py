entree = input("Entrez le nombre de début, le nombre de fin et le pas ")
nombre=entree.split(" ")
nb_debut = int(nombre[0])
nb_fin = int(nombre[1])
pas = int(nombre[2])

for entier in range(nb_debut, (nb_fin-1), pas):
    print(entier)
