#%%

import pygame
import random
import time
import math

from classGrille import Grille  

class Tuile:
    
    pygame.font.init()

    FONT = pygame.font.SysFont("comicsans", 30, bold=True)
    FONT_COLOR = (0, 0, 0)
    COLORS = [
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
    - value : Valeur de la tuile
    - ligne : Ligne de la tuile
    - col : Colonne de la tuile
    - grille : Instance de la classe Grille

    Description : Cette fonction initialise les attributs de la classe Tuile
    """
    def __init__ (self, value, ligne, col, grille):
        self.value = value
        self.ligne = ligne
        self.col = col
        self.RECT_WIDTH = grille.rectLargeur
        self.RECT_HEIGHT = grille.rectHauteur
        self.x = col * self.RECT_WIDTH
        self.y = ligne * self.RECT_HEIGHT


    """
    Fonction __str__ : Retourne une chaîne de caractères
    Paramètres : Aucun

    Description : Cette fonction retourne une chaîne de caractères
    """
    def __str__(self):
        return f"Tuile: {self.value} at ({self.ligne}, {self.col})"

    """
    Fonction get_color : Retourne la couleur de la tuile
    Paramètres : Aucun

    Description : Cette fonction retourne la couleur de la tuile
    """
    def get_color(self):
        color_index = int(math.log2(self.value)) -1
        color = self.COLORS[color_index]
        return color


    """
    Fonction draw : Dessine la tuile
    Paramètres :
    - window : Instance de la classe Ecran

    Description : Cette fonction dessine la tuile
    """
    def draw(self, window, offsetY=50):
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y + offsetY, self.RECT_WIDTH, self.RECT_HEIGHT))

        text = self.FONT.render(str(self.value), 1, self.FONT_COLOR)
        window.blit(
            text,
            (
                self.x + (self.RECT_WIDTH / 2 - text.get_width() / 2), 
                self.y + offsetY + (self.RECT_HEIGHT / 2 - text.get_height() / 2)
            ),
        )
        
    """
    Fonction set_pos : Définit la position de la tuile
    Paramètres :
    - ceil : Arrondir à l'entier supérieur
    
    Description : Cette fonction définit la position de la tuile
    """
    def set_pos(self, ceil=False):
        if ceil: 
            self.ligne = math.ceil(self.y / self.RECT_HEIGHT)
            self.col = math.ceil(self.x / self.RECT_WIDTH)
        else:
            self.ligne = math.floor(self.y / self.RECT_HEIGHT)
            self.col = math.floor(self.x / self.RECT_WIDTH)

    """
    Fonction move : Déplace la tuile
    Paramètres :
    - delta : Déplacement

    Description : Cette fonction déplace la tuile
    """
    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]

        
