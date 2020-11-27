from random import *
from qtido import *

def dessin_cercle_rouge():
    couleur(f,1,0,0)
    disque(f, 300+x, 300+y, 0.5)

def dessin_cercle_vert():
    couleur(f,0,1,0)
    disque(f, 300+x, 300+y, 0.5)

    
#Définition variable
entree=input("Entrez r et n (séparés par des espaces) : ")
nr = entree.split(" ")

f = creer(600,600)

if len(nr) == 1:                                                                                             #Test si une valeur entrée
    n = int(nr[0])
    r = 300
else:
    r = float(nr[0])  #float ou int?
    n = int(nr[1])

m = 0
iteration=0
#Affichage Tirage point
for i in range(0,n):
   # print("Tirage d'un point.")
    x = uniform(-r, r)                                                                                        #Valeur aléatoire x et y
    y = uniform(-r, r)
#    print("x =",x)
#    print("y =",y)
    if ((x*x + y*y)**0.5) <= r and ((x*x + y*y)**0.5) >= -r:                                                   #Vérification point dans le cercle
       # print("Le point de coordonnées " ,x,",",y, " est dans le cercle de rayon " ,r, sep ="")
        m = m + 1
        dessin_cercle_vert()

    else:
       # print("Le point de coordonnées " ,x,",",y, " n'est pas dans le cercle de rayon " ,r, sep ="")
        dessin_cercle_rouge()

    iteration = iteration + 1
    if iteration % 1000 == 0:
        re_afficher(f)
        print("Estimation de pi :",4*(m/n))
            
re_afficher(f)
print("Nombre de points tiré :",n)
print("Estimation de pi :",4*(m/n))

attendre_fermeture(f)
