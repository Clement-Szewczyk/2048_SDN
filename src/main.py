#%%

import pygame
from classEcran import Ecran
from classGrille import Grille
from classJeu import Jeu
from classBandeau import Bandeau
import frontend  # Importer le module frontend

def main():
    
    FPS = 60
    # Initialisation de Pygame
    pygame.init()
    
    # Créer une instance de l'écran
    ecran = Ecran(400, 450, "2048 SDN")

    # Créer une instance du bandeau
    bandeau = Bandeau(ecran.largeur)  
    # Appel de la fonction main du fichier frontend pour l'authentification
    user = frontend.main()  # Vérifie si l'authentification a réussi
    user = True

    if user:  # Si l'authentification a réussi
        jeu = Jeu(ecran,user, bandeau)
        clock = pygame.time.Clock()  
        jeu.grille = Grille(4, 4)
        jeu.dessiner()
        jeu.tuile = jeu.genererTuile()
    
        
        
        # Boucle principale du jeu
        while True:
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Éteindre l'écran si la fenêtre est fermée
                    ecran.eteindre()  
                    return
              
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Éteindre l'écran si la touche Échap est pressées
                        ecran.eteindre()  
                        return
                    if event.key == pygame.K_LEFT:
                        jeu.mouvement(clock, "left")
                    if event.key == pygame.K_RIGHT:
                        jeu.mouvement(clock, "right")
                    if event.key == pygame.K_UP:
                        jeu.mouvement(clock, "up")
                    if event.key == pygame.K_DOWN:
                        jeu.mouvement(clock, "down")
                        
                # Si un clic souris est effectué
                if event.type == pygame.MOUSEBUTTONDOWN:  
                     # Vérifier si le clic est sur le bouton "Redémarrer"
                    if bandeau.verifierClick(event.pos): 
                        jeu.grille = Grille(4, 4)  # Réinitialiser la grille
                        jeu.score = 0  # Réinitialiser le score
                        jeu.tuile = jeu.genererTuile()  # Régénérer la tuile
                        jeu.dessiner()  # Redessiner le jeu
                        jeu.victoire_affichee = False
                    
             # Dessiner le bandeau
            bandeau.afficherBandeau(ecran.fenetre, jeu.score, jeu.score_maximal)
            jeu.dessiner()

            
            
   
    
    pygame.quit()  # Quitter Pygame à la fin

if __name__ == "__main__":
    main()

