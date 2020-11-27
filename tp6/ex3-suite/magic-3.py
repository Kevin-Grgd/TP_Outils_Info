###import bibliothèque

from qtido import *
import sys

###définition fonction

def magic_3():
    f = creer(800,600)
    n = int(sys.argv[1])
    sortie = sys.argv[2]
    x = 20
    
    for i in range(n):
        if i % 2 == 0:
            couleur(f,0,1,0)
        else : 
            couleur(f,1,0,0)
        cercle(f,400,300,x)
        x = x + 20

    exporter_image(f, sortie)
    attendre_fermeture(f)

###programme principal

magic_3()
