#%%

import pygame
import random
import time

from classGrille import Grille  


# Couleurs pour les tuiles
COULEURS_TUILES = {
    0: (187, 173, 160),  # Couleur pour une tuile vide
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

class Tuile:
    def __init__(self, valeur):
        self.valeur = valeur
        self.couleur = self.miseAJourCouleurTuile()
        self.x = None
        self.y = None

    def deplacerTuile(self, nouvelle_x, nouvelle_y):
        self.x = nouvelle_x
        self.y = nouvelle_y

    def creerTuile(self, grille):
        # Choisir aléatoirement un des bords (haut, bas, gauche, droite)
        bord = random.choice(["haut", "bas", "gauche", "droite"])
        
        if bord == "haut":  # Si on place sur le bord supérieur
            self.x = random.randint(0, grille.nbColonneLargeur - 1)
            self.y = 0
        elif bord == "bas":  # Si on place sur le bord inférieur
            self.x = random.randint(0, grille.nbColonneLargeur - 1)
            self.y = grille.nbColonneHauteur - 1
        elif bord == "gauche":  # Si on place sur le bord gauche
            self.x = 0
            self.y = random.randint(0, grille.nbColonneHauteur - 1)
        elif bord == "droite":  # Si on place sur le bord droit
            self.x = grille.nbColonneLargeur - 1
            self.y = random.randint(0, grille.nbColonneHauteur - 1)

        # Mettre la valeur de la tuile dans la grille logique
        grille.grille[self.y][self.x] = self.valeur
        print(f"Tuile de valeur {self.valeur} placée en ({self.x}, {self.y}) sur le bord {bord}")

    def miseAJourCouleurTuile(self):
        # Retourne la couleur de la tuile en fonction de sa valeur
        return COULEURS_TUILES.get(self.valeur, (0, 0, 0))  # Noir par défaut pour les valeurs non définies

    def afficherTuile(self, fenetre, grille):
        # Dessine la tuile à sa position sur la grille
        if self.x is not None and self.y is not None:
            x = self.x * grille.tailleTuileLargeur + grille.marge
            y = self.y * grille.tailleTuileHauteur + grille.marge
            pygame.draw.rect(fenetre, self.couleur, (x, y, grille.tailleTuileLargeur - 2 * grille.marge, grille.tailleTuileHauteur - 2 * grille.marge))
            # Afficher la valeur de la tuile
            font = pygame.font.Font(None, 40)
            text = font.render(str(self.valeur), True, (0, 0, 0))  # Couleur du texte (noir)
            text_rect = text.get_rect(center=(x + (grille.tailleTuileLargeur - 2 * grille.marge) / 2, y + (grille.tailleTuileHauteur - 2 * grille.marge) / 2))
            fenetre.blit(text, text_rect)

    

