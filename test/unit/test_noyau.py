import pytest

from noyau import *

def test_changer_joueur():
   assert True==True


# import des modules nécessaires
import sys
import pytest

# import du module à tester
from noyau import jeton, coup_gagnant, changer_joueur, maj_jeu

# Tests unitaires
# Fonction coup_gagnant
def test_coup_gagnant():
    grille = [[-1]*7 for _ in range(6)]  # grille vide
    joueur = 0
    assert not coup_gagnant(joueur, 0, 0, grille)  # test sans jeton
    grille[0][0] = joueur  # ajout d'un jeton à la position (0,0)
    grille[1][0] = joueur  # ajout d'un jeton à la position (1,0)
    grille[2][0] = joueur  # ajout d'un jeton à la position (2,0)
    grille[3][0] = joueur  # ajout d'un jeton à la position (3,0)
    assert coup_gagnant(joueur, 3, 0, grille)  # test vertical gagnant
    grille[0][1] = joueur  # ajout d'un jeton à la position (0,1)
    grille[0][2] = joueur  # ajout d'un jeton à la position (0,2)
    grille[0][3] = joueur  # ajout d'un jeton
    
    
def test_changer_joueur():
    assert changer_joueur(1) == 0
    assert changer_joueur(1) == 1
