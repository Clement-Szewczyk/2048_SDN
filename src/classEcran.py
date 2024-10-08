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
    
    def afficher(self):
        pygame.display.flip()

    def choixVue(self, vue):
        self.vue = vue

    def MettreAJour(self):
        pygame.display.flip()
    
    def eteindre(self):
        pygame.quit()