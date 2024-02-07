import pygame

pygame.init()

window_width = 800
window_height = 600
background_color = (25, 25, 25)
window = pygame.display.set_mode((window_width, window_height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    x = 32
    y = 32
    width = 100
    height = 200

    # TODO: zeichne ein Rechteck


    window.fill(background_color)
    pygame.display.update()

pygame.quit()
