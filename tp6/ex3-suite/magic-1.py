###importation bibliothèque

from qtido import *
import sys

###définition fonction

def spirale():
    f = creer(800,600)
    n = sys.argv[1]
    sortie = sys.argv[2]
    x = 25

    for i in range(int(n)):
        couleur(f,1,1,1)
        cercle(f,(800/2),(600/2),x)
        x = x + 20

    exporter_image(f, sortie)
    attendre_fermeture(f)

###programme principal

spirale()
