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

        # Initialisation de Pygame et création de la fenêtre
        #pygame.init()
        #self.fenetre = pygame.display.set_mode((self.tailleFenetreLargeur, self.tailleFetreHauteur))
        #pygame.display.set_caption("Jeu 2048")

    def afficherGrille(self, fenetre):
        # Remplir la fenêtre avec la couleur de fond (grille)
        fenetre.fill(GRIS)

        # Parcourir chaque case de la grille et dessiner des rectangles blancs pour chaque tuile
        for i in range(self.nbColonneHauteur):
            for j in range(self.nbColonneLargeur):
                # Calculer la position de chaque case
                x = j * self.tailleTuileLargeur + self.marge
                y = i * self.tailleTuileHauteur + self.marge
                # Dessiner chaque case (rectangle blanc)
                pygame.draw.rect(fenetre, BLANC, (x, y, self.tailleTuileLargeur - 2 * self.marge, self.tailleTuileHauteur - 2 * self.marge))

        # Rafraîchir l'affichage pour voir la grille
        pygame.display.flip()


# Création de l'instance de la grille
#grille = Grille()
#grille.creerGrille(nbColonneLargeur=4, nbColonneHauteur=4, tailleFenetreLargeur=400, tailleFenetreHauteur=400)  # Initialisation de la grille
#grille.afficherGrille()  # Afficher la grille

# Attendre quelques secondes pour voir la fenêtre avant de quitter
#time.sleep(5)  # Laisse la fenêtre ouverte pendant 5 secondes

# Quitter Pygame
#pygame.quit()

# %%
