# frontend.py
import re
import pygame
from backend import  User

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
ecran = pygame.display.set_mode((400, 450))
pygame.display.set_caption("Authentification")

# Définir les couleurs modernes
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
    Classe Link : Représente un lien cliquable
    Attributs :
    - x : Position horizontale du lien
    - y : Position verticale du lien
    - text : Texte affiché pour le lien
    - font : Police utilisée pour afficher le texte
"""
class Link:
    """
        Méthode __init__ : Initialise un lien
        Paramètres :
        - x : Position horizontale
        - y : Position verticale
        - text : Texte du lien

        Description : Cette méthode initialise un objet Link avec ses coordonnées,
        son texte et une police par défaut.
    """
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, 28)

    """
        Méthode draw : Affiche le lien sur une surface
        Paramètres :
        - surface : Surface pygame où afficher le lien

        Description : Cette méthode dessine le texte du lien à ses coordonnées sur la surface donnée.
    """
    def draw(self, surface):
        dessinerTexte(self.text, self.font, BLEU, surface, self.x, self.y)

    """
        Méthode estSurvole : Vérifie si le lien est survolé par la souris
        Paramètres :
        - pos : Position actuelle de la souris (tuple x, y)

        Description : Cette méthode retourne True si la position de la souris est à
        l'intérieur des dimensions du texte du lien, sinon False.
    """
    def estSurvole(self, pos):
        textWidth = self.font.size(self.text)[0]
        textHeight = self.font.size(self.text)[1]
        return self.x <= pos[0] <= self.x + textWidth and self.y <= pos[1] <= self.y + textHeight
  

"""
    Classe Button : Représente un bouton interactif
    Attributs :
    - rect : Rectangle définissant la position et la taille du bouton
    - text : Texte affiché sur le bouton
    - font : Police utilisée pour afficher le texte
    - active : Indique si le bouton est actuellement survolé
"""
class Button:
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
        Méthode draw : Affiche le bouton sur une surface
        Paramètres :
        - surface : Surface pygame où afficher le bouton

        Description : Cette méthode dessine le bouton avec un effet d'ombre et
        ajuste sa couleur si le bouton est actif (survolé).
    """
    def draw(self, surface):
        color = SURVOL_BLEU if self.active else BLEU
        shadow_offset = 5  # Ajoute une ombre
        pygame.draw.rect(surface, OMBRE, (self.rect.x + shadow_offset, self.rect.y + shadow_offset, self.rect.width, self.rect.height), border_radius=15)
        pygame.draw.rect(surface, color, self.rect, border_radius=15)
        dessinerTexte(self.text, self.font, BLANC, surface, self.rect.x + 20, self.rect.y + 10)

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
class InputBox:
    def __init__(self, x, y, width, height, placeholder):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRIS_CLAIR
        self.text = ''
        self.placeholder = placeholder
        self.font = pygame.font.Font(None, 28)
        self.active = False
        self.show_password = False  # Indique si le mot de passe est visible


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
            self.color = BLEU_CLAIR if self.active else GRIS_CLAIR

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
        self.show_password = not self.show_password

    """
        Dessine la boîte de saisie et son contenu à l'écran.
        :param screen: Surface Pygame sur laquelle dessiner.
        """
    def draw(self, surface):
        pygame.draw.rect(surface, OMBRE, (self.rect.x + 3, self.rect.y + 3, self.rect.width, self.rect.height), border_radius=10)
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)

        # Affichage du texte
        afficherTexte = self.text if self.show_password else '*' * len(self.text) if self.placeholder == "Mot de passe" else self.text
        dessinerTexte(afficherTexte if self.text or self.placeholder == "Mot de passe" else self.placeholder, self.font, NOIR if self.text else GRIS_FONCE, surface, self.rect.x + 10, self.rect.y + 10)

