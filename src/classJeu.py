from classGrille import Grille
from classTuile import Tuile

class Jeu:
    def __init__(self, Ecran):
        self.Ecran = Ecran
        self.fenetre = Ecran.fenetre
        self.largeur = Ecran.largeur
        self.grille = None
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
            self.grille.creerGrille(nbColonneLargeur, nbColonneHauteur, self.largeur, hauteur, marge)
            #self.grille.afficherGrille(self.fenetre)

    """
    Fonction ajouterTuile
        Elle permet de créer une tuile
    Paramètres:
    - valeur: valeur de la tuile
    """
    def ajouterTuile(self, valeur):
        tuile = Tuile(valeur)
        tuile.creerTuile(self.grille)
        self.tuile.append(tuile)
        #tuile.afficherTuile(self.fenetre, self.grille)
    

    """
    Fonction afficherJeu
        Elle permet d'afficher le jeu
    Paramètres:
    - aucun
    """
    def afficherJeu(self):
        self.grille.afficherGrille(self.fenetre)
        for tuile in self.tuile:
            tuile.afficherTuile(self.fenetre, self.grille)
    

    """
    Fonction cacherJeu
        Elle permet de cacher le jeu
    Paramètres:
    - aucun
    """
    def cacherJeu(self):
        self.fenetre.fill((187, 173, 160))
    
    def TriTuile(self, direction):
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
            tuile.deplacerTuile(direction, self.fenetre, self.grille)
        self.afficherJeu()
        self.Ecran.mettreAJour()

        
        
        

