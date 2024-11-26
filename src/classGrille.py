import pygame
import time

class Grille:

    """
    Fonction __init__ : Constructeur de la classe Grille
    Paramètres :
    - nbligne : Nombre de lignes
    - nbcol : Nombre de colonnes
    - largeur : Largeur de la grille
    - hauteur : Hauteur de la grille
    - contourCouleur : Couleur du contour
    - contourEppaiseur : Épaisseur du contour
    - tuileHauteur : Hauteur de la tuile
    - tuileLargeur : Largeur de la tuile

    Description : Cette fonction initialise les attributs de la classe Grille
    """
    def __init__(self, nbligne, nbcol):
        self.nbligne = nbligne
        self.nbcol = nbcol
        self.largeur = 400
        self.hauteur = 400
        self.contourCouleur = (187, 173, 160)
        self.contourEppaiseur = 5
        self.tuileHauteur = self.hauteur / self.nbligne
        self.tuileLargeur = self.largeur / self.nbligne
        
    
    """
    Fonction draw_grid : Dessine la grille
    Paramètres :
    - ecran : Instance de la classe Ecran
    - decalageY : Décalage en y

    Description : Cette fonction dessine la grille
    """
    def draw_grid(self, ecran, decalageY=50):        
        for ligne in range(1, self.nbligne):
            y = ligne * self.tuileHauteur + decalageY
            pygame.draw.line(ecran.fenetre, self.contourCouleur, (0, y), 
                             (self.largeur, y), self.contourEppaiseur)
        
        for col in range(1, self.nbcol):
            x = col * self.tuileLargeur
            pygame.draw.line(ecran.fenetre, self.contourCouleur, 
                             (x, 0 + decalageY), 
                             (x, self.hauteur + decalageY), 
                             self.contourEppaiseur)
        
        pygame.draw.rect(ecran.fenetre, self.contourCouleur, 
                         (0, 0 + decalageY, self.largeur, self.hauteur), 
                         self.contourEppaiseur)