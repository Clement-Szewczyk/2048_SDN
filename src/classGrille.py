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

        self.contourCouleur = (187, 173, 160)
        self.contourEppaiseur = 10
        self.rectHauteur = ecran.hauteur // self.ligne
        self.rectLargeur = ecran.largeur // self.col
        
    
    """
    Fonction draw_grid : Dessine la grille
    Paramètres :
    - ecran : Instance de la classe Ecran

    Description : Cette fonction dessine la grille
    """
    def draw_grid(self, ecran):        
        for ligne in range(1, self.ligne):
            
            y = ligne * self.rectHauteur
            pygame.draw.line(ecran.fenetre, self.contourCouleur, (0,y), (ecran.largeur, y), self.contourEppaiseur)
        
        for col in range(1, self.col):
            
            x = col * self.rectLargeur
            pygame.draw.line(ecran.fenetre, self.contourCouleur, (x,0), (x, ecran.hauteur), self.contourEppaiseur)
        
        pygame.draw.rect(ecran.fenetre, self.contourCouleur, (0, 0, ecran.largeur, ecran.hauteur), self.contourEppaiseur)

