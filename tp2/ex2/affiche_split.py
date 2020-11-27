entree=str(input("Entrez une chaîne de caractère : "))
parties = entree.split(" ")
print(entree)
print("Il y a ", len(parties),"partie(s).")

for n in range(len(parties)):
    print(" - partie ",n," : ",parties[n], sep="")

