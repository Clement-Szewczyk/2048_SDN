from classGrille import Grille
from classTuile import Tuile
from classBandeau import Bandeau
from backend import afficher_score,inserer_score,update_score,existe_utilisateur
import random

class Jeu:
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


    def dessiner(self):
        self.fenetre.fill((205, 192, 180))

        for tile in self.tuile.values():
            tile.draw(self.fenetre)

        self.grille.draw_grid(self.Ecran)
        
        #self.tuile = {"00" : Tuile(2, 0, 0, self.grille),"02" : Tuile(2, 0, 2, self.grille) }
        self.Ecran.mettreAJour()
        
    def positionRandom(self, tiles):
        row = None
        col = None
        while True: 
            row = random.randrange(0, self.grille.ligne)
            col = random.randrange(0, self.grille.col)

            if f"{row}{col}" not in tiles:
                break
        return row, col
        

    def genererTuile(self):
        print("tuile")
        tiles = {}
        for _ in range(2):
            row, col = self.positionRandom(tiles)
            tiles[f"{row}{col}"] = Tuile(2, row, col, self.grille)
        return tiles
    

    def updateTiles(self, sorted_tiles):
        self.tuile.clear() 
        for tile in sorted_tiles:
            self.tuile[f"{tile.row}{tile.col}"] = tile
        self.dessiner()
        


    def endMove(self):
        if (len(self.tuile) == 16):
            print("Game Over")
            return "Game Over"
        row, col = self.positionRandom(self.tuile)

        print("row", row)
        print("col", col)
        self.tuile[f"{row}{col}"] = Tuile(2, row, col, self.grille)
        return "COntinue"

           


    def move_tiles(self, clock, direction):
        updated = True
        blocks = set()

        for tile in self.tuile.values():
            print(tile)


        if direction == "left":
            sort_func = lambda x: x.col
            reverse = False
            delta = (-self.movVel, 0)
            boundary_check = lambda tile: tile.col == 0
            get_next_tile = lambda tile: self.tuile.get(f"{tile.row}{tile.col - 1}")
            merge_check = lambda tile, next_tile: tile.x > next_tile.x + self.movVel
            move_check = (
                lambda tile, next_tile: tile.x > next_tile.x + self.grille.rectLargeur + self.movVel
            )
            ceil = True
        elif direction == "right":
            sort_func = lambda x: x.col
            reverse = True
            delta = (self.movVel, 0)
            boundary_check = lambda tile: tile.col == self.grille.col - 1
            get_next_tile = lambda tile: self.tuile.get(f"{tile.row}{tile.col + 1}")
            merge_check = lambda tile, next_tile: tile.x < next_tile.x - self.movVel
            move_check = (
                lambda tile, next_tile: tile.x < next_tile.x - self.grille.rectLargeur - self.movVel
            )
            ceil = True
        elif direction == "up":
            sort_func = lambda x: x.row
            reverse = False
            delta = (0, -self.movVel)
            boundary_check = lambda tile: tile.row == 0
            get_next_tile = lambda tile: self.tuile.get(f"{tile.row - 1}{tile.col}")
            merge_check = lambda tile, next_tile: tile.y > next_tile.y + self.movVel
            move_check = (
                lambda tile, next_tile: tile.y > next_tile.y + self.grille.rectHauteur + self.movVel
            )
            ceil = True
        elif direction == "down":
            sort_func = lambda x: x.row
            reverse = True
            delta = (0, self.movVel)
            boundary_check = lambda tile: tile.row == self.grille.ligne - 1
            get_next_tile = lambda tile: self.tuile.get(f"{tile.row + 1}{tile.col}")
            merge_check = lambda tile, next_tile: tile.y < next_tile.y - self.movVel
            move_check = (
                lambda tile, next_tile: tile.y < next_tile.y - self.grille.rectHauteur - self.movVel
            )
            ceil = True
        else:
            pass


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
                    updated = True
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
            
            self.updateTiles(sorted_tiles)
        self.endMove()

        