
from qtido import *


def principale():
    f = creer(800, 600);
    
    cercle(f, 100, 300, 50)
    couleur(f, 1, 1, 0)
    disque(f, 200, 200, 50)
    couleur(f, 0, 1, 0)
    ligne(f, 400, 200, 450, 250)
    cadre(f, 500, 200, 550, 250)
    rectangle(f, 450, 250, 500, 300)
    exporter_image(f, "salut.png")

    couleur(f, 1,0,0)
    losange(f, 250, 350, 100, 100)
    couleur(f,0,1,1)
    losange(f, 100, 150, 100, 150)
    exporter_image(f, "question-losange.png")
    
    attendre_fermeture(f)


def losange(f, centre_x, centre_y, rayon_h, rayon_v):
    ligne(f, centre_x, centre_y-rayon_v, centre_x-rayon_h, centre_y)
    ligne(f, centre_x, centre_y+rayon_v, centre_x+rayon_h, centre_y)
    ligne(f, centre_x+rayon_h, centre_y, centre_x, centre_y-rayon_v)
    ligne(f, centre_x-rayon_h, centre_y, centre_x, centre_y+rayon_v)
    

principale()

