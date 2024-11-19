import pygame
import time

class Grille:

    """
    Fonction __init__ : Constructeur de la classe Grille
    Paramètres :
    - ligne : Nombre de lignes
    - col : Nombre de colonnes
    - ecran : Instance de la classe Ecran

    Description : Cette fonction initialise les attributs de la classe Grille
    """
    def __init__(self, ligne, col, ecran):
        self.ligne = ligne
        self.col = col
        self.rectHauteur = None
        self.rectLargeur = None
        self.largeur = 400
        self.hauteur = 400
        self.contourCouleur = (187, 173, 160)
        self.contourEppaiseur = 5
        self.rectHauteur = self.hauteur / self.ligne
        self.rectLargeur = self.largeur / self.col
        
    
    """
    Fonction draw_grid : Dessine la grille
    Paramètres :
    - ecran : Instance de la classe Ecran

    Description : Cette fonction dessine la grille
    """
    def draw_grid(self, ecran, offsetY=50):        
        for ligne in range(1, self.ligne):
            y = ligne * self.rectHauteur + offsetY
            pygame.draw.line(ecran.fenetre, self.contourCouleur, (0, y), (self.largeur, y), self.contourEppaiseur)
        
        for col in range(1, self.col):
            x = col * self.rectLargeur
            pygame.draw.line(ecran.fenetre, self.contourCouleur, (x, 0 + offsetY), (x, self.hauteur + offsetY), self.contourEppaiseur)
        
        pygame.draw.rect(ecran.fenetre, self.contourCouleur, (0, 0 + offsetY, self.largeur, self.hauteur), self.contourEppaiseur)