# frontend.py
import re
import pygame
from Authentification import  User
class Application:
      # Initialisation de Pygame
        pygame.init()
        ecran = pygame.display.set_mode((400, 450))
        pygame.display.set_caption("Authentification")
        
        # Définition des couleurs
        BLANC = (255, 255, 255)
        GRIS_CLAIR = (245, 245, 245)
        GRIS_FONCE = (80, 80, 80)
        BLEU = (93, 139, 193)
        BLEU_CLAIR = (100, 149, 237)
        SURVOL_BLEU = (135, 206, 250)
        ROUGE = (220, 20, 60)
        NOIR = (0, 0, 0)
        OMBRE = (192, 192, 192)
     
 
    


"""
 Fonction dessinerTexte : Affiche un texte sur une surface
 Paramètres :
 - texte : Texte à afficher
 - police : Objet pygame.font.Font représentant la police à utiliser
 - couleur : Couleur du texte, format RGB
 - surface : Surface pygame où le texte sera dessiné
 - x, y : Coordonnées du coin supérieur gauche où positionner le texte

 Description : Cette fonction crée un objet texte avec la police et la couleur données, puis
 le positionne et l'affiche sur la surface spécifiée.
 """
def dessinerTexte(texte, police, couleur, surface, x, y):
    textObj = police.render(texte, True, couleur)
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObj, textRect)

"""
    Fonction validerEmail : Vérifie la validité d'une adresse email
   Paramètres :
    - email : Adresse email à valider

    Description : Cette fonction utilise une expression régulière pour vérifier si l'adresse email
    fournie respecte le format standard.
 """
def validerEmail(email):
    # Vérifie si l'email est valide avec une expression régulière
    emailRegex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(emailRegex, email) is not None

"""
    Fonction validerMdp : Vérifie si un mot de passe est valide
    Paramètres :
    - motDePasse : Mot de passe à valider

    Description : Cette fonction vérifie si le mot de passe contient au moins 5 caractères.
"""
def validerMdp(motDePasse):
    return len(motDePasse) >= 5

"""
    Classe Lien : Représente un lien cliquable
    Attributs :
    - x : Position horizontale du lien
    - y : Position verticale du lien
    - text : Texte affiché pour le lien
    - font : Police utilisée pour afficher le texte
"""
class Lien:
    """
        Méthode __init__ : Initialise un lien
        Paramètres :
        - x : Position horizontale
        - y : Position verticale
        - text : Texte du lien

        Description : Cette méthode initialise un objet Lien avec ses coordonnées,
        son texte et une police par défaut.
    """
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, 28)

    """
        Méthode dessiner : Affiche le lien sur une surface
        Paramètres :
        - surface : Surface pygame où afficher le lien

        Description : Cette méthode dessine le texte du lien à ses coordonnées sur la surface donnée.
    """
    def dessiner(self, surface):
        dessinerTexte(self.text, self.font,Application.BLEU, surface, self.x, self.y)

    """
        Méthode estSurvole : Vérifie si le lien est survolé par la souris
        Paramètres :
        - pos : Position actuelle de la souris (tuple x, y)

        Description : Cette méthode retourne True si la position de la souris est à
        l'intérieur des dimensions du texte du lien, sinon False.
    """
    def estSurvole(self, pos):
        textLargeur = self.font.size(self.text)[0]
        textHauteur = self.font.size(self.text)[1]
        return ( self.x <= pos[0] <= self.x + textLargeur and
                 self.y <= pos[1] <= self.y + textHauteur)
  

