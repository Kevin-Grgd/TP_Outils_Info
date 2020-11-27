###importation bibliothèque

from qtido import *
import sys

###définition fonction

def spirale():
    f = creer(800,600)
    tortue = creer_tortue(f)
    x = 50
    n = sys.argv[1]
    sortie = sys.argv[2]

    for i in range(int(n)):
        tortue_trace(tortue)
        tortue_avance(tortue,x)
        x = x + 5
        tortue_stop(tortue)
        tortue_gauche(tortue,90)

    exporter_image(f, sortie)
    attendre_fermeture(f)

###programme principal

spirale()
