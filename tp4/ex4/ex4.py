# 1) imports
from math import *


# 2) définitions de fonctions

def carre(x):
        carre= x**2
        #print(carre)
        return carre

def cube(x):
        cube = x * x * x
        #print(cube)
        return cube

def logbase(v,b):
        logbase = (log10(v)/log10(b))
        #print(logbase)
        return logbase
	
def aire_disque(r):
        aire = pi * (r ** 2)
        #print(aire)
        return aire
	
def volume_cylindre(r,h):
        volume = aire_disque(r) * h
        #print(volume)
        return volume



### NE PAS MODIFIER CETTE FONCTION ###
def verifie_presque_egal(a, b):
    if round(a, 5) != round(b, 5):
        raise ValueError("ERREUR : «"+str(a)+"» != «"+str(b)+"»")
######################################


    
# 3 et 4) programme principal

z = aire_disque(42.42)
resultat = cube(logbase(z,volume_cylindre(10,2)))
print("Le résultat est :",resultat)

### Dé-commenter les tests suivants, petit à petit
### au fur et à mesure que vous écrivez les fonctions

#verifie_presque_egal( carre(8), 64)
#verifie_presque_egal( carre(-10), 100)
#verifie_presque_egal( cube(10), 1000)
#verifie_presque_egal( cube(-0.1), -0.001)
#verifie_presque_egal( logbase(1024, 2), 10)
#verifie_presque_egal( logbase(1024, 1024), 1)
#verifie_presque_egal( aire_disque(2.5), 19.634954084936208)
#verifie_presque_egal( volume_cylindre(2.5, 100), 1963.4954084936208)


### Ajouter vos propres tests ci-dessous

#carre(4)
#cube(3)
#cube(4)
#logbase(1024,2)
#aire_disque(6)
#volume_cylindre(9, 59)
