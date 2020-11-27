###import bibliothèques

from qtido import *
import sys
import smiley

###definitions foncitons

def magic_smiley():
    f = creer(800,600)
    largeur = int(sys.argv[1])
    longueur = int(sys.argv[2])
    sortie = sys.argv[3]
    x = 30
    y = 30

    for i in range(longueur):
        for j in range(largeur):
            if (i+j) % 2 == 0:
                couleur(f,0,1,1)
                smiley.smiley(f,couleur,x,y,25)
                
            else :
                couleur(f,0,1,0)
                smiley.smiley(f,couleur,x,y,15)
            y = y + 50
        x = x + 50
        y = 30
                
    exporter_image(f,sortie)
    attendre_fermeture(f)


###programme principal

magic_smiley()
