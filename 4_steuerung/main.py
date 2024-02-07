import pygame

pygame.init()

window_width = 800
window_height = 600
background_color = (25, 25, 25)
window = pygame.display.set_mode((window_width, window_height))
player_x = 32
player_y = 32
speed = 10
clock = pygame.time.Clock()

running = True
while running:
    delta_time = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()

    # TODO: Pfeiltaste nach Rechts



    window.fill(background_color)
    pygame.draw.rect(window, "red", (player_x, player_y, 64, 64))
    pygame.display.update()

pygame.quit()
