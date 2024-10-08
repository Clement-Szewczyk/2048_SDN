from classEcran import Ecran
from classJeu import Jeu
import pygame


def main():
    ecran = Ecran(800, 600, "Jeu")
    #ecran.afficher()
    jeu = Jeu(ecran)
    jeu.ajouterGrille(4, 4, 5, 400)
    jeu.ajouterTuile(2)
    
    ecran.choixVue(jeu)
    ecran.MettreAJour()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ecran.eteindre()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ecran.eteindre()
                    return
            
if __name__ == "__main__":
    main()