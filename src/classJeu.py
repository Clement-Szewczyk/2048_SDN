from classGrille import Grille
from classTuile import Tuile

class Jeu:
    def __init__(self, Ecran):
        self.fenetre = Ecran.fenetre
        self.largeur = Ecran.largeur
        self.grille = None
        self.tuile = None


    def ajouterGrille(self, nbColonneLargeur, nbColonneHauteur, marge, hauteur):
            self.grille = Grille()
            self.grille.creerGrille(nbColonneLargeur, nbColonneHauteur, self.largeur, hauteur, marge)
            self.grille.afficherGrille(self.fenetre)

    def ajouterTuile(self, valeur):
        tuile = Tuile(valeur)
        tuile.creerTuile(self.grille)
        tuile.afficherTuile(self.fenetre, self.grille)