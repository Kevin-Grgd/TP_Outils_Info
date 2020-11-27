###import bibliothèque

from qtido import *
import sys

###définition fonction

def losange(f, centre_x, centre_y, rayon_h, rayon_v):
    ligne(f, centre_x, centre_y-rayon_v, centre_x-rayon_h, centre_y)
    ligne(f, centre_x, centre_y+rayon_v, centre_x+rayon_h, centre_y)
    ligne(f, centre_x+rayon_h, centre_y, centre_x, centre_y-rayon_v)
    ligne(f, centre_x-rayon_h, centre_y, centre_x, centre_y+rayon_v)

def magic_2():
    f = creer(800,600)
    n = int(sys.argv[1])
    sortie = sys.argv[2]
    x = 20
    y = 40
    couleur(f,1,1,1)

    if n % 2 == 0:
        for i in range(int(n/2)):
            cercle(f,400,300,x)
            losange(f,400,300,y,x)
            x = x + 40
            y = y + 50
    else:
        for i in range(int(n/2)):
            cercle(f,400,300,x)
            losange(f,400,300,y,x)
            x = x + 40
            y = y + 50

        cercle(f,400,300,x)

    exporter_image(f, sortie)
    attendre_fermeture(f)

###programme principal

magic_2()
