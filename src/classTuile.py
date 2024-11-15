#%%

import pygame
import random
import time
import math

from classGrille import Grille  

class Tuile:
    
    pygame.font.init()

    FONT = pygame.font.SysFont("comicsans", 40)
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
    ]

    def __init__ (self, value, row, col, grille):
        self.value = value
        self.row = row
        self.col = col
        self.RECT_WIDTH = grille.rectLargeur
        self.RECT_HEIGHT = grille.rectHauteur
        self.x = col * self.RECT_WIDTH
        self.y = row * self.RECT_HEIGHT

    def __str__(self):
        return f"Tuile: {self.value} at ({self.row}, {self.col})"

    def get_color(self):
        color_index = int(math.log2(self.value)) -1
        color = self.COLORS[color_index]
        return color

    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, self.RECT_WIDTH, self.RECT_HEIGHT))

        text = self.FONT.render(str(self.value), 1, self.FONT_COLOR)
        #text = str(self.value)
        window.blit(
            text,
            (
                self.x + (self.RECT_WIDTH / 2 - text.get_width() /2), 
                self.y + (self.RECT_HEIGHT / 2 - text.get_width() /2)
            ),
        )
        

    def set_pos(self, ceil=False):
        if ceil: 
            self.row = math.ceil(self.y / self.RECT_HEIGHT)
            self.col = math.ceil(self.x / self.RECT_WIDTH)
        else:
            self.row = math.floor(self.y / self.RECT_HEIGHT)
            self.col = math.floor(self.x / self.RECT_WIDTH)


    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]

        
