#%%

import pygame
import time
from classGrille import Grille
from classTuile import Tuile

# Initialiser Pygame
pygame.init()

# Création de la grille
grille = Grille()
grille.creerGrille(nbColonneLargeur=4, nbColonneHauteur=4, tailleFenetreLargeur=400, tailleFenetreHauteur=400)

# Affichage initial de la grille
grille.afficherGrille()

# Création et positionnement aléatoire d'une tuile sur un bord
tuile = Tuile()
tuile.creerTuile(grille)

# Affichage de la tuile sur la grille
tuile.afficherTuile(grille.fenetre, grille)

# Attendre avant de quitter pour voir la fenêtre
time.sleep(5)
pygame.quit()
# %%
