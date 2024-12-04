import pygame

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (187, 173, 160)
BLEU = (70, 130, 180)

class Bandeau:
    def __init__(self, largeurFenetre, hauteurBandeau=50):
        self.largeurFenetre = largeurFenetre
        self.hauteurBandeau = hauteurBandeau
        self.police = pygame.font.Font(None, 20)

        # Définition du bouton de redémarrage
        self.boutonRedemarrerRect = pygame.Rect(
            self.largeurFenetre - 150, 10, 140, 30)

    def afficherBandeau(self, fenetre, scoreActuel, scoreMaximal):
        # Dessiner le bandeau
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

    def verifierClick(self, positionSouris):
        # Vérifier si le clic est sur le bouton de redémarrage
        return self.boutonRedemarrerRect.collidepoint(positionSouris)
