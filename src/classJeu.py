import pygame
from classGrille import Grille
from classTuile import Tuile
from classBandeau import Bandeau
from backend import User
import random
import sys

class Jeu:

    """
    Fonction __init__ : Constructeur de la classe Jeu
    Paramètres :
    - Ecran : Instance de la classe Ecran
    - idUtilisateur : Identifiant de l'utilisateur

    Description : Cette fonction initialise les attributs de la classe Jeu
    """
    def __init__(self, Ecran,idUtilisateur, bandeau):
        self.user = User()  # Crée une instance de la classe User
        self.Ecran = Ecran
        self.fenetre = Ecran.fenetre
        self.largeur = Ecran.largeur
        self.grille = None
        self.bandeau = bandeau 
        self.tuile = {  }
        self.movVel = 20
        self.id = idUtilisateur
        self.score = 0
        self.score_maximal = self.user.afficher_score(idUtilisateur)
        # Police pour le message de victoire
        self.font = pygame.font.Font(None, 50) 
        # Variable pour vérifier si la victoire a déjà été affichée
        self.victoire_affichee = False  
        # Indicateur pour vérifier si le message est actif
        self.dialog_active = False  
         

   


    
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
            self.grille.creerGrille(nbColonneLargeur, 
                                    nbColonneHauteur, 
                                    self.largeur, 
                                    hauteur, 
                                    marge, 
                                    self.bandeau.hauteurBandeau)
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


    """
    def ajouterTuilePos(self, x, y, valeur):
        tuile = Tuile(valeur)
        tuile.x = x
        tuile.y = y
        tuile.creerTuilePos(self.grille, x, y)
        self.tuile.append(tuile)
        #tuile.afficherTuile(self.fenetre, self.grille)
    """ 

    def ajouterBandeau(self, hauteur_bandeau):
        self.bandeau = Bandeau(self.largeur, hauteur_bandeau)

        print("score max ", self.score_maximal)    

    """
    Fonction dessiner : Dessine tous le jeu 
    Paramètres : Aucun

    Description : Cette fonction dessine tous le jeu

    """
    def dessiner(self):
        self.fenetre.fill((205, 192, 180))

        # Dessiner le bandeau
        self.bandeau.afficherBandeau(self.fenetre, self.score, self.score_maximal)
        

        for tuile in self.tuile.values():
            tuile.dessiner(self.fenetre)

        self.grille.dessinerGrille(self.Ecran)
        
        self.Ecran.mettreAJour()
        

    


   
    """
    Fonction afficher_message_victoire : Affiche le message de victoire
    Paramètres : Aucun

    Description : Cette fonction affiche le message de victoire    
    """
    def afficher_message_victoire(self):
     
     # Dessiner une superposition semi-transparente
     overlay = pygame.Surface((self.largeur, self.largeur))  # Créer une surface de la taille de l'écran
     overlay.set_alpha(180)  # Définir la transparence (0-255)
     overlay.fill((0, 0, 0))  # Remplir avec du noir
     self.fenetre.blit(overlay, (0, 0))  # Dessiner la superposition sur l'écran

     # Dessiner le texte de victoire
     message = self.font.render("Vous avez gagné !", True, (255, 255, 255))  # Texte en blanc
     rect_message = message.get_rect(center=(self.largeur // 2, self.largeur // 2))  # Centrer le texte
     self.fenetre.blit(message, rect_message)

     # Dessiner un bouton pour continuer ou fermer
     bouton_rect = pygame.Rect(self.largeur // 2 - 75, self.largeur // 2 + 50, 150, 50)
     pygame.draw.rect(self.fenetre, (255, 255, 255), bouton_rect)
     texte_bouton = self.font.render("Continuer", True, (0, 0, 0))
     rect_texte_bouton = texte_bouton.get_rect(center=bouton_rect.center)
     self.fenetre.blit(texte_bouton, rect_texte_bouton) 
     self.victoire_affichee = True
     pygame.display.update()  # Mettre à jour l'affichage

     #  Gérer les événements pour le bouton
     while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN and bouton_rect.collidepoint(event.pos):
                self.dialog_active = False  # Réinitialiser l'état
                return



          
    """
    Function gagnant : Vérifie si le joueur a gagné
    Paramètres : Aucun

    Description : Cette fonction vérifie si le joueur a gagné
    """
    def gagnant(self):
     print("score dans gagnant ", self.score)
     if self.score == 2048 and not self.victoire_affichee:  # Afficher le message de victoire une seule fois
        self.afficher_message_victoire()
        pygame.display.update()

       





    
    


    """
    Fonction positionAleatoire : Génère une position aléatoire pour une tuile
    Paramètres :
    - tuiles : Dictionnaire des tuiles

    Description : Cette fonction génère une position aléatoire pour une tuile
    """ 
    def positionAleatoire(self, tuiles):
        ligne = None
        col = None
        while True: 
            ligne = random.randrange(0, self.grille.nbLigne)
            col = random.randrange(0, self.grille.nbCol)

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
            ligne, col = self.positionAleatoire(tuiles)
            tuiles[f"{ligne}{col}"] = Tuile(2, ligne, col, self.grille)
        return tuiles
    
    """
    Fonction majTuile : Met à jour les tuiles
    Paramètres :
    - tuilleTrie : Liste des tuiles

    Description : Cette fonction met à jour les tuiles
    """
    def majTuile(self, tuilleTrie):
        self.tuile.clear() 
        for tuile in tuilleTrie:
            self.tuile[f"{tuile.ligne}{tuile.col}"] = tuile
        self.dessiner()
        
       

    

    """
    Fonction finMouvement : Vérifie si le jeu est terminé
    Paramètres : Aucun

    Description : Cette fonction vérifie si le jeu est terminé
    """
    def finMouvement(self):
        if (len(self.tuile) == 16):
            print("Game Over")
            return "Game Over"
        
        ligne, col = self.positionAleatoire(self.tuile)
        self.tuile[f"{ligne}{col}"] = Tuile(random.choice([2, 4]), 
                                            ligne, col, self.grille)
        return "Continue"

           

    """
    Fonction mouvement : Gère le mouvement des tusiles
    Paramètres :
    - horloge : Horloge
    - direction : Direction du mouvement

    Description : Cette fonction gère le mouvement des tuiles
    """
    def mouvement(self, horloge, direction):
        self.user =User ()
        miseAJour = True
        blocks = set()
        delta_score = 0  # Score gagné dans ce mouvement


        if direction == "left":
            funcTri = lambda x: x.col
            inverse = False
            delta = (-self.movVel, 0)
            checkLimite = lambda tuile: tuile.col == 0
            prendProchTuile = lambda tuile: self.tuile.get(
                f"{tuile.ligne}{tuile.col - 1}")
            checkFusion = (lambda tuile, 
             prochaineTuile: tuile.x > prochaineTuile.x + self.movVel)
            checkMouvement = (
                lambda tuile, prochaineTuile: tuile.x >( 
                    prochaineTuile.x + self.grille.tuileLargeur + self.movVel)
            )
            arrondir = True
        elif direction == "right":
            funcTri = lambda x: x.col
            inverse = True
            delta = (self.movVel, 0)
            checkLimite = lambda tuile: tuile.col == self.grille.nbCol - 1
            prendProchTuile = lambda tuile: self.tuile.get(
                f"{tuile.ligne}{tuile.col + 1}")
            checkFusion = (lambda tuile, 
                           prochaineTuile: tuile.x < 
                           prochaineTuile.x - self.movVel)
            checkMouvement = (
                lambda tuile, prochaineTuile: 
                (tuile.x + self.grille.tuileLargeur + self.movVel 
                 < prochaineTuile.x)
            )
            arrondir = False
        elif direction == "up":
            funcTri = lambda x: x.ligne
            inverse = False
            delta = (0, -self.movVel)
            checkLimite = lambda tuile: tuile.ligne == 0
            prendProchTuile = lambda tuile: self.tuile.get(
                f"{tuile.ligne - 1}{tuile.col}")
            checkFusion = (lambda tuile, prochaineTuile: tuile.y > 
                           (prochaineTuile.y + self.movVel))
            checkMouvement = (
                lambda tuile, prochaineTuile: tuile.y > 
                (prochaineTuile.y + self.grille.tuileHauteur + self.movVel)
            )
            arrondir = True
        elif direction == "down":
            funcTri = lambda x: x.ligne
            inverse = True
            delta = (0, +self.movVel)
            checkLimite = lambda tuile: tuile.ligne == self.grille.nbLigne - 1
            prendProchTuile = lambda tuile: self.tuile.get(
                f"{tuile.ligne + 1}{tuile.col}")
            checkFusion = (lambda tuile, prochaineTuile: tuile.y < 
                           prochaineTuile.y - self.movVel)
            checkMouvement = (
                lambda tuile, prochaineTuile: 
                (tuile.y + self.grille.tuileHauteur + self.movVel 
                 < prochaineTuile.y )
            )
            arrondir = False



        while miseAJour:
            horloge.tick(60)
            miseAJour = False

            tuileTriee = sorted(self.tuile.values(),
                                key=funcTri,
                                reverse=inverse)
           


            for i, tuile in enumerate(tuileTriee):
                if checkLimite(tuile):
                    continue
                prochaineTuile = prendProchTuile(tuile) 
                if not prochaineTuile:
                    tuile.mouvement(delta)
        
                elif (
                    tuile.valeur == prochaineTuile.valeur
                    and prochaineTuile not in blocks
                    and tuile not in blocks):
                    if checkFusion(tuile, prochaineTuile):
                        tuile.mouvement(delta)
                    else:
                        print("FUSION")
                        prochaineTuile.valeur *= 2
                        delta_score += prochaineTuile.valeur
                        tuileTriee.pop(i)
                        blocks.add(prochaineTuile)
                elif checkMouvement(tuile, prochaineTuile):
                    tuile.mouvement(delta)
                else:
                    continue
                
                tuile.prendrePos(arrondir)
                miseAJour = True
            
            self.majTuile(tuileTriee)
        
        # Mise à jour du score global après le mouvement
        self.score += delta_score
        self.gagnant()    

        if self.score > self.score_maximal:
          self.score_maximal = self.score

        # Mise à jour dans la base de données
        if  self.user.existe_utilisateur(self.id):
          self.user.update_score(self.id, self.score)
        else:
           self.user.inserer_score(self.id, self.score)
        return self.finMouvement()

        

