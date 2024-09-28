from ecran import Ecran
import pygame


def main():
    ecran = Ecran(800, 600, "Jeu")
    ecran.afficher()
    ecran.ajouterGrille(4,4,5)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ecran.eteindre()
                return
            
if __name__ == "__main__":
    main()