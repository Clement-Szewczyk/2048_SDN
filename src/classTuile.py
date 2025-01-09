
"""
Module contenant la classe Tuile pour le jeu 2048.
"""
import pygame
import random
import time
import math

from classGrille import Grille  

class Tuile:
    """
    Classe représentant une tuile du jeu 2048.

    Attributs:
        valeur (int): Valeur de la tuile.
        ligne (int): Ligne de la tuile.
        col (int): Colonne de la tuile.
        tuileLargeur (int): Largeur de la tuile.
        tuileHauteur (int): Hauteur de la tuile.
        x (int): Position en x de la tuile.
        y (int): Position en y de la tuile.
    """
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


    def __init__ (self, valeur, ligne, col, grille):
        """
        Constructeur de la classe Tuile.

        Args:
            valeur (int): Valeur de la tuile.
            ligne (int): Ligne de la tuile.
            col (int): Colonne de la tuile.
            grille (Grille): Instance de la grille contenant la tuile.

        Description:
            Cette fonction initialise les attributs de la classe Tuile.
        """
        self.valeur = valeur
        self.ligne = ligne
        self.col = col
        self.tuileLargeur = grille.tuileLargeur
        self.tuileHauteur = grille.tuileHauteur
        self.x = col * self.tuileLargeur
        self.y = ligne * self.tuileHauteur


    
    def __str__(self):
        """
        Fonction __str__ : Retourne une chaîne de caractères
        Paramètres : Aucun

        Description : Cette fonction retourne une chaîne de caractères
        """
        return f"Tuile: {self.valeur} at ({self.ligne}, {self.col})"

    
    def obtenirCouleur(self):
        """
        Fonction obtenirCouleur : Retourne la couleur de la tuile
        Paramètres : Aucun

        Description : Cette fonction retourne la couleur de la tuile
        """
        couleurIndex = int(math.log2(self.valeur)) -1
        couleur = self.COULEURS[couleurIndex]
        return couleur


  
    def dessiner(self, fenetre, decalageY=50):
        """
        Fonction dessiner : Dessine la tuile
        Paramètres :
        - fenetre : Instance de la classe Ecran

        Description : Cette fonction dessine la tuile
        """
        couleur = self.obtenirCouleur()
        pygame.draw.rect(fenetre, couleur, 
            (self.x, self.y + decalageY, self.tuileLargeur, self.tuileHauteur))

        text = self.FONT.render(str(self.valeur), 1, self.COULEUR_TEXT)
        fenetre.blit(
            text,
            (
                self.x + (self.tuileLargeur / 2 - text.get_width() / 2), 
                self.y + decalageY + (self.tuileHauteur / 2 -text.get_height()/2)
            ),
        )
        

    def prendrePos(self, arrondir=False):
        """
        Fonction prendrePos : Définit la position de la tuile
        Paramètres :
            - arrondir : Arrondir à l'entier supérieur
            
            Description : Cette fonction définit la position de la tuile
       """
        if arrondir: 
            self.ligne = math.ceil(self.y / self.tuileHauteur)
            self.col = math.ceil(self.x / self.tuileLargeur)
        else:
            self.ligne = math.floor(self.y / self.tuileHauteur)
            self.col = math.floor(self.x / self.tuileLargeur)

    
    def mouvement(self, delta):
        """
        Fonction mouvement : Déplace la tuile
        Paramètres :
        - delta : Déplacement

        Description : Cette fonction déplace la tuile
        """
        self.x += delta[0]
        self.y += delta[1]

        
