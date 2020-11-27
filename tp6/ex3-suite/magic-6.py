###import bibliothèque

from qtido import *
import sys

###définition fonction

def carre(f,x,y):
    rectangle(f,x,y,(x+15),(y+15))

    
def magic_6():
    f = creer(800,600)
    largeur = int(sys.argv[1])
    longueur = int(sys.argv[2])
    sortie = sys.argv[3]
    x = 30
    y = 30


    for i in range(longueur):
        for j in range(largeur):
            if (i+j) % 2 == 0:
                couleur(f,0,0,1)
            else:
                couleur(f,0,1,0)
            carre(f,x,y)
            y = y + 18
        x = x + 18
        y = 30


    exporter_image(f, sortie)
    attendre_fermeture(f)

###programme principal

magic_6()
