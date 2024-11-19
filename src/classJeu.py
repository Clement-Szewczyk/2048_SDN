import pygame
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
    def __init__(self, Ecran,id_user, bandeau):
        self.Ecran = Ecran
        self.fenetre = Ecran.fenetre
        self.largeur = Ecran.largeur
        self.grille = None
        self.bandeau = bandeau 
        self.tuile = {  }
        self.movVel = 20
        self.id = id_user
        self.score = 0
        self.score_maximal = afficher_score(id_user)
<<<<<<< HEAD
        self.font = pygame.font.Font(None, 50)  # Police pour le message de victoire
        self.victoire_affichee = False  # Variable pour vérifier si la victoire a déjà été affichée
        self.temps_debut_victoire = None  # Pour garder la trace du début du temps d'affichage
        self.dialog_active = False  # Indicateur pour vérifier si le message est actif
        self.dialog_rect = pygame.Rect(self.largeur // 4, self.largeur // 4, self.largeur // 2, 200)  # Position et taille de la boîte
        self.x_button_rect = pygame.Rect(self.dialog_rect.right - 40, self.dialog_rect.top + 10, 30, 30)  # Bouton "X"

   


    
    """
    Fonction ajouterGrille 
        Elle permet de créer une grille de jeu
    Paramètres:
    - nbColonneLargeur: nombre de colonnes en largeur
    - nbColonneHauteur: nombre de colonnes en hauteur
    - marge: marge entre les cases de la grille
    - hauteur: hauteur de la grille
    """
    def ajouterGrille(self, nbColonneLargeur, nbColonneHauteur, marge, hauteur):
            self.grille = Grille()
            self.grille.creerGrille(nbColonneLargeur, nbColonneHauteur, self.largeur, hauteur, marge, self.bandeau.hauteurBandeau)
            #self.grille.afficherGrille(self.fenetre)

    """
    Fonction ajouterTuile
        Elle permet de créer une tuile
    Paramètres:
    - valeur: valeur de la tuile
    """
    def ajouterTuile(self):
        
        valeur = 2 if random.random() < 0.9 else 4
        tuile = Tuile(valeur)
        tuile.creerTuile(self.grille)
        self.tuile.append(tuile)
        #tuile.afficherTuile(self.fenetre, self.grille)

    def ajouterTuilePos(self, x, y, valeur):
        tuile = Tuile(valeur)
        tuile.x = x
        tuile.y = y
        tuile.creerTuilePos(self.grille, x, y)
        self.tuile.append(tuile)
        #tuile.afficherTuile(self.fenetre, self.grille)
    
    def ajouterBandeau(self, hauteur_bandeau):
        self.bandeau = Bandeau(self.largeur, hauteur_bandeau)
=======
        print("score max ", self.score_maximal)
>>>>>>> 99c106882513831b3385d1c2e25c4af03365c670


    """
    Fonction dessiner : Dessine la grille de jeu
    Paramètres : Aucun

    Description : Cette fonction dessine la grille de jeu
    """
<<<<<<< HEAD
   
# Fonction afficher_message_victoire permet de definir la façon d'afficher le message 
    def afficher_message_victoire(self):
        # Afficher la boîte de dialogue
        if not self.dialog_active:
            self.dialog_active = True  # La boîte de dialogue devient active
            self.temps_debut_victoire = pygame.time.get_ticks()

        if self.dialog_active:
            # Créer la boîte modale
            pygame.draw.rect(self.fenetre, (255, 255, 255), self.dialog_rect)  # Fond de la boîte
            pygame.draw.rect(self.fenetre, (0, 0, 0), self.x_button_rect)  # Bouton "X" en noir
            pygame.draw.line(self.fenetre, (255, 255, 255), (self.x_button_rect.left, self.x_button_rect.top), 
                             (self.x_button_rect.right, self.x_button_rect.bottom), 2)  # Ligne du bouton "X"
            pygame.draw.line(self.fenetre, (255, 255, 255), (self.x_button_rect.right, self.x_button_rect.top), 
                             (self.x_button_rect.left, self.x_button_rect.bottom), 2)  # Ligne du bouton "X"
            
            # Texte du message de victoire
            message = self.font.render("Vous avez gagné !", True, (0, 0, 0))
            message_rect = message.get_rect(center=self.dialog_rect.center)
            self.fenetre.blit(message, message_rect)

            pygame.display.flip()  # Rafraîchir l'écran

# La fonction qui gére le bouton x pour fermer le message affiché
    def handle_events(self):
     print("pygame.event.get()",pygame.event.get())
     for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Click detected at {event.pos}")  # Affiche la position du clic
            if self.x_button_rect.collidepoint(event.pos):
                print("Closing victory dialog")  # Débogage
                self.dialog_active = False  # Fermer la boîte de dialogue
                self.temps_debut_victoire = None  # Réinitialiser le temps d'affichage de la victoire
                self.victoire_affichee = True  # Marquer que la victoire a été affichée
                pygame.display.update()  # Mettre à jour l'affichage pour que les changements soient visibles
            else:
                print(f"Click not on button, rect: {self.x_button_rect}")





    def afficherJeu(self):
        self.bandeau.afficherBandeau(self.fenetre, self.score, self.score_maximal)
        self.grille.afficherGrille(self.fenetre)
        for tuile in self.tuile:
            tuile.afficherTuile(self.fenetre, self.grille, self.bandeau.hauteurBandeau)

        # Vérifier si le joueur a gagné
        self.gagnat()

        # Gérer les événements de la fenêtre de message
        print("elf.dialog_active",self.dialog_active)
        if self.dialog_active:
            self.handle_events()
=======
    def dessiner(self):
        self.fenetre.fill((205, 192, 180))

        # Dessiner le bandeau
        self.bandeau.afficherBandeau(self.fenetre, self.score, self.score_maximal)
>>>>>>> 99c106882513831b3385d1c2e25c4af03365c670

        for tile in self.tuile.values():
            tile.draw(self.fenetre)

        self.grille.draw_grid(self.Ecran)
        
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
        
#La fonction gagnat 
    def gagnat(self):
        if self.score == 2048 and not self.victoire_affichee:  # Afficher le message de victoire une seule fois
            self.afficher_message_victoire()

<<<<<<< HEAD
    

    
=======
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
        self.tuile[f"{ligne}{col}"] = Tuile(random.choice([2, 4]), ligne, col, self.grille)
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
            delta = (self.movVel, 0)
            boundary_check = lambda tile: tile.col == self.grille.col - 1
            get_next_tile = lambda tile: self.tuile.get(f"{tile.ligne}{tile.col + 1}")
            merge_check = lambda tile, next_tile: tile.x < next_tile.x - self.movVel
            move_check = (
                lambda tile, next_tile: tile.x + self.grille.rectLargeur + self.movVel < next_tile.x 
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
                lambda tile, next_tile: tile.y + self.grille.rectHauteur + self.movVel < next_tile.y  
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
                        print("FUSION")
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
        return self.endMove()

        
>>>>>>> 99c106882513831b3385d1c2e25c4af03365c670
