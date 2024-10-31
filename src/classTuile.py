#%%

import pygame
import random
import time

from classGrille import Grille  


# Couleurs pour les tuiles
COULEURS_TUILES = {
    0: (187, 173, 160),  # Couleur pour une tuile vide
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

class Tuile:

    id = 1

    def __init__(self, valeur):
        self.valeur = valeur
        self.couleur = self.miseAJourCouleurTuile()
        self.x = None
        self.y = None
        self.id = Tuile.id
        Tuile.id += 1

    def __str__(self):
        return f"Tuile {self.id} de valeur {self.valeur} en ({self.x}, {self.y})"
    

    def deplacerTuile(self, nouvelle_x, nouvelle_y):
        self.x = nouvelle_x
        self.y = nouvelle_y

    def creerTuile(self, grille):

        # Choisir aléatoirement une case vide
        casesVides = []
        for i in range(grille.nbColonneHauteur):
            for j in range(grille.nbColonneLargeur):
                if grille.grille[i][j] == 0:
                    casesVides.append((i, j))
        if casesVides:
            self.y, self.x = random.choice(casesVides)
            grille.grille[self.y][self.x] = self.valeur
           
    def creerTuilePos(self, grille, x, y):
        if grille.grille[y][x] == 0:
            self.x = x
            self.y = y
            grille.grille[y][x] = self.valeur
            
        else:
            print(f"Erreur: La case ({x}, {y}) n'est pas vide.")
    
    


    def miseAJourCouleurTuile(self):
        # Retourne la couleur de la tuile en fonction de sa valeur
        return COULEURS_TUILES.get(self.valeur, (0, 0, 0))  # Noir par défaut pour les valeurs non définies

    def afficherTuile(self, fenetre, grille, ofsety):
        # Dessine la tuile à sa position sur la grille
        if self.x is not None and self.y is not None:
            x = self.x * grille.tailleTuileLargeur + grille.marge
            y = self.y * grille.tailleTuileHauteur + grille.marge + ofsety
            pygame.draw.rect(fenetre, self.couleur, (x, y, grille.tailleTuileLargeur - 2 * grille.marge, grille.tailleTuileHauteur - 2 * grille.marge))
            # Afficher la valeur de la tuile
            font = pygame.font.Font(None, 40)
            text = font.render(str(self.valeur), True, (0, 0, 0))  # Couleur du texte (noir)
            text_rect = text.get_rect(center=(x + (grille.tailleTuileLargeur - 2 * grille.marge) / 2, y + (grille.tailleTuileHauteur - 2 * grille.marge) / 2))
            fenetre.blit(text, text_rect)

    def supprimerTuile(self, grille):
        # Supprime la tuile de la grille
        if self.x is not None and self.y is not None:
            grille.grille[self.y][self.x] = 0
            self.x = None
            self.y = None


    def fusionnerTuile(self, tuile, grille, jeu, pos):

        valeur = self.valeur * 2
        jeu.supprimeTuile(self)
        jeu.supprimeTuile(tuile)
        jeu.ajouterTuilePos(pos[0], pos[1], valeur)

        return valeur

        

    def deplacerTuile(self, direction, fenetre, grille, ofsety, jeu):
        valeur_resultat = None
        print("Je déplace la tuile ", self.id )
        
        if self.x is None or self.y is None:
            print("Erreur: La position de la tuile n'est pas définie.")
            return None
        


        

       
        if direction == "haut":
            
            while self.y > 0:
                if grille.grille[self.y - 1][self.x] == 0:
                    grille.grille[self.y][self.x] = 0
                    grille.grille[self.y - 1][self.x] = self.valeur
                    self.y -= 1
                elif grille.grille[self.y - 1][self.x] == self.valeur:
                    tuile2 = jeu.getTuile(self.x, self.y - 1)
                    valeur_resultat =  self.fusionnerTuile(tuile2, grille, jeu, (self.x-1, self.y))
                    break
                else:
                    print("Je ne peux pas aller plus haut")
                    break
                
            
             
        elif direction == "bas":
            
            while self.y < grille.nbColonneHauteur - 1:
                if grille.grille[self.y + 1][self.x] == 0:
                    grille.grille[self.y][self.x] = 0
                    grille.grille[self.y + 1][self.x] = self.valeur
                    self.y += 1
                elif grille.grille[self.y + 1][self.x] == self.valeur:
                    tuile = jeu.getTuile(self.x, self.y + 1)
                    valeur_resultat = self.fusionnerTuile(tuile, grille, jeu, (self.x, self.y+1))
                    break
                else:
                    print("Je ne peux pas aller plus bas") 
                    break
            
             
        elif direction == "gauche":
           
            while self.x > 0:
                if grille.grille[self.y][self.x - 1] == 0:
                    grille.grille[self.y][self.x] = 0
                    grille.grille[self.y][self.x - 1] = self.valeur
                    self.x -= 1
                elif grille.grille[self.y][self.x - 1] == self.valeur:
                    tuile = jeu.getTuile(self.x - 1, self.y)
                    valeur_resultat =self.fusionnerTuile(tuile, grille, jeu, (self.x-1, self.y))
                    break
                else: 
                    print("Je ne peux pas aller plus à gauche")
                    break
                    
            
        elif direction == "droite":

            while self.x < grille.nbColonneLargeur - 1:
                if grille.grille[self.y][self.x + 1] == 0:
                    grille.grille[self.y][self.x] = 0
                    grille.grille[self.y][self.x + 1] = self.valeur
                    self.x += 1
                elif grille.grille[self.y][self.x + 1] == self.valeur:
                    tuile = jeu.getTuile(self.x + 1, self.y)
                    valeur_resultat = self.fusionnerTuile(tuile, grille, jeu, (self.x+1, self.y))
                    break
                else:
                    print("Je ne peux pas aller plus à droite")
                    break
            
        else:
            print("Direction non reconnue")

        return valeur_resultat
