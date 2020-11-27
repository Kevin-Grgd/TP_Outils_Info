###importation bibliotheque

from qtido import *
import sys
import figures

###définition fonction

def smiley(f,couleur_demande,x,y,rayon):           #fonction dessin smiley
    couleur_smiley(f,couleur_demande)
    disque(f,x,y,rayon)
    couleur(f,0,0,0)
    disque(f,x,y,(int(rayon/15)))
    bouche(f, x, (y+(rayon/3)), rayon)
    oeil(f,(int(x-(rayon/2.7))),(int(y-(rayon/2.5))),rayon)
    oeil(f,(int(x+(rayon/2.7))),(int(y-(rayon/2.5))),rayon)


    
def couleur_smiley(f,couleur_demande):             #fonction defini couleur smiley
    if couleur_demande == "rouge":
        couleur(f,1,0,0)
    elif couleur_demande == "bleu":
        couleur(f,0,0,1)
    elif couleur_demande == "vert":
        couleur(f,0,1,0)
    elif couleur_demande == "cyan":
        couleur(f,0,1,1)
    elif couleur_demande == "magenta":
        couleur(f,1,0,1)
    elif couleur_demande == "jaune":
        couleur(f,1,1,0)


        
def bouche(f,x,y,rayon):                                #fonction dessin bouche
    ligne(f,(x+(rayon/1.5)),y,(x-(rayon/1.5)),y)
    ligne(f,(x+(rayon/1.5)),y,x,(y+(rayon/3)))
    ligne(f,x,(y+(rayon/3)),(x-(rayon/1.5)),y)


    
def oeil(f,x,y,rayon):                                 #fonction dessin oeil
    figures.losange(f,x,y,(int(rayon/4)),(int(rayon/4)))


    
def principale():
    f = creer(800,600)
    couleur = (f,1,1,1)
    rectangle(f,0,0,800,600)
    couleur_demande = sys.argv[1]
    x = 200
    y = 200
    rayon = 100
    sortie = "question-smiley.png"
    
    smiley(f,couleur_demande,x,y,rayon)

    x = 450
    y = 450
    rayon = 75
    couleur_demande = "rouge"
    smiley(f,couleur_demande,x,y,rayon)

    x = 375
    y = 175
    rayon = 35
    couleur_demande = "cyan"
    smiley(f,couleur_demande,x,y,rayon)

    x = 623
    y = 515
    rayon = 62
    couleur_demande = "vert"
    smiley(f,couleur_demande,x,y,rayon)

    exporter_image(f,sortie)
    attendre_fermeture(f)

###programme principale

#principale()
