import pygame
import time

# Couleurs et autres constantes pour la grille
BLANC = (255, 255, 255)
GRIS = (187, 173, 160)

class Grille:
    def __init__(self, ligne, col, ecran):
        self.ligne = ligne
        self.col = col
        self.rectHauteur = None
        self.rectLargeur = None

        self.contourCouleur = (187, 173, 160)
        self.contourEppaiseur = 10
        self.rectHauteur = ecran.hauteur // self.ligne
        self.rectLargeur = ecran.largeur // self.col
        
    
    def draw_grid(self, ecran):
        ##ecran.fenetre.fill((205, 192, 180))
        
        for row in range(1, self.ligne):
            
            y = row * self.rectHauteur
            pygame.draw.line(ecran.fenetre, self.contourCouleur, (0,y), (ecran.largeur, y), self.contourEppaiseur)
        
        for col in range(1, self.col):
            
            x = col * self.rectLargeur
            pygame.draw.line(ecran.fenetre, self.contourCouleur, (x,0), (x, ecran.hauteur), self.contourEppaiseur)
        
        pygame.draw.rect(ecran.fenetre, self.contourCouleur, (0, 0, ecran.largeur, ecran.hauteur), self.contourEppaiseur)

