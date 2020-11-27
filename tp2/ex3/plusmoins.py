nombre=int(input("Entrez un nombre : "))
acc = 0

for n in range(1,nombre+1):
    if n % 2 == 0:
        acc = acc - n
    else:
        acc = acc + n
print(acc)
