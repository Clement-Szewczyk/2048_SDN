import pygame
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
        self.tuile = []
        self.id = id_user
        self.score = 0
        self.score_maximal = afficher_score(id_user)
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


    """
    Fonction afficherJeu
        Elle permet d'afficher le jeu
    Paramètres:
    - aucun
    """
   
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

    """
    Fonction cacherJeu
        Elle permet de cacher le jeu
    Paramètres:
    - aucun
    """
    def cacherJeu(self):
        self.fenetre.fill((187, 173, 160))
    
    def TriTuile(self, direction):
        print("TRI !!!!!")
        self.infotuile()
        #Tri des tuiles en fonction de la direction
        if direction == "haut":
            self.tuile.sort(key=lambda tuile: tuile.y)
        elif direction == "bas":
            self.tuile.sort(key=lambda tuile: tuile.y, reverse=True)
        elif direction == "gauche":
            self.tuile.sort(key=lambda tuile: tuile.x)
        elif direction == "droite":
            self.tuile.sort(key=lambda tuile: tuile.x, reverse=True)

    def deplacerTuile(self, direction):
        #deplacer toute les tuile dans la direction.
        score = 0
        self.TriTuile(direction)
        for tuile in self.tuile:
            
         score= tuile.deplacerTuile(direction, self.fenetre, self.grille, self.bandeau.hauteurBandeau, self)
         if score is not None:
             if self.score < score:
              self.score = score 
             if self.score_maximal < score:
                self.score_maximal = score 
                if existe_utilisateur(self.id):
                   update_score(self.id,self.score)
                else: 
                    inserer_score(self.id,self.score)
        self.ajouterTuile()
        self.afficherJeu()
        self.Ecran.mettreAJour()
        
        

    def getTuile(self, x, y):
        #Récupérer la tuile en fonction de ses coordonnées
        for tuile in self.tuile:
            if tuile.x == x and tuile.y == y:
                return tuile
        return None

    def supprimeTuile(self, tuile):
        #Supprimer une tuile
        tuile.supprimerTuile( self.grille)
        self.tuile.remove(tuile)

    def infotuile(self):
        for tuile in self.tuile:
            print(tuile)
        
        
#La fonction gagnat 
    def gagnat(self):
        if self.score == 2048 and not self.victoire_affichee:  # Afficher le message de victoire une seule fois
            self.afficher_message_victoire()

    

    