"""
    Classe Button : Représente un bouton interactif
    Attributs :
    - rect : Rectangle définissant la position et la taille du bouton
    - text : Texte affiché sur le bouton
    - font : Police utilisée pour afficher le texte
    - active : Indique si le bouton est actuellement survolé
"""
class Bouton:
    """
        Méthode __init__ : Initialise un bouton
        Paramètres :
        - x : Position horizontale du bouton
        - y : Position verticale du bouton
        - largeur : Largeur du bouton
        - hauteur : Hauteur du bouton
        - text : Texte affiché sur le bouton

        Description : Cette méthode initialise un objet Button avec ses dimensions,
        son texte, sa police, et son état actif par défaut à False.
    """
    def __init__(self, x, y, largeur, hauteur, text):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.active = False

    """
        Méthode dessiner : Affiche le bouton sur une surface
        Paramètres :
        - surface : Surface pygame où afficher le bouton

        Description : Cette méthode dessine le bouton avec un effet d'ombre et
        ajuste sa couleur si le bouton est actif (survolé).
    """
    def dessiner(self, surface):
        couleur = Application.SURVOL_BLEU if self.active else Application.BLEU
        ombre = 5  # Ajoute une ombre
        pygame.draw.rect(surface, Application.OMBRE, (self.rect.x + ombre, 
                                          self.rect.y + ombre, self.rect.width,
                                          self.rect.height), border_radius=15)
        pygame.draw.rect(surface, couleur, self.rect, border_radius=15)
        dessinerTexte(self.text, self.font, Application.BLANC, surface, self.rect.x + 20, 
                      self.rect.y + 10)

    """
        Méthode estSurvole : Vérifie si le bouton est survolé par la souris
        Paramètres :
        - pos : Position actuelle de la souris (tuple x, y)

        Description : Cette méthode retourne True si la position de la souris
        est à l'intérieur du rectangle du bouton, sinon False.
    """
    def estSurvole(self, pos):
        return self.rect.collidepoint(pos)



"""
        Classe représentant une boîte de saisie.
        :param x: Position en x de la boîte.
        :param y: Position en y de la boîte.
        :param width: Largeur de la boîte.
        :param height: Hauteur de la boîte.
        :param placeholder: Texte indicatif à afficher quand aucune donnée n'est saisie.
        """
