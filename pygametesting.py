import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load("data/images/dinosadventurebg.png")
bg = pygame.transform.scale(bg, (1280, 720))
while running:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
    screen.fill("black")
    screen.blit(bg, (0, 0))
    #pygame.draw.rect(screen, "white", pygame.Rect(600, 360, 200, 50), 2, 5)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()