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
    user = frontend.main()  # Vérifie si l'authentification a réussi

    if user:  # Si l'authentification a réussi
        # Initialiser et afficher le jeu
        jeu = Jeu(ecran)
        jeu.ajouterGrille(4, 4, 5, 400)  # Initialiser la grille du jeu
        jeu.ajouterTuile(2)  # Ajouter une tuile de valeur 2
        jeu.ajouterTuile(4)  # Ajouter une tuile de valeur 4
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
    
    pygame.quit()  # Quitter Pygame à la fin

if __name__ == "__main__":
    main()
