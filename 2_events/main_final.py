import pygame

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_Q:
            running = False

    window.fill((25, 25, 25))
    pygame.display.update()

pygame.quit()
