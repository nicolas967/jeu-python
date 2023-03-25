from math import * 
from random import *
nb = randint(0,100)
nb_joueurs = int(input("bienvenue au jeu du juste prix propose un nombre et je t'indiquerai si tu es au dessus ou en dessous\n"))
compteur = 0  
while nb_joueurs!=nb :
    if nb_joueurs> nb :
        print("tu es au dessus\n")
        if nb_joueurs-nb >=0 and nb_joueurs-nb <=10 :
            print("t a 10 près")
        nb_joueurs = int(input("essaie encore : "))
    elif nb_joueurs < nb :
        print("le nombre est un peu plus grand\n")
        if nb_joueurs-nb <=0 and nb_joueurs-nb >= -10 : 
            print("t a 10 près")
        nb_joueurs = int(input("remet un nombre : "))
    compteur = compteur + 1
print("gg t'as gagné gros boeau gosse")
print ("tu as mis",compteur,"essais" )
    
