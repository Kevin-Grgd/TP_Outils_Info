#Définitions des fonctions :

def produit (a,b):
        print("Appel de la fonction produit")
        print(a*b)
        return a*b
	
def somme (a,b):
        print("Appel de la fonction somme")
        print(a+b)
        return a+b

#Programme principal :

print("Programme principal")
var1 = 10
var2 = 1.5
produit(var1,var2)
somme(var1,var2)

var3 = 20
var4 = 42
produit(var3,var4)
somme(var3,var4)
