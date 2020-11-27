print("Choisissez un animal dans cette liste : Oiseau, Moustique, Chat, Chien, Tyrannosaure, Ptérodactyle.")
print("Répondez par oui ou par non uniquement")

reponse = input("Votre animal est-il est un dinosaure ?  ")
if reponse == "oui" or reponse == "Oui":
    reponse2 = input("Votre animal peut-il voler ? ")
    if reponse2 == "oui" or reponse2 == "Oui":
        print("Vous avez choisi le Ptérodactyle.")
    elif reponse2 =="non" or reponse2 == "Non":
        print("Vous avez choisi le Tyrannosaure.")
elif reponse == "non" or reponse == "Non":
    reponse = input("Votre animal a-t-il des poils ? ")
    if reponse == "oui" or reponse =="Oui":
        reponse2 = input("Votre animal miaule-t-il ? ")
        if reponse2 == "oui" or reponse2 == "Oui":
            print("Vous avez choisi le chat.")
        elif reponse2 == "non" or reponse2 == "Non":
            print("Vous avez choisi le chien.")
    elif reponse == "non" or reponse == "Non":
        reponse = input("Votre animal a-t-il des plûmes ? ")
        if reponse == "oui" or reponse == "Oui":
            print("Vous avez choisi l'oiseau.")
        elif reponse == "non" or reponse == "Non":
            print("Vous avez choisi le moustique.")
