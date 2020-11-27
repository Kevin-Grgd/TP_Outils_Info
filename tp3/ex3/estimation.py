from random import *

#Définition variable
entree=input("Entrez r et n (séparés par des espaces) : ")
nr = entree.split(" ")
r = float(nr[0])     #float?
n = int(nr[1])
m = 0
                                                                                                              #Affichage Tirage point
for i in range(0,n):
    print("Tirage d'un point.")
    x = uniform(-r, r)                                                                                        #Valeur aléatoire x et y
    y = uniform(-r, r)
#    print("x =",x)
#    print("y =",y)
    if ((x*x + y*y)**0.5) <= r and ((x*x + y*y)**0.5) >= -r:                                                   #Vérification point dans le cercle
        print("Le point de coordonnées " ,x,",",y, " est dans le cercle de rayon " ,r, sep ="")
        m = m + 1 
    else:
        print("Le point de coordonnées " ,x,",",y, " n'est pas dans le cercle de rayon " ,r, sep ="")

print("Estimation de pi :",4*(m/n))
