import pygame
import sys

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu de Voiture")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Classe pour la voiture
class Car:
    def __init__(self):
        self.width = 50
        self.height = 100
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def render(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# Classe pour les obstacles
class Obstacle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = -self.height

    def render(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))

# Fonction principale
def main():
    clock = pygame.time.Clock()
    car = Car()
    obstacles = [
        Obstacle(200, -100, 50, 100, 5),
        Obstacle(400, -300, 50, 100, 5),
        Obstacle(600, -500, 50, 100, 5),
    ]

    running = True
    while running:
        screen.fill(WHITE)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Déplacement de la voiture
        keys = pygame.key.get_pressed()
        car.move(keys)

        # Déplacement des obstacles
        for obstacle in obstacles:
            obstacle.move()

        # Vérification des collisions
        for obstacle in obstacles:
            if (
                car.x < obstacle.x + obstacle.width
                and car.x + car.width > obstacle.x
                and car.y < obstacle.y + obstacle.height
                and car.y + car.height > obstacle.y
            ):
                print("Collision !")
                running = False

        # Rendu des éléments
        car.render(screen)
        for obstacle in obstacles:
            obstacle.render(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()