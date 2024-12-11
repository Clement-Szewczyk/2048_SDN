import pygame

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (187, 173, 160)
BLEU = (70, 130, 180)


"""
        Initialisation du bandeau avec la largeur de la fenêtre et la hauteur du bandeau.
        Le bouton de redémarrage est aussi défini ici.

        :param largeurFenetre: Largeur de la fenêtre de jeu
        :param hauteurBandeau: Hauteur du bandeau en haut de l'écran
        """
class Bandeau:
    def __init__(self, largeurFenetre, hauteurBandeau=50):
        self.largeurFenetre = largeurFenetre
        self.hauteurBandeau = hauteurBandeau
        self.police = pygame.font.Font(None, 20)

        # Définition du bouton de redémarrage
        self.boutonRedemarrerRect = pygame.Rect(
            self.largeurFenetre - 150, 10, 140, 30)


    """
        Affiche le bandeau avec le score actuel, le score maximal et le bouton de redémarrage.
        
        :param fenetre: Fenêtre sur laquelle afficher le bandeau
        :param scoreActuel: Le score actuel du jeu
        :param scoreMaximal: Le score maximal atteint jusqu'à présent
        """
    def afficherBandeau(self, fenetre, scoreActuel, scoreMaximal):
        pygame.draw.rect(fenetre, GRIS, 
                         (0, 0, self.largeurFenetre, self.hauteurBandeau))

        # Afficher le texte du score actuel
        texteScoreActuel = self.police.render(f"Score actuel: {scoreActuel}", 
                                              True, NOIR)
        fenetre.blit(texteScoreActuel, (10, 10))

        # Afficher le texte du score maximal
        texteScoreMaximal = self.police.render(f"Score maximal: {scoreMaximal}",
                                               True, NOIR)
        fenetre.blit(texteScoreMaximal, (self.largeurFenetre // 2 - 190, 30))

        # Afficher le bouton de redémarrage
        pygame.draw.rect(fenetre, BLEU, self.boutonRedemarrerRect)
        texteBouton = self.police.render("Redémarrer", True, BLANC)
        fenetre.blit(texteBouton, (self.boutonRedemarrerRect.x + 10,
                                    self.boutonRedemarrerRect.y + 5))

        """
        Vérifie si un clic de souris a eu lieu sur le bouton de redémarrage.

        :param positionSouris: Position du clic de souris
        :return: True si le clic est dans la zone du bouton, sinon False
        """
    def verifierClick(self, positionSouris):
        return self.boutonRedemarrerRect.collidepoint(positionSouris)
