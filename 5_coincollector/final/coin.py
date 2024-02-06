import pygame

class Coin:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.is_destroyed = False
        
    def update(self):
        self.draw()
        # TODO Kollisionsabfrage
        if self.rect.colliderect(self.game.player.rect):
            self.is_destroyed = True

    def draw(self):
        self.rect = pygame.draw.circle(self.game.window, "yellow", (self.x, self.y), 10)

    
