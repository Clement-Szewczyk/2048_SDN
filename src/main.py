#%%

import pygame
from classEcran import Ecran
from classJeu import Jeu
import frontend  # Importer le module frontend

def main():
    # Initialisation de Pygame
    pygame.init()
    
    # Créer une instance de l'écran
    ecran = Ecran(800, 600, "Jeu")

    # Appel de la fonction main du fichier frontend pour l'authentification
    #user = frontend.main()  # Vérifie si l'authentification a réussi
    user = True

    if user:  # Si l'authentification a réussi
        ecran.clear()
        ecran.mettreAJour()
        # Initialiser et afficher le jeu
        jeu = Jeu(ecran)
        jeu.ajouterBandeau(50)  # Initialiser le bandeau du jeu
        jeu.ajouterGrille(4, 4, 5, 400)  # Initialiser la grille du jeu
        jeu.ajouterTuile()  # Ajouter une tuile de valeur 2
        jeu.ajouterTuile()  # Ajouter une tuile de valeur 4
        jeu.afficherJeu()  # Afficher l'état du jeu
        ecran.mettreAJour()  # Mettre à jour l'affichage de l'écran

        # Boucle principale du jeu
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ecran.eteindre()  # Éteindre l'écran si la fenêtre est fermée
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ecran.eteindre()  # Éteindre l'écran si la touche Échap est pressée
                        return
                    if event.key == pygame.K_UP:
                        jeu.deplacerTuile("haut")
                    if event.key == pygame.K_DOWN:
                        jeu.deplacerTuile("bas")
                    if event.key == pygame.K_LEFT:
                        jeu.deplacerTuile("gauche")
                    if event.key == pygame.K_RIGHT:
                        jeu.deplacerTuile("droite")
                    
   
    
    pygame.quit()  # Quitter Pygame à la fin

if __name__ == "__main__":
    main()

# %%
