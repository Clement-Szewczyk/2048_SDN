import pygame

from classGrille import Grille

class Ecran:
    
    """
    Fonction __init__ : Constructeur de la classe Ecran
    Paramètres :
    - largeur : Largeur de l'écran
    - hauteur : Hauteur de l'écran
    - titre : Titre de l'écran

    Description : Cette fonction initialise les attributs de la classe Ecran
    """
    def __init__(self, largeur, hauteur, titre):
        self.largeur = largeur
        self.hauteur = hauteur
        self.titre = titre
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        
        pygame.font.init()
        pygame.display.set_caption(self.titre)

    

    
    """
    Fonction afficherGrille
        Elle permet d'afficher la grille
    Paramètres:
    - grille : Instance de la classe Grille
    - ecran : Instance de la classe

    Description : Cette fonction affiche la grille
    """
    def afficherGrille(grille, ecran):
        grille.dessinerGrille(ecran)


    

    """
    Fonction mettreAJour
        Elle permet de mettre à jour l'écran
    Paramètres:
    - aucun

    Description : Cette fonction met à jour l'écran
    """
    def mettreAJour(self):
        pygame.display.update()
    
    """
    Fonction eteindre
        Elle permet d'éteindre l'écran
    Paramètres:
    - aucun

    Description : Cette fonction éteint l'écran
    """
    def eteindre(self):
        pygame.quit()