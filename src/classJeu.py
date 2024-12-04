import pygame
from classGrille import Grille
from classTuile import Tuile
from classBandeau import Bandeau
from backend import User
import random

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
        # Pour garder la trace du début du temps d'affichage
        self.temps_debut_victoire = None  
        # Indicateur pour vérifier si le message est actif
        self.dialog_active = False  
        # Position et taille de la boîte
        self.dialog_rect = pygame.Rect(self.largeur // 4, 
                                       self.largeur // 4, 
                                       self.largeur // 2, 200)  
        # Bouton "X"s
        self.x_boutton_rect = pygame.Rect(self.dialog_rect.right - 40, 
                                         self.dialog_rect.top + 10, 30, 30)  

   


    
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
        print("Message de victoire affiché")

        # Si la boîte de dialogue n'est pas déjà active
        if not self.dialog_active:
            self.dialog_active = True
            self.temps_debut_victoire = pygame.time.get_ticks()  # Temps de début pour la victoire
            print("Message de victoire affiché11")

        # Vérification si le message de victoire doit être affiché
        if self.dialog_active:
            print("Message de victoire affiché22")

            # Créer la boîte modale
            pygame.draw.rect(self.fenetre, (255, 255, 255), self.dialog_rect)  # Fond de la boîte
            pygame.draw.rect(self.fenetre, (0, 0, 0), self.x_boutton_rect)  # Bouton "X" en noir
            pygame.draw.line(self.fenetre, (255, 255, 255), (self.x_boutton_rect.left, self.x_boutton_rect.top), 
                            (self.x_boutton_rect.right, self.x_boutton_rect.bottom), 2)  # Ligne du bouton "X"
            pygame.draw.line(self.fenetre, (255, 255, 255), (self.x_boutton_rect.right, self.x_boutton_rect.top), 
                            (self.x_boutton_rect.left, self.x_boutton_rect.bottom), 2)  # Ligne du bouton "X"

            # Texte du message de victoire
            message = self.font.render("Vous avez gagné !", True, (0, 0, 0))
            message_rect = message.get_rect(center=self.dialog_rect.center)
            self.fenetre.blit(message, message_rect)

            pygame.display.flip()  # Rafraîchir l'écran

            # Vérifier si le temps d'affichage du message est écoulé (par exemple, 3 secondes)
            if pygame.time.get_ticks() - self.temps_debut_victoire > 3000:  # 3 secondes
                self.dialog_active = False  # Fermer le message après 3 secondes
                pygame.display.update()  # Mettre à jour l'affichage



    # La fonction qui gére le bouton x pour fermer le message affiché

    """
    Fonction eventSouris : Gère les événements
    Paramètres : Aucun

    Description : Cette fonction gère les événements
    """
    def eventSouris(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Click detecté at {event.pos}")  # Affiche la position du clic
                if self.x_boutton_rect.collidepoint(event.pos):
                    print("Closing victory dialog")  # Débogage
                    self.dialog_active = False  # Fermer la boîte de dialogue
                    self.temps_debut_victoire = None  # Réinitialiser le temps d'affichage de la victoire
                    self.victoire_affichee = True  # Marquer que la victoire a été affichée
                    pygame.display.update()  # Mettre à jour l'affichage pour que les changements soient visibles
                else:
                    print(f"Click not on button, rect: {self.x_boutton_rect}")

          
    """
    Function gagnant : Vérifie si le joueur a gagné
    Paramètres : Aucun

    Description : Cette fonction vérifie si le joueur a gagné
    """
    def gagnant(self):
     print("score dans gagnant ", self.score)
     if self.score == 4 and not self.victoire_affichee:  # Afficher le message de victoire une seule fois
        print("Victoire !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.afficher_message_victoire()
        
        # Gérer les événements après l'affichage du message de victoire
        if self.dialog_active:
            self.eventSouris()  # Appel de eventSouris ici





    
    


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

        

