#Définition des fonctions :

def produit(a,b):
    print("Appel de la fonction produit")
    print(a*b)
    return a*b

def somme(a,b):
    print("Appel de la fonction somme")
    print(a+b)
    return a+b

def calculer(commande):
    decoupe = commande.split(" ")
    var1 = float(decoupe[1])
    var2 = float(decoupe[2])
    if decoupe[0] == "produit":
        print("Multiplication")
        produit(var1,var2)
    elif decoupe[0] == "somme":
        print("Addition")
        somme(var1,var2)
    else:
        print("Erreur, le programme",decoupe[0],"n'existe pas.")


#Programme principal :

entree = input("Entrez le programme et les valeurs à calculer : ")
calculer(entree)
