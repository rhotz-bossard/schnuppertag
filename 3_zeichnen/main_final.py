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

    window.fill(background_color)

    x = 32
    y = 32
    width = 100
    height = 200

    pygame.draw.rect(window, "red", (x, y, width, height))
    pygame.draw.circle(window, "blue", (window_width/2, window_height/2), 100)
    pygame.draw.line(window, "white", (0, 0), (window_width, window_height), 10)

    pygame.display.update()

pygame.quit()
