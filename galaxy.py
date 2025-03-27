import pygame
import random
import sys

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galaxy Shooter")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Classe pour le vaisseau
class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = 5
        self.bullets = []

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def shoot(self):
        bullet = Bullet(self.x + self.width // 2 - 5, self.y)
        self.bullets.append(bullet)

    def render(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
        for bullet in self.bullets:
            bullet.render(screen)

# Classe pour les balles
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 20
        self.speed = 7

    def move(self):
        self.y -= self.speed

    def render(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# Classe pour les ennemis
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = speed

    def move(self):
        self.y += self.speed

    def render(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

# Fonction principale
def main():
    clock = pygame.time.Clock()
    player = Player()
    enemies = [Enemy(random.randint(0, SCREEN_WIDTH - 50), random.randint(-150, -50), random.randint(2, 5)) for _ in range(5)]

    running = True
    while running:
        screen.fill(BLACK)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.shoot()

        # Déplacement du joueur
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Déplacement des balles
        for bullet in player.bullets[:]:
            bullet.move()
            if bullet.y < 0:
                player.bullets.remove(bullet)

        # Déplacement des ennemis
        for enemy in enemies[:]:
            enemy.move()
            if enemy.y > SCREEN_HEIGHT:
                enemies.remove(enemy)
                enemies.append(Enemy(random.randint(0, SCREEN_WIDTH - 50), random.randint(-150, -50), random.randint(2, 5)))

        # Vérification des collisions
        for enemy in enemies[:]:
            for bullet in player.bullets[:]:
                if (
                    bullet.x < enemy.x + enemy.width
                    and bullet.x + bullet.width > enemy.x
                    and bullet.y < enemy.y + enemy.height
                    and bullet.y + bullet.height > enemy.y
                ):
                    player.bullets.remove(bullet)
                    enemies.remove(enemy)
                    enemies.append(Enemy(random.randint(0, SCREEN_WIDTH - 50), random.randint(-150, -50), random.randint(2, 5)))

        # Rendu des éléments
        player.render(screen)
        for enemy in enemies:
            enemy.render(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()