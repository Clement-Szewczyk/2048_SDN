from classGrille import Grille
from classTuile import Tuile
from classBandeau import Bandeau
import random

class Jeu:
    def __init__(self, Ecran):
        self.Ecran = Ecran
        self.fenetre = Ecran.fenetre
        self.largeur = Ecran.largeur
        self.grille = None
        self.bandeau = None
        self.tuile = []

  
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
    def afficherJeu(self):
        self.bandeau.afficherBandeau(self.fenetre, 0, 0)
        self.grille.afficherGrille(self.fenetre)
        for tuile in self.tuile:
            tuile.afficherTuile(self.fenetre, self.grille, self.bandeau.hauteurBandeau)
    

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
        self.TriTuile(direction)
        for tuile in self.tuile:
            
            tuile.deplacerTuile(direction, self.fenetre, self.grille, self.bandeau.hauteurBandeau, self)
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
        
        

