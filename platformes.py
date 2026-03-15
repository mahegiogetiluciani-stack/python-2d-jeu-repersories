import pygame
import sys
import datetime

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mon jeu")

WHITE = (255,255,255)
BLUE = (0,128,255)
GREEN = (0,200,0)

playersize = 50
playerpos = [WIDTH//2, HEIGHT-playersize]

# plateforme
platform = pygame.Rect(200, 400, 400, 20)

floor = HEIGHT - playersize

clock = pygame.time.Clock()

velocity_y = 0
gravity = 0.5
jump_power = -15
on_ground = False

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        playerpos[0] -= 5
        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(d,"gauche")

    if keys[pygame.K_d]:
        playerpos[0] += 5
        c = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(c,"droite")

    if keys[pygame.K_z] and on_ground:
        velocity_y = jump_power
        on_ground = False
        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(d,"sauter")

    # gravité
    velocity_y += gravity
    playerpos[1] += velocity_y

    player_rect = pygame.Rect(playerpos[0], playerpos[1], playersize, playersize)

    # collision plateforme
    if player_rect.colliderect(platform) and velocity_y >= 0:
        playerpos[1] = platform.top - playersize
        velocity_y = 0
        on_ground = True
        a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(a,"plateforme toucher")



    # collision sol
    if playerpos[1] >= floor:
        playerpos[1] = floor
        velocity_y = 0
        on_ground = True
        e = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(e,"sol toucher")

    # limites écran
    if playerpos[0] < 0:
        playerpos[0] = 0
    if playerpos[0] > WIDTH - playersize:
        playerpos[0] = WIDTH - playersize

    screen.fill(WHITE)

    # dessiner plateforme
    pygame.draw.rect(screen, GREEN, platform)

    # dessiner joueur
    pygame.draw.rect(screen, BLUE, (playerpos[0], playerpos[1], playersize, playersize))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
