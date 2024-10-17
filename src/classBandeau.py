import pygame

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (187, 173, 160)
BLEU = (70, 130, 180)

class Bandeau:
    def __init__(self, largeur_fenetre, hauteur_bandeau=50):
        self.largeur_fenetre = largeur_fenetre
        self.hauteur_bandeau = hauteur_bandeau
        self.font = pygame.font.Font(None, 36)

        # Définition du bouton de redémarrage
        self.bouton_redemarrer_rect = pygame.Rect(self.largeur_fenetre - 150, 10, 140, 30)

    def afficher_bandeau(self, fenetre, score_actuel, score_maximal):
        # Dessiner le bandeau
        pygame.draw.rect(fenetre, GRIS, (0, 0, self.largeur_fenetre, self.hauteur_bandeau))

        # Afficher le texte du score actuel
        texte_score_actuel = self.font.render(f"Score actuel: {score_actuel}", True, NOIR)
        fenetre.blit(texte_score_actuel, (20, 10))

        # Afficher le texte du score maximal
        texte_score_maximal = self.font.render(f"Score maximal: {score_maximal}", True, NOIR)
        fenetre.blit(texte_score_maximal, (self.largeur_fenetre // 2 - 100, 10))

        # Afficher le bouton de redémarrage
        pygame.draw.rect(fenetre, BLEU, self.bouton_redemarrer_rect)
        texte_bouton = self.font.render("Redémarrer", True, BLANC)
        fenetre.blit(texte_bouton, (self.bouton_redemarrer_rect.x + 10, self.bouton_redemarrer_rect.y + 5))

    def verifier_click(self, position_souris):
        # Vérifier si le clic est sur le bouton de redémarrage
        return self.bouton_redemarrer_rect.collidepoint(position_souris)
