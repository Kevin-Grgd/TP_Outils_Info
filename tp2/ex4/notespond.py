#Definition variable
entree=input("Entrez un nombre pair de  nombres (un coefficient suivi d'une note separe par des espaces) : ")
nombre=entree.split(" ")

#Affichage note et coeff
if len(nombre)%2==0:
    for i in range(0,len(nombre),2):
        print("Une note de ",nombre[i+1]," avec un coefficient de ",nombre[i],".", sep="")

#Calcul de la moyenne pondérée        
        somme_note=0
        somme_coeff=0
        for n in range(0, len(nombre),2):
            somme_note = somme_note + (float(nombre[n+1])*float(nombre[n]))
            somme_coeff = somme_coeff + float(nombre[n])
        moyenne = somme_note / somme_coeff
    print("")
    print("La moyenne pondérée est de :" ,moyenne)

#Affichage erreur si nombre impair        
else:
    print("Erreur, il y a un nombre impair de nombre. Il manque un coefficient ou une note")
