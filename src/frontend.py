# frontend.py

import re
import pygame
from backend import  User

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
screen = pygame.display.set_mode((400, 450))
pygame.display.set_caption("Authentification")

# Définir les couleurs modernes
WHITE = (255, 255, 255)
LIGHT_GRAY = (245, 245, 245)
DARK_GRAY = (80, 80, 80)
BLUE = (93, 139, 193)
LIGHT_BLUE = (100, 149, 237)
HOVER_BLUE = (135, 206, 250)
RED = (220, 20, 60)
BLACK = (0, 0, 0)
SHADOW = (192, 192, 192)

# Fonction pour afficher du texte
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Fonction pour valider l'email
def validate_email(email):
    # Vérifie si l'email est valide avec une expression régulière
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Fonction de validation du mot de passe (minimum 5 caractères)
def validate_password(password):
    return len(password) >= 5

# Classe pour les liens
class Link:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, 28)

    def draw(self, surface):
        draw_text(self.text, self.font, BLUE, surface, self.x, self.y)

    def is_hovered(self, pos):
        text_width = self.font.size(self.text)[0]
        text_height = self.font.size(self.text)[1]
        return self.x <= pos[0] <= self.x + text_width and self.y <= pos[1] <= self.y + text_height
    

# Classe pour les boutons
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.active = False

    def draw(self, surface):
        color = HOVER_BLUE if self.active else BLUE
        shadow_offset = 5  # Ajoute une ombre
        pygame.draw.rect(surface, SHADOW, (self.rect.x + shadow_offset, self.rect.y + shadow_offset, self.rect.width, self.rect.height), border_radius=15)
        pygame.draw.rect(surface, color, self.rect, border_radius=15)
        draw_text(self.text, self.font, WHITE, surface, self.rect.x + 20, self.rect.y + 10)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

# Classe pour les champs de texte
class InputBox:
    def __init__(self, x, y, width, height, placeholder):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = LIGHT_GRAY
        self.text = ''
        self.placeholder = placeholder
        self.font = pygame.font.Font(None, 28)
        self.active = False
        self.show_password = False  # Indique si le mot de passe est visible

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = LIGHT_BLUE if self.active else LIGHT_GRAY

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def toggle_password_visibility(self):
        self.show_password = not self.show_password

    def draw(self, surface):
        pygame.draw.rect(surface, SHADOW, (self.rect.x + 3, self.rect.y + 3, self.rect.width, self.rect.height), border_radius=10)
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)

        # Affichage du texte
        display_text = self.text if self.show_password else '*' * len(self.text) if self.placeholder == "Mot de passe" else self.text
        draw_text(display_text if self.text or self.placeholder == "Mot de passe" else self.placeholder, self.font, BLACK if self.text else DARK_GRAY, surface, self.rect.x + 10, self.rect.y + 10)

