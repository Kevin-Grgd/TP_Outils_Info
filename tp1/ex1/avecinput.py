p = int(input("Combien vaut p ? "))
q = int(input("Combien vaut q ? "))
s = p+q

#Calcul Somme
print("p vaut",p, "q vaut",q, ",leur somme vaut", s)

#Calcul Modulo
if p % q == 0:
    print("Multiple")
else :
    print("Pas multiple")

#Variable temporaire
tmp = p
p = q
q = tmp
s = p+q
print("p vaut",p ,", q vaut",q ," et leur somme vaut ", s,)


#Challenge Optionnel
print("p =",p)
print("q =",q)
p=p+q
q=p-q
p=p-q

print("p =",p)
print("q =",q)
