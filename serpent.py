import pygame
import time
import random
 
# Initialisation de pygame
pygame.init()
 
# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (213, 50, 80)
VERT = (0, 255, 0)
BLEU = (50, 153, 213)
 
# Dimensions de la fenêtre du jeu
LARGEUR = 600
HAUTEUR = 400
 
# Taille du serpent
TAILLE_SERPENT = 10
VITESSE = 15
 
# Police de texte
police = pygame.font.SysFont("bahnschrift", 25)
 
# Création de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du Serpent")
 
# Horloge pour contrôler la vitesse du jeu
horloge = pygame.time.Clock()
 
# Fonction pour afficher le serpent
def dessiner_serpent(taille, pixels):
    for pixel in pixels:
        pygame.draw.rect(fenetre, NOIR, [pixel[0], pixel[1], taille, taille])
 
# Fonction pour afficher le score
def afficher_score(score):
    texte = police.render(f"Score: {score}", True, BLEU)
    fenetre.blit(texte, [10, 10])
 
# Boucle principale du jeu
def jeu():
    game_over = False
    game_close = False
 
    x = LARGEUR / 2
    y = HAUTEUR / 2
 
    x_change = 0
    y_change = 0
 
    serpent_pixels = []
    longueur_serpent = 1
 
    # Position aléatoire de la nourriture
    nourriture_x = round(random.randrange(0, LARGEUR - TAILLE_SERPENT) / 10.0) * 10.0
    nourriture_y = round(random.randrange(0, HAUTEUR - TAILLE_SERPENT) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close:
            fenetre.fill(BLANC)
            texte_fin = police.render("Game Over! Appuyez sur C pour rejouer ou Q pour quitter", True, ROUGE)
            fenetre.blit(texte_fin, [LARGEUR / 6, HAUTEUR / 3])
            afficher_score(longueur_serpent - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jeu()
 
        # Gestion des événements (clavier)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -TAILLE_SERPENT
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = TAILLE_SERPENT
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -TAILLE_SERPENT
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = TAILLE_SERPENT
                    x_change = 0
 
        # Vérification des collisions avec les bords
        if x >= LARGEUR or x < 0 or y >= HAUTEUR or y < 0:
            game_close = True
 
        x += x_change
        y += y_change
 
        fenetre.fill(BLANC)
        pygame.draw.rect(fenetre, VERT, [nourriture_x, nourriture_y, TAILLE_SERPENT, TAILLE_SERPENT])
 
        # Ajout des pixels du serpent
        serpent_pixels.append([x, y])
        if len(serpent_pixels) > longueur_serpent:
            del serpent_pixels[0]
 
        # Vérification de collision avec soi-même
        for pixel in serpent_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True
 
        dessiner_serpent(TAILLE_SERPENT, serpent_pixels)
        afficher_score(longueur_serpent - 1)
 
        pygame.display.update()
 
        # Si le serpent mange la nourriture
        if x == nourriture_x and y == nourriture_y:
            nourriture_x = round(random.randrange(0, LARGEUR - TAILLE_SERPENT) / 10.0) * 10.0
            nourriture_y = round(random.randrange(0, HAUTEUR - TAILLE_SERPENT) / 10.0) * 10.0
            longueur_serpent += 1
 
        horloge.tick(VITESSE)
 
    pygame.quit()
    quit()
 
# Lancement du jeu
jeu()