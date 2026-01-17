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

    #setting startbtn to the button image
    startbtn = pygame.image.load("data/images/startnewgamebtn.png").convert_alpha()
    startbtn = pygame.transform.scale(startbtn, (350, 100))

    loadbtn = pygame.image.load("data/images/loadgamebtn.png").convert_alpha()
    loadbtn = pygame.transform.scale(loadbtn, (300, 90))

    quitbtn = pygame.image.load("data/images/quitbtn.png").convert_alpha()
    quitbtn = pygame.transform.scale(quitbtn, (250, 75))

    settingsbtn = pygame.image.load("data/images/settingsbtn.png").convert_alpha()
    settingsbtn = pygame.transform.scale(settingsbtn, (90, 75))

    def draw_img(img, x ,y):
        screen.blit(img, (x, y))

    class Button:
        def __init__(self, x, y, img, scale):
            width = img.get_width()
            height = img.get_height()
            self.image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):

            action = False

            #get mouse position
            pos = pygame.mouse.get_pos()

            #check if the mouse is over the button
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            #if the mouse is not clicked, set the clicked variable to False
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            screen.blit(self.image, (self.rect.x, self.rect.y))

            return action

    start_button =  Button(centerx - startbtn.get_width() / 2 , centery - startbtn.get_height() / 0.9, startbtn, 1)
    load_button = Button(centerx - loadbtn.get_width() / 2 , centery + startbtn.get_height() / 2.2, loadbtn, 1)
    quit_button = Button (centerx - quitbtn.get_width() / 2 , centery + startbtn.get_height() * 2.4, quitbtn, 1)
    settings_button = Button(screen.get_width() - settingsbtn.get_width() - 10, 10, settingsbtn, 1)


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

        if start_button.draw():
            print("start")
        if load_button.draw():
            print("load")
        if quit_button.draw():
            print("quit")
        if settings_button.draw():
            print("settings")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        pygame.display.update()

        clock.tick(60)

    pygame.quit()