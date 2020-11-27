#NE MARCHE PAS
nombre_div=int(input("Entrer un nombre de divisions à effectuer : "))


if nombre_div == 1:
    div1 = 1+0
    div2 = 1 /div1

else :
    div1 = 1+0
    div2 = 1 / div1
    for n in range(1, nombre_div ,1):
        div1= 1 + div2
        div2 = n / div1
        
resultat= 1 + div2    
print("Le résultat est :",resultat)
