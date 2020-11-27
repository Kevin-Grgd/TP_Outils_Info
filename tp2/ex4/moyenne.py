entree=input("Entrez les notes : (separees par des espaces) ")
note=entree.split(" ")
acc=0
somme_note=0

for i in range(0, len(note)):
    somme_note = somme_note + float(note[i])
    acc = acc + 1
    
moyenne = somme_note / acc
print("La moyenne est",moyenne)
