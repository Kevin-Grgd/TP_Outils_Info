a = int(input("Entrer un nombre entier : "))
print("a =",a)
b = int(input("Entrer un second nombre entier : "))
print("b =",b)
c = int(input("Entrer un troisième nombre entier : "))
print("c =",c)

#Recherche minimum

if a<b and a<c:
    print("Minimum :",a)
    print("La somme des deux plus grands entiers est :",b+c)
elif b<c:
    print("Minimum :",b)
    print("La somme des deux plus grands entiers est :",a+c)
else:
    print("Minimum ",c)
    print("La somme des deux plus grands entiers est :",a+b)
