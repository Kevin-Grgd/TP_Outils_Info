###import bibliothèque

from qtido import *
import sys

###définition fonction

def magic_4():
    f = creer(800,600)
    n = int(sys.argv[1])
    sortie = sys.argv[2]
    x = (20*n)
    
    for i in range(n,0,-1):
        if i % 2 == 0:
            couleur(f,1,0,0)
        else : 
            couleur(f,0,1,0)
        disque(f,400,300,x)
        x = x - 20

    exporter_image(f, sortie)
    attendre_fermeture(f)

###programme principal

magic_4()
