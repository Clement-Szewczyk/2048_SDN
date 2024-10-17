#%%

import pygame

# Initialiser Pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grille 4x4 avec déplacement")

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Taille des cellules
cell_size = width // 4

# Position initiale de la case rouge (ligne 0, colonne 0)
position_x, position_y = 0, 0

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Gérer les flèches pour déplacer la case
            if event.key == pygame.K_LEFT and position_x > 0:
                position_x -= 1
            if event.key == pygame.K_RIGHT and position_x < 3:
                position_x += 1
            if event.key == pygame.K_UP and position_y > 0:
                position_y -= 1
            if event.key == pygame.K_DOWN and position_y < 3:
                position_y += 1

    # Remplir l'écran en blanc
    screen.fill(white)

    # Dessiner la grille
    for row in range(5):
        pygame.draw.line(screen, black, (0, row * cell_size), (width, row * cell_size), 2)
        pygame.draw.line(screen, black, (row * cell_size, 0), (row * cell_size, height), 2)

    # Dessiner la case rouge à sa position actuelle
    pygame.draw.rect(screen, red, (position_x * cell_size, position_y * cell_size, cell_size, cell_size))

    # Mettre à jour l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()

# %%