# Boucle principale
def main():
    user = User()
    actif = True
    font = pygame.font.Font(None, 28)

    # Champs d'entrée pour l'inscription
    inputNom = InputBox(160, 50, 200, 40, "Nom")
    inputPrenom = InputBox(160, 100, 200, 40, "Prénom")
    inputEmail = InputBox(160, 150, 200, 40, "Email")
    inputMdp = InputBox(160, 200, 200, 40, "Mot de passe")

    # Champs d'entrée pour la connexion
    inputLoginEmail = InputBox(160, 60, 200, 40, "Email")
    inputLoginPassword = InputBox(160, 110, 200, 40, "Mot de passe")
    # Champs d'entrée pour la modification de mot de passe 
    inputLoginEmailPass = InputBox(160, 60, 200, 40, "Email")
    inputLoginPasswordPass = InputBox(160, 110, 200, 40, "Mot de passe")

    # État de l'application
    modeInscription = False  # Commence par la page de connexion
    message = ""  # Pour afficher les messages d'erreur ou de succès

    modeMdpOublie = False
    message = ""

    # Liens pour changer de page
    lienInscription = Link(50, 320, "S'inscrire")  # Lien pour passer en mode inscription
    lienConnexion = Link(170, 320, "Se connecter")  # Lien pour passer en mode connexion
    lienMdp = Link(170, 320, "Mot de passe oublié ?")

    # Création des boutons
    boutonValider = Button(160, 250, 140, 50, "Valider")
    basculerBoutonMdp = Button(460, 200, 40, 40, "*")  # Bouton pour afficher/cacher le mot de passe

    while actif:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                actif = False

            # Gérer les événements des champs d'entrée
            if modeInscription:
                inputNom.gererEvenement(event)
                inputPrenom.gererEvenement(event)
                inputEmail.gererEvenement(event)
                inputMdp.gererEvenement(event)
            elif modeMdpOublie:
                inputLoginEmailPass.gererEvenement(event)
                inputLoginPasswordPass.gererEvenement(event)
            else:
                inputLoginEmail.gererEvenement(event)
                inputLoginPassword.gererEvenement(event)

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
                        inputMdp.basculeVisibiliteMdp()  # Basculer la visibilité du mot de passe d'inscription
                    elif modeMdpOublie:
                        inputLoginPasswordPass.basculeVisibiliteMdp()  
                    else:
                        inputLoginPassword.basculeVisibiliteMdp()  # Basculer la visibilité du mot de passe de connexion

                # Validation des entrées uniquement après le clic sur le bouton "Se connecter"
                if boutonValider.estSurvole(pos) and not modeInscription:
                    if not inputLoginEmail.text or not inputLoginPassword.text:
                        message = "Veuillez saisir votre email et mot de passe."
                    else:
                        user = user.seConnecter(inputLoginEmail.text, inputLoginPassword.text)
                        if user:
                            actif = False  # Fermer la fenêtre d'authentification
                            return user  # Indique que l'authentification a réussi
                        else:
                            message = "Nom d'utilisateur ou mot de passe incorrect."
                        inputLoginEmail.text = ""
                        inputLoginPassword.text = ""

                # Validation des entrées uniquement après le clic sur le bouton "S'inscrire"
                if boutonValider.estSurvole(pos) and modeInscription:
                    if not inputNom.text or not inputPrenom.text or not inputEmail.text or not inputMdp.text:
                        message = "Veuillez saisir tous les champs requis."
                    elif not validerEmail(inputEmail.text):
                        message = "L'email n'est pas valide."
                    elif not validerMdp(inputMdp.text):
                            message = "Mot de passe trop court (5 caractères min)"
                                       
                    else:
                        if user.inscription(inputNom.text, inputPrenom.text, inputEmail.text, inputMdp.text):
                            message = "Inscription réussie!"
                        else:
                            message = "L'adresse email est déjà utilisée."

                # Validation des entrées uniquement après le clic sur le bouton "mot de passe oublier"
                if boutonValider.estSurvole(pos) and modeMdpOublie:
                    if  not inputLoginEmailPass.text or not inputLoginPasswordPass.text:
                        message = "Veuillez saisir tous les champs requis."
                    else:
                        if user.emailExiste(inputLoginEmailPass.text):
                            user.modifierMotDePasse(inputLoginEmailPass.text,inputLoginPasswordPass.text)
                            message = "Modification réussite!"
                        else:
                            message = "Erreur dans l'adresse email."

        # Dessiner l'écran avec un fond blanc
        ecran.fill(BLANC)

        # Afficher le formulaire
        if modeInscription:
            dessinerTexte("Mode Inscription", font, GRIS_FONCE, ecran, 20, 20)
            dessinerTexte("Nom:", font, NOIR, ecran, 20, 60)
            inputNom.draw(ecran)
            dessinerTexte("Prénom:", font, NOIR, ecran, 20, 110)
            inputPrenom.draw(ecran)
            dessinerTexte("Email:", font, NOIR, ecran, 20, 160)
            inputEmail.draw(ecran)
            dessinerTexte("Mot de passe:", font, NOIR, ecran, 20, 210)
            inputMdp.draw(ecran)
            basculerBoutonMdp.rect.topleft = (inputMdp.rect.x + inputMdp.rect.width + 10, inputMdp.rect.y)  # Positionner le bouton à droite du champ de mot de passe

            # Afficher le lien pour se connecter
            lienConnexion.draw(ecran)
            
        elif modeMdpOublie:
            dessinerTexte("Réinitialiser Connexion", font, GRIS_FONCE, ecran, 20, 20)
            dessinerTexte("Email:", font, NOIR, ecran, 20, 70)
            inputLoginEmailPass.draw(ecran)
            dessinerTexte("Mot de passe:", font, NOIR, ecran, 20, 120)
            inputLoginPasswordPass.draw(ecran)
            basculerBoutonMdp.rect.topleft = (inputLoginPasswordPass.rect.x + inputLoginPasswordPass.rect.width + 10, inputLoginPasswordPass.rect.y)  # Positionner le bouton à droite du champ de mot de passe
            lienConnexion.draw(ecran)
        else:
            dessinerTexte("Mode Connexion", font, GRIS_FONCE, ecran, 20, 20)
            dessinerTexte("Email:", font, NOIR, ecran, 20, 70)
            inputLoginEmail.draw(ecran)
            dessinerTexte("Mot de passe:", font, NOIR, ecran, 20, 120)
            inputLoginPassword.draw(ecran)
            basculerBoutonMdp.rect.topleft = (inputLoginPassword.rect.x + inputLoginPassword.rect.width + 10, inputLoginPassword.rect.y)  # Positionner le bouton à droite du champ de mot de passe

            # Afficher le lien pour s'inscrire
            lienInscription.draw(ecran)
            lienMdp.draw(ecran)

        # Dessiner les boutons
        boutonValider.draw(ecran)
        basculerBoutonMdp.draw(ecran)

        # Afficher le message d'information
        dessinerTexte(message, font, ROUGE, ecran, 3, 350)

        pygame.display.flip()

    pygame.quit()  # Quitter Pygame
    return False  # Indique que l'authentification a échoué
