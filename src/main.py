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
    #user = True

    if user:  # Si l'authentification a réussi
        jeu = Jeu(ecran,user, bandeau)
        clock = pygame.time.Clock()  
        jeu.grille = Grille(4, 4, ecran)
        jeu.dessiner()
        jeu.tuile = jeu.genererTuile()
    
        
        
        # Boucle principale du jeu
        while True:
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ecran.eteindre()  # Éteindre l'écran si la fenêtre est fermée
                    return
              
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ecran.eteindre()  # Éteindre l'écran si la touche Échap est pressée
                        return
                    if event.key == pygame.K_LEFT:
                        jeu.mouvement(clock, "left")
                    if event.key == pygame.K_RIGHT:
                        jeu.mouvement(clock, "right")
                    if event.key == pygame.K_UP:
                        jeu.mouvement(clock, "up")
                    if event.key == pygame.K_DOWN:
                        jeu.mouvement(clock, "down")
                    
             # Dessiner le bandeau
            bandeau.afficherBandeau(ecran.fenetre, jeu.score, jeu.score_maximal)
            jeu.dessiner()

            
            
   
    
    pygame.quit()  # Quitter Pygame à la fin

if __name__ == "__main__":
    main()

