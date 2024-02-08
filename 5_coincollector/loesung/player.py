import pygame


class Player:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.surface = game.window

    def update(self):
        self.rect = pygame.draw.rect(self.surface, "red", (self.x, self.y, 64, 64))
        self.movement(10)
        self.draw()

    def draw(self):
        pygame.draw.rect(self.surface, "red", (self.x, self.y, 64, 64))

    def movement(self, speed):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += speed
        if keys[pygame.K_LEFT]:
            self.x -= speed
        if keys[pygame.K_DOWN]:
            self.y += speed
        if keys[pygame.K_UP]:
            self.y -= speed