# Boucle principale
def main():
    user = User()
    running = True
    font = pygame.font.Font(None, 28)

    # Champs d'entrée pour l'inscription
    input_nom = InputBox(160, 50, 200, 40, "Nom")
    input_prenom = InputBox(160, 100, 200, 40, "Prénom")
    input_email = InputBox(160, 150, 200, 40, "Email")
    input_password = InputBox(160, 200, 200, 40, "Mot de passe")

    # Champs d'entrée pour la connexion
    input_login_email = InputBox(160, 60, 200, 40, "Email")
    input_login_password = InputBox(160, 110, 200, 40, "Mot de passe")
    # Champs d'entrée pour la modification de mot de passe 
    input_login_email_pass = InputBox(160, 60, 200, 40, "Email")
    input_login_password_pass = InputBox(160, 110, 200, 40, "Mot de passe")

    # État de l'application
    signup_mode = False  # Commence par la page de connexion
    message = ""  # Pour afficher les messages d'erreur ou de succès

    forgot_password_mode = False
    message = ""

    # Liens pour changer de page
    signup_link = Link(50, 320, "S'inscrire")  # Lien pour passer en mode inscription
    login_link = Link(170, 320, "Se connecter")  # Lien pour passer en mode connexion
    Password_link = Link(170, 320, "Mot de passe oublié ?")

    # Création des boutons
    validate_button = Button(160, 250, 140, 50, "Valider")
    toggle_password_button = Button(460, 200, 40, 40, "*")  # Bouton pour afficher/cacher le mot de passe

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Gérer les événements des champs d'entrée
            if signup_mode:
                input_nom.handle_event(event)
                input_prenom.handle_event(event)
                input_email.handle_event(event)
                input_password.handle_event(event)
            elif forgot_password_mode:
                input_login_email_pass.handle_event(event)
                input_login_password_pass.handle_event(event)
            else:
                input_login_email.handle_event(event)
                input_login_password.handle_event(event)

            # Gérer les clics de souris pour les boutons
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if signup_link.is_hovered(pos) and not signup_mode:
                    signup_mode = True  # Passer à l'inscription
                    message = ""  # Réinitialiser le message
                elif login_link.is_hovered(pos) and signup_mode:
                    signup_mode = False  # Passer à la connexion
                    message = ""  # Réinitialiser le message
                elif Password_link.is_hovered(pos) and not forgot_password_mode:
                    forgot_password_mode= True
                    message= ""
                elif login_link.is_hovered(pos) and forgot_password_mode:
                    forgot_password_mode = False  # Passer à la connexion
                    message = ""
                elif toggle_password_button.is_hovered(pos):
                    if signup_mode:
                        input_password.toggle_password_visibility()  # Basculer la visibilité du mot de passe d'inscription
                    elif forgot_password_mode:
                        input_login_password_pass.toggle_password_visibility()  
                    else:
                        input_login_password.toggle_password_visibility()  # Basculer la visibilité du mot de passe de connexion

                # Validation des entrées uniquement après le clic sur le bouton "Se connecter"
                if validate_button.is_hovered(pos) and not signup_mode:
                    if not input_login_email.text or not input_login_password.text:
                        message = "Veuillez saisir votre email et mot de passe."
                    else:
                        user = user.login(input_login_email.text, input_login_password.text)
                        if user:
                            running = False  # Fermer la fenêtre d'authentification
                            return user  # Indique que l'authentification a réussi
                        else:
                            message = "Nom d'utilisateur ou mot de passe incorrect."
                        input_login_email.text = ""
                        input_login_password.text = ""

                # Validation des entrées uniquement après le clic sur le bouton "S'inscrire"
                if validate_button.is_hovered(pos) and signup_mode:
                    if not input_nom.text or not input_prenom.text or not input_email.text or not input_password.text:
                        message = "Veuillez saisir tous les champs requis."
                    elif not validate_email(input_email.text):
                        message = "L'email n'est pas valide."
                    elif not validate_password(input_password.text):
                            message = "Mot de passe trop court (5 caractères min)"
                                       
                    else:
                        if user.signup(input_nom.text, input_prenom.text, input_email.text, input_password.text):
                            message = "Inscription réussie!"
                        else:
                            message = "L'adresse email est déjà utilisée."

                # Validation des entrées uniquement après le clic sur le bouton "mot de passe oublier"
                if validate_button.is_hovered(pos) and forgot_password_mode:
                    if  not input_login_email_pass.text or not input_login_password_pass.text:
                        message = "Veuillez saisir tous les champs requis."
                    else:
                        if user.Email_existe(input_login_email_pass.text):
                            user.modifier_mot_de_passe(input_login_email_pass.text,input_login_password_pass.text)
                            message = "Modification réussite!"
                        else:
                            message = "Erreur dans l'adresse email."

        # Dessiner l'écran avec un fond blanc
        screen.fill(WHITE)

        # Afficher le formulaire
        if signup_mode:
            draw_text("Mode Inscription", font, DARK_GRAY, screen, 20, 20)
            draw_text("Nom:", font, BLACK, screen, 20, 60)
            input_nom.draw(screen)
            draw_text("Prénom:", font, BLACK, screen, 20, 110)
            input_prenom.draw(screen)
            draw_text("Email:", font, BLACK, screen, 20, 160)
            input_email.draw(screen)
            draw_text("Mot de passe:", font, BLACK, screen, 20, 210)
            input_password.draw(screen)
            toggle_password_button.rect.topleft = (input_password.rect.x + input_password.rect.width + 10, input_password.rect.y)  # Positionner le bouton à droite du champ de mot de passe

            # Afficher le lien pour se connecter
            login_link.draw(screen)
            
        elif forgot_password_mode:
            draw_text("Réinitialiser Connexion", font, DARK_GRAY, screen, 20, 20)
            draw_text("Email:", font, BLACK, screen, 20, 70)
            input_login_email_pass.draw(screen)
            draw_text("Mot de passe:", font, BLACK, screen, 20, 120)
            input_login_password_pass.draw(screen)
            toggle_password_button.rect.topleft = (input_login_password_pass.rect.x + input_login_password_pass.rect.width + 10, input_login_password_pass.rect.y)  # Positionner le bouton à droite du champ de mot de passe
            login_link.draw(screen)
        else:
            draw_text("Mode Connexion", font, DARK_GRAY, screen, 20, 20)
            draw_text("Email:", font, BLACK, screen, 20, 70)
            input_login_email.draw(screen)
            draw_text("Mot de passe:", font, BLACK, screen, 20, 120)
            input_login_password.draw(screen)
            toggle_password_button.rect.topleft = (input_login_password.rect.x + input_login_password.rect.width + 10, input_login_password.rect.y)  # Positionner le bouton à droite du champ de mot de passe

            # Afficher le lien pour s'inscrire
            signup_link.draw(screen)
            Password_link.draw(screen)

        # Dessiner les boutons
        validate_button.draw(screen)
        toggle_password_button.draw(screen)

        # Afficher le message d'information
        draw_text(message, font, RED, screen, 3, 350)

        pygame.display.flip()

    pygame.quit()  # Quitter Pygame
    return False  # Indique que l'authentification a échoué
