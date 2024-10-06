from ecran import Ecran
import pygame


def main():
    ecran = Ecran(800, 600, "Jeu")
    ecran.afficher()
    ecran.ajouterGrille(4,4,5)
    ecran.ajouterTuile(2)
    ecran.ajouterTuile(4)
    ecran.ajouterTuile(2)
    ecran.ajouterTuile(4)
    ecran.ajouterTuile(2)
    ecran.ajouterTuile(4)
    ecran.ajouterTuile(2)
    ecran.ajouterTuile(4)

    
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