import pygame

class Ecran:
    
    def __init__(self, largeur, hauteur, titre):
        self.largeur = largeur
        self.hauteur = hauteur
        self.titre = titre
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        self.fenetre.fill((187, 173, 160))
        pygame.font.init()
        pygame.display.set_caption(self.titre)

    """
    Fonction Clear
        Elle permet d'enlver ce qui est afficher à l'écran
    Paramètres : 

    """
    def clear(self):
        #clear l'écran
        self.fenetre.fill((187, 173, 160))


    """
    Fonction mettreAJour
        Elle permet de mettre à jour l'écran
    Paramètres:
    - aucun
    """
    def mettreAJour(self):
        pygame.display.flip()
    
    """
    Fonction eteindre
        Elle permet d'éteindre l'écran
    Paramètres:
    - aucun
    """
    def eteindre(self):
        pygame.quit()