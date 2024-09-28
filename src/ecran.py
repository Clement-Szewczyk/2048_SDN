import pygame

from classGrille import Grille


class Ecran:
    
    def __init__(self, largeur, hauteur, titre):
        self.largeur = largeur
        self.hauteur = hauteur
        self.titre = titre
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(self.titre)
    

    def ajouterGrille(self, nbColonneLargeur, nbColonneHauteur, marge):
        self.grille = Grille()
        self.grille.creerGrille(nbColonneLargeur, nbColonneHauteur, self.largeur, self.hauteur, marge)
        self.grille.afficherGrille(self.fenetre)

    def afficher(self):

        pygame.display.flip()
    
    def eteindre(self):
        pygame.quit()