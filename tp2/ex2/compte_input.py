nombre=int(input("Quelle liste de nombre afficher ? : "))

for n in range(1,(nombre)+1):
    print(n, ", sa racine carré est ", n**0.5,".",sep="")
    n=n+1
