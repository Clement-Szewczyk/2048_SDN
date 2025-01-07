import pygame
from classGrille import Grille
from classTuile import Tuile
from classBandeau import Bandeau
from Authentification import User
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
        self.scoreMaximal = self.user.afficherScore(idUtilisateur)
        # Police pour le message de victoire
        self.font = pygame.font.Font(None, 50) 
        # Variable pour vérifier si la victoire a déjà été affichée
        self.victoireAffichee = False  
        # Indicateur pour vérifier si le message est actif
        self.dialogActive = False  
         
    
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


    def ajouterBandeau(self, hauteurBandeau):
        self.bandeau = Bandeau(self.largeur, hauteurBandeau)

           

    """
    Fonction dessiner : Dessine tous le jeu 
    Paramètres : Aucun

    Description : Cette fonction dessine tous le jeu
    """
    def dessiner(self):
        self.fenetre.fill((205, 192, 180))

        # Dessiner le bandeau
        self.bandeau.afficherBandeau(self.fenetre, self.score, self.scoreMaximal)
        

        for tuile in self.tuile.values():
            tuile.dessiner(self.fenetre)

        self.grille.dessinerGrille(self.Ecran)
        
        self.Ecran.mettreAJour()
        
   
    """
    Fonction afficher_message_victoire : Affiche le message de victoire
    Paramètres : Aucun

    Description : Cette fonction affiche le message de victoire    
    """
    def afficherMessageVictoire(self):
     
     # Dessiner une superposition semi-transparente
     overlay = pygame.Surface((self.largeur, self.largeur))  # Créer une surface de la taille de l'écran
     overlay.set_alpha(180)  # Définir la transparence (0-255)
     overlay.fill((0, 0, 0))  # Remplir avec du noir
     self.fenetre.blit(overlay, (0, 0))  # Dessiner la superposition sur l'écran

     # Dessiner le texte de victoire
     message = self.font.render("Vous avez gagné !", True, (255, 255, 255))  # Texte en blanc
     rectMessage = message.get_rect(center=(self.largeur // 2, 
                                            self.largeur // 2))  # Centrer le texte
     self.fenetre.blit(message, rectMessage)

     # Dessiner un bouton pour continuer ou fermer
     boutonRect = pygame.Rect(self.largeur // 2 - 75, 
                              self.largeur // 2 + 50, 150, 50)
     pygame.draw.rect(self.fenetre, (255, 255, 255), boutonRect)
     texteBouton = self.font.render("Continuer", True, (0, 0, 0))
     rectTexteBouton = texteBouton.get_rect(center=boutonRect.center)
     self.fenetre.blit(texteBouton, rectTexteBouton) 
     self.victoireAffichee = True
     pygame.display.update()  # Mettre à jour l'affichage

     #  Gérer les événements pour le bouton
     while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if (event.type == pygame.MOUSEBUTTONDOWN 
                and boutonRect.collidepoint(event.pos)):
                self.dialogActive = False  # Réinitialiser l'état
                return



          
    """
    Function gagnant : Vérifie si le joueur a gagné
    Paramètres : Aucun

    Description : Cette fonction vérifie si le joueur a gagné
    """
    def gagnant(self):
     

     # Vérifiez si une tuile a la valeur 2048
     for tuile in self.tuile.values():
        if tuile.valeur == 2048 and not self.victoireAffichee:  # Afficher le message de victoire une seule fois
            self.afficherMessageVictoire()
            pygame.display.update()
            break

    
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
    
   
    def messagePerdant(self):
        # Dessiner une superposition semi-transparente
        overlay = pygame.Surface((self.largeur, self.largeur))  # Créer une surface de la taille de l'écran
        overlay.set_alpha(180)  # Définir la transparence (0-255)
        overlay.fill((0, 0, 0))  # Remplir avec du noir
        self.fenetre.blit(overlay, (0, 0))  # Dessiner la superposition sur l'écran

        # Dessiner le texte de victoire
        message = self.font.render("Vous avez Perdu !", True, (255, 255, 255))  # Texte en blanc
        rectMessage = message.get_rect(center=(self.largeur // 2, 
                                                self.largeur // 2))  # Centrer le texte
        self.fenetre.blit(message, rectMessage)

        # Dessiner un bouton pour continuer ou fermer
        texteBouton = self.font.render("Recommencer", True, (0, 0, 0))
        texteLargeur, texteHauteur = self.font.size("Recommencer")

        boutonRect = pygame.Rect(self.largeur // 2 - texteLargeur // 2, 
                                self.largeur // 2 + 50, texteLargeur, 
                                texteHauteur)
        pygame.draw.rect(self.fenetre, (255, 255, 255), boutonRect)
        self.fenetre.blit(texteBouton, (self.largeur // 2 - texteLargeur // 2, 
                                        self.largeur // 2 + 50)) 
        self.victoireAffichee = True
        pygame.display.update()  # Mettre à jour l'affichage

        #  Gérer les événements pour le bouton
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if (event.type == pygame.MOUSEBUTTONDOWN 
                    and boutonRect.collidepoint(event.pos)):
                        self.grille = Grille(4, 4)  # Réinitialiser la grille
                        self.score = 0  # Réinitialiser le score
                        self.tuile = self.genererTuile()  # Régénérer la tuile
                        self.dessiner()  # Redessiner le self
                        self.victoireAffichee = False   
                        return

    
    def perdant(self):
        #cette fonction va regarder si des déplacement (fusion son possible)

        for tuile in self.tuile.values():
            if tuile.col > 0:
                if (self.tuile.get(f"{tuile.ligne}{tuile.col - 1}").valeur ==
                tuile.valeur):
                    return
            if tuile.col < 3:
                if (self.tuile.get(f"{tuile.ligne}{tuile.col + 1}").valeur == 
                tuile.valeur):
                    return
            if tuile.ligne > 0:
                if (self.tuile.get(f"{tuile.ligne - 1}{tuile.col}").valeur == 
                tuile.valeur):
                    return
            if tuile.ligne < 3:
                if (self.tuile.get(f"{tuile.ligne + 1}{tuile.col}").valeur == 
                tuile.valeur):
                    return
        self.messagePerdant()
        #print("Vous avez perdu")

    

    """
    Fonction finMouvement : Vérifie si le jeu est terminé
    Paramètres : Aucun

    Description : Cette fonction vérifie si le jeu est terminé
    """
    def finMouvement(self):
        if (len(self.tuile) == 16):
            self.perdant()
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
        deltaScore = 0  # Score gagné dans ce mouvement


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
                        
                        prochaineTuile.valeur *= 2
                        deltaScore += prochaineTuile.valeur
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
        self.score += deltaScore
        self.gagnant()    

        if self.score > self.scoreMaximal:
          self.scoreMaximal = self.score

        # Mise à jour dans la base de données
        if  self.user.existeUtilisateur(self.id):
          self.user.mettreAJourScore(self.id, self.score)
        else:
           self.user.insererScore(self.id, self.score)
        return self.finMouvement()

        

