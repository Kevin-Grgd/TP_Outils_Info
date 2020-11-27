# 1) imports
import math

# 2) définitions de fonctions

def au_carre(liste):
    liste_fin=[]
    for i in (liste):
        liste_fin.append(i**2)
    return liste_fin


def au_cube(liste):
    liste_fin=[]
    for i in (liste):
        liste_fin.append(i*i*i)
    return liste_fin

def au_logbase(base, liste):
    liste_fin = []
    for i in liste:
        liste_fin.append((float(lg(i)))/(float(lg(base))))
       #print(liste_fin)
    return liste_fin


def somme(liste):
    somme = sum(liste)
    #print(somme)
    return somme


def produit(liste):
    acc = 1
    for i in range(0,len(liste)):
        acc = acc * liste[i]
    #print(acc)
    return acc


def somme_2d(liste):
    acc = 0
    resultat = 0
    for i in liste:
        for j in i:
            acc = acc + j
    resultat = resultat + acc
    #print(resultat)
    return(resultat)


def produit_2d(liste):
    acc = 1
    for i in liste:
        for j in i:
            acc = acc * j
    return acc
    

### NE PAS MODIFIER CES FONCTIONS ###
def verifie_presque_egal_liste(a, b):
    if len(a) != len(b):
        raise ValueError("ERREUR len(...) : «"+str(a)+"» != «"+str(b)+"»")
    for i in range(len(a)):
        verifie_presque_egal(a[i], b[i])
def verifie_presque_egal(a, b):
    if round(a, 5) != round(b, 5):
        raise ValueError("ERREUR : «"+str(a)+"» != «"+str(b)+"»")
######################################


    
# 3 et 4) programme principal

### Dé-commenter les tests suivants, petit à petit
### au fur et à mesure que vous écrivez les fonctions

l1 = [1, 10, 20]
verifie_presque_egal_liste( au_carre(l1), [1, 100, 400])
verifie_presque_egal_liste(  au_cube(l1), [1, 1000, 8000])
lg = math.log
verifie_presque_egal_liste( au_logbase(2, l1), [lg(1)/lg(2), lg(10)/lg(2), lg(20)/lg(2)])
verifie_presque_egal( produit(l1), 200)
verifie_presque_egal( somme(l1), 31)
l2 = [ [1, 2, 3], [10, 20, 30] ]
verifie_presque_egal( somme_2d(l2), 66)
verifie_presque_egal( produit_2d(l2), 36000)

### Ajouter vos propres tests ci-dessous

x = [1,2,3,4,5,6,7,8,9]
y = [[1,2,3,4,5], [6,7,8,9,10]]
au_carre(x)
au_cube(x)
somme(x)
produit(x)
au_logbase(2, x)
somme_2d(y)
produit_2d(y)


