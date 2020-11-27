from math import *
a = int(input("Entrer a : "))
b = int(input("Entrer b : "))
c = int(input("Entrer c : "))


#Calcul delta
delta = (b*b) - (4 * a * c)
print("Delta =",delta)


#Si Delta < 0
if delta<0:
    print("Pas de solutions possibles dans les réels")

    
#Si Delta = 0
elif delta == 0:
    print("Une seule solution :", (-b)/(2*a))

    
#Si Delta > 0
elif delta>0:
    
    r1 = (-b + sqrt(delta))/(2*a)
    r2 = (-b - sqrt(delta))/(2*a)
    print("r1 =",r1)
    print("r2 =",r2)
