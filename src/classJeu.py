from classGrille import Grille
from classTuile import Tuile
from classBandeau import Bandeau
from backend import afficher_score,inserer_score,update_score,existe_utilisateur
import random

class Jeu:

    """
    Fonction __init__ : Constructeur de la classe Jeu
    Paramètres :
    - Ecran : Instance de la classe Ecran
    - id_user : Identifiant de l'utilisateur

    Description : Cette fonction initialise les attributs de la classe Jeu
    """
    def __init__(self, Ecran,id_user):
        self.Ecran = Ecran
        self.fenetre = Ecran.fenetre
        self.largeur = Ecran.largeur
        self.grille = None
        self.bandeau = None
        print("largeur", self.Ecran.largeur)
        print("hauteur", self.Ecran.hauteur)
        self.tuile = { }
        self.movVel = 20
        self.id = id_user
        self.score = 0
        self.score_maximal = afficher_score(id_user)
        print("score max ", self.score_maximal)


    """
    Fonction dessiner : Dessine la grille de jeu
    Paramètres : Aucun

    Description : Cette fonction dessine la grille de jeu
    """
    def dessiner(self):
        self.fenetre.fill((205, 192, 180))

        for tile in self.tuile.values():
            tile.draw(self.fenetre)

        self.grille.draw_grid(self.Ecran)
        
        #self.tuile = {"00" : Tuile(2, 0, 0, self.grille),"02" : Tuile(2, 0, 2, self.grille) }
        self.Ecran.mettreAJour()


    """
    Fonction positionRandom : Génère une position aléatoire pour une tuile
    Paramètres :
    - tuiles : Dictionnaire des tuiles

    Description : Cette fonction génère une position aléatoire pour une tuile
    """ 
    def positionRandom(self, tuiles):
        ligne = None
        col = None
        while True: 
            ligne = random.randrange(0, self.grille.ligne)
            col = random.randrange(0, self.grille.col)

            if f"{ligne}{col}" not in tuiles:
                break
        return ligne, col
        

    """
    Fonction genererTuile : Génère une tuile
    Paramètres : Aucun

    Description : Cette fonction génère une tuile
    """
    def genererTuile(self):
        print("tuile")
        tuiles = {}
        for _ in range(2):
            ligne, col = self.positionRandom(tuiles)
            tuiles[f"{ligne}{col}"] = Tuile(2, ligne, col, self.grille)
        return tuiles
    
    """
    Fonction MajTuile : Met à jour les tuiles
    Paramètres :
    - tuilleTrie : Liste des tuiles

    Description : Cette fonction met à jour les tuiles
    """
    def MajTuile(self, tuilleTrie):
        self.tuile.clear() 
        for tuile in tuilleTrie:
            self.tuile[f"{tuile.ligne}{tuile.col}"] = tuile
        self.dessiner()
        

    """
    Fonction endMove : Vérifie si le jeu est terminé
    Paramètres : Aucun

    Description : Cette fonction vérifie si le jeu est terminé
    """
    def endMove(self):
        if (len(self.tuile) == 16):
            print("Game Over")
            return "Game Over"
        
        ligne, col = self.positionRandom(self.tuile)
        self.tuile[f"{ligne}{col}"] = Tuile(2, ligne, col, self.grille)
        return "Continue"

           

    """
    Fonction mouvement : Gère le mouvement des tuiles
    Paramètres :
    - clock : Horloge
    - direction : Direction du mouvement

    Description : Cette fonction gère le mouvement des tuiles
    """
    def mouvement(self, clock, direction):
        updated = True
        blocks = set()

        for tile in self.tuile.values():
            print(tile)


        if direction == "left":
            sort_func = lambda x: x.col
            reverse = False
            delta = (-self.movVel, 0)
            boundary_check = lambda tile: tile.col == 0
            get_next_tile = lambda tile: self.tuile.get(f"{tile.ligne}{tile.col - 1}")
            merge_check = lambda tile, next_tile: tile.x > next_tile.x + self.movVel
            move_check = (
                lambda tile, next_tile: tile.x > next_tile.x + self.grille.rectLargeur + self.movVel
            )
            ceil = True
        elif direction == "right":
            sort_func = lambda x: x.col
            reverse = True
            delta = (+self.movVel, 0)
            boundary_check = lambda tile: tile.col == self.grille.col - 1
            get_next_tile = lambda tile: self.tuile.get(f"{tile.ligne}{tile.col + 1}")
            merge_check = lambda tile, next_tile: tile.x < next_tile.x - self.movVel
            move_check = (
                lambda tile, next_tile: tile.x < next_tile.x - self.grille.rectLargeur - self.movVel
            )
            ceil = False
        elif direction == "up":
            sort_func = lambda x: x.ligne
            reverse = False
            delta = (0, -self.movVel)
            boundary_check = lambda tile: tile.ligne == 0
            get_next_tile = lambda tile: self.tuile.get(f"{tile.ligne - 1}{tile.col}")
            merge_check = lambda tile, next_tile: tile.y > next_tile.y + self.movVel
            move_check = (
                lambda tile, next_tile: tile.y > next_tile.y + self.grille.rectHauteur + self.movVel
            )
            ceil = True
        elif direction == "down":
            sort_func = lambda x: x.ligne
            reverse = True
            delta = (0, +self.movVel)
            boundary_check = lambda tile: tile.ligne == self.grille.ligne - 1
            get_next_tile = lambda tile: self.tuile.get(f"{tile.ligne + 1}{tile.col}")
            merge_check = lambda tile, next_tile: tile.y < next_tile.y - self.movVel
            move_check = (
                lambda tile, next_tile: tile.y < next_tile.y - self.grille.rectHauteur - self.movVel
            )
            ceil = False



        while updated:
            clock.tick(60)
            updated = False
            sorted_tiles = sorted(self.tuile.values(), key=sort_func, reverse=reverse)

            for i, tile in enumerate(sorted_tiles):
                if boundary_check(tile):
                    continue
                next_tile = get_next_tile(tile) 
                if not next_tile:
                    tile.move(delta)
        
                elif (
                    tile.value == next_tile.value
                    and next_tile not in blocks
                    and tile not in blocks):
                    if merge_check(tile, next_tile):
                        tile.move(delta)
                    else:
                        next_tile.value *= 2
                        sorted_tiles.pop(i)
                        blocks.add(next_tile)
                elif move_check(tile, next_tile):
                    tile.move(delta)
                else:
                    continue
                
                tile.set_pos(ceil)
                updated = True
            
            self.MajTuile(sorted_tiles)
        self.endMove()

        