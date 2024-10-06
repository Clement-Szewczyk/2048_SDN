import pygame

from classGrille import Grille
from classTuile import Tuile


class Ecran:
    
    def __init__(self, largeur, hauteur, titre):
        self.largeur = largeur
        self.hauteur = hauteur
        self.titre = titre
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        self.fenetre.fill((187, 173, 160))
        pygame.font.init()
        pygame.display.set_caption(self.titre)
    

    def ajouterGrille(self, nbColonneLargeur, nbColonneHauteur, marge):
        self.grille = Grille()
        self.grille.creerGrille(nbColonneLargeur, nbColonneHauteur, self.largeur, self.hauteur, marge)
        self.grille.afficherGrille(self.fenetre)

    def ajouterTuile(self, valeur):
        tuile = Tuile(valeur)
        tuile.creerTuile(self.grille)
        tuile.afficherTuile(self.fenetre, self.grille)

    def afficher(self):
        pygame.display.flip()
    
    def eteindre(self):
        pygame.quit()