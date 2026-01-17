import pygame
import sys
from pygame.locals import *


def mainloop():

    pygame.init()

    #screen size
    screen = pygame.display.set_mode((1280, 720))

    centerx , centery = screen.get_rect().centerx , screen.get_rect().centery

    #setting the variable bg to the background image
    bg = pygame.image.load("data/images/dinosadventurebg.png").convert_alpha()
    bg = pygame.transform.scale(bg, (1280, 720))

    #settings startbtn to the button image
    startbtn = pygame.image.load("data/images/startnewgamebtn.png").convert_alpha()
    startbtn = pygame.transform.scale(startbtn, (350, 100))

    loadbtn = pygame.image.load("data/images/loadgamebtn.png").convert_alpha()
    loadbtn = pygame.transform.scale(loadbtn, (630, 190))

    def draw_img(img, x ,y):
        screen.blit(img, (x, y))

    def clicked():
        pos = pygame.mouse.get_pos()
        if pygame.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return "clicked"


    font = pygame.font.SysFont("arialblack", 40)
    textcolor = (255, 255, 255)

    def draw_text(text, font , textcolor, x, y):
        img = font.render(text, True, textcolor)
        screen.blit(img, (x, y))


    pygame.display.set_caption("Dino's Adventure")

    clock = pygame.time.Clock()

    running = True
    while running:

        screen.fill("black")
        screen.blit(bg, (0, 0))
        draw_img(startbtn, centerx - startbtn.get_width() / 2 , centery - startbtn.get_height() / 0.9)
        draw_img(loadbtn, centerx - loadbtn.get_width() / 2 , centery + startbtn.get_height() / 2.2)

        #clicked()

        #draw_text("Welcome to Dino's Adventure", font, textcolor, 250, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #pygame.draw.rect(screen, "white", pygame.Rect(600, 360, 200, 50), 2, 5)

        pygame.display.flip()
        pygame.display.update()

        clock.tick(60)

    pygame.quit()