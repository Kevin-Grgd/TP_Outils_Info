nombre=int(input("Entrez un nombre : "))
acc = 0

for n in range(1,nombre+1):
    acc  = acc + n
    moy = acc / nombre
print(moy)