class ZoneSaisie:
    def __init__(self, x, y, width, height, placeholder):
        self.rect = pygame.Rect(x, y, width, height)
        self.couleur = Application.GRIS_CLAIR
        self.text = ''
        self.placeholder = placeholder
        self.font = pygame.font.Font(None, 28)
        self.active = False
        self.mdpVisible = False  # Indique si le mot de passe est visible


        """
        Gère les événements liés à la boîte (clic et saisie).
        :param event: Événement Pygame à traiter.
        """
    def gererEvenement(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.couleur = Application.BLEU_CLAIR if self.active else Application.GRIS_CLAIR

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    
    """
        Bascule la visibilité du mot de passe.
        Si le mot de passe est masqué, il devient visible, et inversement.
        """
    def basculeVisibiliteMdp(self):
        self.mdpVisible = not self.mdpVisible

    """
        Dessine la boîte de saisie et son contenu à l'écran.
        :param screen: Surface Pygame sur laquelle dessiner.
        """
    def dessiner(self, surface):
        pygame.draw.rect(surface, Application.OMBRE, (self.rect.x + 3, self.rect.y + 3, 
                                          self.rect.width,
                                          self.rect.height), border_radius=10)
        pygame.draw.rect(surface, self.couleur, self.rect, border_radius=10)

        # Affichage du texte
        afficherTexte = self.text if self.mdpVisible else '*' * len(self.text) if self.placeholder == "Mot de passe" else self.text
        dessinerTexte(afficherTexte if self.text or self.placeholder == "Mot de passe" else self.placeholder, self.font, Application.NOIR if self.text else Application.GRIS_FONCE, surface, self.rect.x + 10, self.rect.y + 10)

 # Boucle principale
def main():
    utilisateur = User()
    actif = True
    font = pygame.font.Font(None, 28)

    # Champs d'entrée pour l'inscription
    champNom = ZoneSaisie(160, 50, 200, 40, "Nom")
    champPrenom = ZoneSaisie(160, 100, 200, 40, "Prénom")
    champEmail = ZoneSaisie(160, 150, 200, 40, "Email")
    champMDP = ZoneSaisie(160, 200, 200, 40, "Mot de passe")

    # Champs d'entrée pour la connexion
    champConnectEmail = ZoneSaisie(160, 60, 200, 40, "Email")
    champConnectMdp = ZoneSaisie(160, 110, 200, 40, "Mot de passe")
    # Champs d'entrée pour la modification de mot de passe 
    champConnectEmailPass = ZoneSaisie(160, 60, 200, 40, "Email")
    champConnectMdpPass = ZoneSaisie(160, 110, 200, 40, "Mot de passe")

    # État de l'application
    modeInscription = False  # Commence par la page de connexion
    message = ""  # Pour afficher les messages d'erreur ou de succès

    modeMdpOublie = False
    message = ""

    # Liens pour changer de page
    lienInscription = Lien(50, 320, "S'inscrire")  # Lien pour passer en mode inscription
    lienConnexion = Lien(170, 320, "Se connecter")  # Lien pour passer en mode connexion
    lienMdp = Lien(170, 320, "Mot de passe oublié ?")

    # Création des boutons
    boutonValider = Bouton(160, 250, 140, 50, "Valider")
    basculerBoutonMdp = Bouton(460, 200, 40, 40, "*")  # Bouton pour afficher/cacher le mot de passe

    while actif:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                actif = False

            # Gérer les événements des champs d'entrée
            if modeInscription:
                champNom.gererEvenement(event)
                champPrenom.gererEvenement(event)
                champEmail.gererEvenement(event)
                champMDP.gererEvenement(event)
            elif modeMdpOublie:
                champConnectEmailPass.gererEvenement(event)
                champConnectMdpPass.gererEvenement(event)
            else:
                champConnectEmail.gererEvenement(event)
                champConnectMdp.gererEvenement(event)

            # Gérer les clics de souris pour les boutons
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if lienInscription.estSurvole(pos) and not modeInscription:
                    modeInscription = True  # Passer à l'inscription
                    message = ""  # Réinitialiser le message
                elif lienConnexion.estSurvole(pos) and modeInscription:
                    modeInscription = False  # Passer à la connexion
                    message = ""  # Réinitialiser le message
                elif lienMdp.estSurvole(pos) and not modeMdpOublie:
                    modeMdpOublie= True
                    message= ""
                elif lienConnexion.estSurvole(pos) and modeMdpOublie:
                    modeMdpOublie = False  # Passer à la connexion
                    message = ""
                elif basculerBoutonMdp.estSurvole(pos):
                    if modeInscription:
                        champMDP.basculeVisibiliteMdp()  # Basculer la visibilité du mot de passe d'inscription
                    elif modeMdpOublie:
                        champConnectMdpPass.basculeVisibiliteMdp()  
                    else:
                        champConnectMdp.basculeVisibiliteMdp()  # Basculer la visibilité du mot de passe de connexion

                # Validation des entrées uniquement après le clic sur le bouton "Se connecter"
                if boutonValider.estSurvole(pos) and not modeInscription:
                    if not champConnectEmail.text or not champConnectMdp.text:
                        message = "Veuillez saisir votre email et mot de passe."
                    else:
                        utilisateur = utilisateur.seConnecter(champConnectEmail.text, 
                                                              champConnectMdp.text)
                        if utilisateur:
                            actif = False  # Fermer la fenêtre d'authentification
                            return utilisateur  # Indique que l'authentification a réussi
                        else:
                            message = "Nom d'utilisateur ou mot de passe incorrect."
                        champConnectEmail.text = ""
                        champConnectMdp.text = ""

                # Validation des entrées uniquement après le clic sur le bouton "S'inscrire"
                if boutonValider.estSurvole(pos) and modeInscription:
                    if (not champNom.text or 
                        not champPrenom.text or 
                        not champEmail.text or 
                        not champMDP.text):
                        message = "Veuillez saisir tous les champs requis."
                    elif not validerEmail(champEmail.text):
                        message = "L'email n'est pas valide."
                    elif not validerMdp(champMDP.text):
                            message = "Mot de passe trop court (5 caractères min)"
                                       
                    else:
                        if utilisateur.inscription(champNom.text, 
                                                   champPrenom.text, 
                                                   champEmail.text, 
                                                   champMDP.text):
                            message = "Inscription réussie!"
                        else:
                            message = "L'adresse email est déjà utilisée."

                # Validation des entrées uniquement après le clic sur le bouton "mot de passe oublier"
                if boutonValider.estSurvole(pos) and modeMdpOublie:
                    if  not champConnectEmailPass.text or not champConnectMdpPass.text:
                        message = "Veuillez saisir tous les champs requis."
                    else:
                        if utilisateur.emailExiste(champConnectEmailPass.text):
                            utilisateur.modifierMotDePasse(champConnectEmailPass.text,
                                                           champConnectMdpPass.text)
                            message = "Modification réussite!"
                        else:
                            message = "Erreur dans l'adresse email."

        # Dessiner l'écran avec un fond blanc
        Application.ecran.fill(Application.BLANC)

        # Afficher le formulaire
        if modeInscription:
            dessinerTexte("Mode Inscription", font, Application.GRIS_FONCE, Application.ecran, 20, 20)
            dessinerTexte("Nom:", font, Application.NOIR, Application.ecran, 20, 60)
            champNom.dessiner(Application.ecran)
            dessinerTexte("Prénom:", font, Application.NOIR, Application.ecran, 20, 110)
            champPrenom.dessiner(Application.ecran)
            dessinerTexte("Email:", font, Application.NOIR, Application.ecran, 20, 160)
            champEmail.dessiner(Application.ecran)
            dessinerTexte("Mot de passe:", font, Application.NOIR, Application.ecran, 20, 210)
            champMDP.dessiner(Application.ecran)
            basculerBoutonMdp.rect.topleft = (champMDP.rect.x + champMDP.rect.width + 10, 
                                              champMDP.rect.y)  # Positionner le bouton à droite du champ de mot de passe

            # Afficher le lien pour se connecter
            lienConnexion.dessiner(Application.ecran)
            
        elif modeMdpOublie:
            dessinerTexte("Réinitialiser Connexion", font, Application.GRIS_FONCE, Application.ecran, 20, 20)
            dessinerTexte("Email:", font, Application.NOIR, Application.ecran, 20, 70)
            champConnectEmailPass.dessiner(Application.ecran)
            dessinerTexte("Mot de passe:", font, Application.NOIR, Application.ecran, 20, 120)
            champConnectMdpPass.dessiner(Application.ecran)
            basculerBoutonMdp.rect.topleft = (champConnectMdpPass.rect.x + champConnectMdpPass.rect.width + 10, 
                                              champConnectMdpPass.rect.y)  # Positionner le bouton à droite du champ de mot de passe
            lienConnexion.dessiner(Application.ecran)
        else:
            dessinerTexte("Mode Connexion", font, Application.GRIS_FONCE, Application.ecran, 20, 20)
            dessinerTexte("Email:", font,Application.NOIR, Application.ecran, 20, 70)
            champConnectEmail.dessiner(Application.ecran)
            dessinerTexte("Mot de passe:", font, Application.NOIR, Application.ecran, 20, 120)
            champConnectMdp.dessiner(Application.ecran)
            basculerBoutonMdp.rect.topleft = (champConnectMdp.rect.x + champConnectMdp.rect.width + 10, 
                                              champConnectMdp.rect.y)  # Positionner le bouton à droite du champ de mot de passe

            # Afficher le lien pour s'inscrire
            lienInscription.dessiner(Application.ecran)
            lienMdp.dessiner(Application.ecran)

        # Dessiner les boutons
        boutonValider.dessiner(Application.ecran)
        basculerBoutonMdp.dessiner(Application.ecran)

        # Afficher le message d'information
        dessinerTexte(message, font, Application.ROUGE, Application.ecran, 3, 350)

        pygame.display.flip()

    pygame.quit()  # Quitter Pygame
    return False  # Indique que l'authentification a échoué
