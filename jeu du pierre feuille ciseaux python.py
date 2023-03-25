from random import randint


jeu  = ["pierre", "papier", "ciseaux"]


ordinateur = jeu[randint(0,2)]


Pointsjoueur = 0
Pointsordinateur = 0

continuer = True


while(continuer):
   
    joueur = input("pierre, papier, ciseaux? ou tapez Fin pour arrêter le jeu!\n")

    
    if(joueur == 'Fin'):
        continuer = False
    elif(joueur == ordinateur):
        print("Egalité!")
    elif(joueur == "pierre"):
        if(ordinateur == "papier"):
            print("Perdu!", ordinateur, "recouvre", joueur)
            Pointsordinateur = Pointsordinateur + 1 
        else:
            print("Gagné!", joueur, "écrase", ordinateur)
            Pointsjoueur = Pointsjoueur + 1
    elif(joueur == "papier"):
        if(ordinateur == "ciseaux"):
            print("Perdu!", ordinateur, "cut", joueur)
            Pointsordinateur = Pointsordinateur + 1
        else:
            print("Gagné!", joueur, "recouvre", ordinateur)
            Pointsjoueur = Pointsjoueur + 1
    elif(joueur == "ciseaux"):
        if(ordinateur == "Rock"):
            print("Perdu...", ordinateur, "écrase", joueur)
            Pointsordinateur = Pointsordinateur + 1
        else:
            print("Gagné!", joueur, "cut", ordinateur)
            Pointsjoueur = Pointsjoueur + 1
    else:
        print("Votre choix n'est pas correct, vérifiez l'orthographe!")
    
    ordinateur = jeu[randint(0,2)]
    print('********Tour suivant********')


print("********Points********")
print("joueur: ", Pointsjoueur)
print("ordinateur: ", Pointsordinateur)