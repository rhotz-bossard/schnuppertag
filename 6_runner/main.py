import pygame
import random

pygame.init()

# game constants
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
WIDTH = 450
HEIGHT = 300

# game variables
score = 0
player_x = 50
player_y = 200
y_change = 0
x_change = 0
gravity = 0.5
obstacles = [300, 400, 600]
obstacles_speed = 2
active = False

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Infinite Runner")

background = black
fps = 60
font = pygame.font.Font("freesansbold.ttf", 16)
timer = pygame.time.Clock()

running = True

while running:
    timer.tick(fps)
    screen.fill(background)
    if not active:
        instruction_text = font.render("Press space to start", True, white, black)
        screen.blit(instruction_text, (140, 50))
    score_text = font.render(f"Score: {score}", True, white, black)
    screen.blit(score_text, (160, 250))

    floor = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])
    player = pygame.draw.rect(screen, green, [player_x, player_y, 20, 20])
    obstacles0 = pygame.draw.rect(screen, red, [obstacles[0], 200, 20, 20])
    obstacles1 = pygame.draw.rect(screen, orange, [obstacles[1], 200, 20, 20])
    obstacles2 = pygame.draw.rect(screen, yellow, [obstacles[2], 200, 20, 20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles = [300, 400, 600]
                player_x = 50
                score = 0
                active = True

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 10
            if event.key == pygame.K_RIGHT:
                x_change = 2
            if event.key == pygame.K_LEFT:
                x_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = 0


    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacles_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(470, 570)
                score += 1
            if player.colliderect(obstacles0) or player.colliderect(obstacles1) or player.colliderect(obstacles2):
                active = False

    if 0 <= player_x <= 430:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 430:
        player_x = 430


    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if y_change > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0
        

    pygame.display.flip()
pygame.quit()


