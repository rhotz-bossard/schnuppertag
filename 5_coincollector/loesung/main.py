import pygame
import player
import coin


class Game:
    def __init__(self):
        pygame.init()
        self.window_width = 800
        self.window_height = 600

        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 16)
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Coin Colletor")
        self.clock = pygame.time.Clock()
        self.player = player.Player(self, 32, 32)
        
        # TODO: Münzen hinzufügen
        self.coins = [
            coin.Coin(self, 200, 250),
            coin.Coin(self, 450, 100),
            coin.Coin(self, 500, 350)
        ]

        self.run()

    def run(self):
        running = True
        while running:
            self.delta_time = self.clock.tick(60) / 1000
            self.window.fill((25, 25, 25))
            score_text = self.font.render(f"Score: {self.score}", True, "white", "black")
            self.window.blit(score_text, (405, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                
            self.player.update()
            for coin in self.coins:
                coin.update()
                if coin.is_destroyed:
                    self.coins.remove(coin)
                    self.score += 1

            pygame.display.update()

    pygame.quit()

game = Game()
