# 1) imports
import math

# 2) définitions de fonctions

def input_liste_nombres():
    entrees = input_liste("Nombres (séparés par des espaces) : ", " ")
    valeurs = en_float(entrees)
    return valeurs


def input_liste(x,y):
    entre=input(x)
    liste=entre.split(y)
    return liste

def en_float(x):
    liste=[]
    for i in x:
        liste.append(float(i))
    return liste

def au_carre(x):
    liste=[]
    for i in x:
        liste.append(i**2)
    return liste

def afficher_liste_multiligne(x):
    for i in range(len(x)):
        print(i+1, "-", x[i])
    print("Total :",sum(x))

    
def principal():
    nbrs = input_liste_nombres()
    carres = au_carre(nbrs)
    afficher_liste_multiligne(carres)
    
# 3 et 4) programme principal
#nbrs = input_liste_nombres()
#carres = au_carre(nbrs)
#afficher_liste_multiligne(carres)
principal()
