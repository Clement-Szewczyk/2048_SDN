#%%

import pygame
import random
import time
import math

from classGrille import Grille  

class Tuile:
    
    pygame.font.init()

    FONT = pygame.font.SysFont("comicsans", 30, bold=True)
    COULEUR_TEXT = (0, 0, 0)
    COULEURS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
        (236, 199, 65),
        (236, 196, 47),
        (236, 193, 40),
        (236, 190, 30),
    ]

    """
    Fonction __init__ : Constructeur de la classe Tuile
    Paramètres :
    - valeur : Valeur de la tuile
    - ligne : Ligne de la tuile 
    - col : Colonne de la tuile
    - rectLargeur : Largeur du rectangle de la grille
    - rectHauteur : Hauteur du rectangle de la grille
    - x : Position en x
    - y : Position en y

    Description : Cette fonction initialise les attributs de la classe Tuile
    """
    def __init__ (self, valeur, ligne, col, grille):
        self.valeur = valeur
        self.ligne = ligne
        self.col = col
        self.tuileLargeur = grille.tuileLargeur
        self.tuileHauteur = grille.tuileHauteur
        self.x = col * self.tuileLargeur
        self.y = ligne * self.tuileHauteur


    """
    Fonction __str__ : Retourne une chaîne de caractères
    Paramètres : Aucun

    Description : Cette fonction retourne une chaîne de caractères
    """
    def __str__(self):
        return f"Tuile: {self.valeur} at ({self.ligne}, {self.col})"

    """
    Fonction obtenirCouleur : Retourne la couleur de la tuile
    Paramètres : Aucun

    Description : Cette fonction retourne la couleur de la tuile
    """
    def obtenirCouleur(self):
        couleurIndex = int(math.log2(self.valeur)) -1
        couleur = self.COULEURS[couleurIndex]
        return couleur


    """
    Fonction dessiner : Dessine la tuile
    Paramètres :
    - fenetre : Instance de la classe Ecran

    Description : Cette fonction dessine la tuile
    """
    def dessiner(self, fenetre, offsetY=50):
        couleur = self.obtenirCouleur()
        pygame.draw.rect(fenetre, couleur, 
            (self.x, self.y + offsetY, self.tuileLargeur, self.tuileHauteur))

        text = self.FONT.render(str(self.valeur), 1, self.COULEUR_TEXT)
        fenetre.blit(
            text,
            (
                self.x + (self.tuileLargeur / 2 - text.get_width() / 2), 
                self.y + offsetY + (self.tuileHauteur / 2 -text.get_height()/2)
            ),
        )
        
    """
    Fonction prendrePos : Définit la position de la tuile
    Paramètres :
    - arrondir : Arrondir à l'entier supérieur
    
    Description : Cette fonction définit la position de la tuile
    """
    def prendrePos(self, arrondir=False):
        if arrondir: 
            self.ligne = math.ceil(self.y / self.tuileHauteur)
            self.col = math.ceil(self.x / self.tuileLargeur)
        else:
            self.ligne = math.floor(self.y / self.tuileHauteur)
            self.col = math.floor(self.x / self.tuileLargeur)

    """
    Fonction mouvement : Déplace la tuile
    Paramètres :
    - delta : Déplacement

    Description : Cette fonction déplace la tuile
    """
    def mouvement(self, delta):
        self.x += delta[0]
        self.y += delta[1]

        
