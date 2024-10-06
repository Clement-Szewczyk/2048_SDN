#%%

import pygame
import time

# Couleurs et autres constantes pour la grille
BLANC = (255, 255, 255)
GRIS = (187, 173, 160)

class Grille:
    def creerGrille(self, nbColonneLargeur=4, nbColonneHauteur=4, tailleFenetreLargeur=400, tailleFenetreHauteur=400, marge=5):
        # Initialisation des attributs de la grille
        self.nbColonneLargeur = nbColonneLargeur
        self.nbColonneHauteur = nbColonneHauteur
        self.tailleFenetreLargeur = tailleFenetreLargeur
        self.tailleFenetreHauteur = tailleFenetreHauteur
        self.marge = marge

        # Calcul des tailles des tuiles
        self.tailleTuileLargeur = self.tailleFenetreLargeur // self.nbColonneLargeur
        self.tailleTuileHauteur = self.tailleFenetreHauteur // self.nbColonneHauteur

        # Initialisation de la grille logique (liste de listes)
        self.grille = [[0 for _ in range(self.nbColonneLargeur)] for _ in range(self.nbColonneHauteur)]

        # Initialisation de Pygame et création de la fenêtre
        pygame.init()
        self.fenetre = pygame.display.set_mode((self.tailleFenetreLargeur, self.tailleFenetreHauteur))
        pygame.display.set_caption("Jeu 2048")

    def afficherGrille(self):
        # Remplir la fenêtre avec la couleur de fond (grille)
        self.fenetre.fill(GRIS)

        # Parcourir chaque case de la grille et dessiner des rectangles blancs pour chaque tuile
        for i in range(self.nbColonneHauteur):
            for j in range(self.nbColonneLargeur):
                # Calculer la position de chaque case
                x = j * self.tailleTuileLargeur + self.marge
                y = i * self.tailleTuileHauteur + self.marge
                # Dessiner chaque case (rectangle blanc)
                pygame.draw.rect(self.fenetre, BLANC, (x, y, self.tailleTuileLargeur - 2 * self.marge, self.tailleTuileHauteur - 2 * self.marge))

        # Rafraîchir l'affichage pour voir la grille
        pygame.display.flip()

# %%
