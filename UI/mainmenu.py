import pygame
from . import button


def mainloop():

    pygame.init()

    #screen size
    screen = pygame.display.set_mode((1280, 720))

    centerx , centery = screen.get_rect().centerx , screen.get_rect().centery

    #setting the variable bg to the background image
    bg = pygame.image.load("data/images/dinosadventurebg.png").convert_alpha()
    bg = pygame.transform.scale(bg, (1280, 720))

    #setting startbtn to the button image
    startbtn = pygame.image.load("data/images/buttons/startnewgamebtn.png").convert_alpha()
    startbtn = pygame.transform.scale(startbtn, (350, 100))

    loadbtn = pygame.image.load("data/images/buttons/loadgamebtn.png").convert_alpha()
    loadbtn = pygame.transform.scale(loadbtn, (300, 90))

    quitbtn = pygame.image.load("data/images/buttons/quitbtn.png").convert_alpha()
    quitbtn = pygame.transform.scale(quitbtn, (250, 75))

    settingsbtn = pygame.image.load("data/images/buttons/settingsbtn.png").convert_alpha()
    settingsbtn = pygame.transform.scale(settingsbtn, (90, 75))

    backbtn = pygame.image.load("data/images/buttons/backbtn.png").convert_alpha()
    backbtn = pygame.transform.scale(backbtn, (250, 75))

    audiosettingsbtn = pygame.image.load("data/images/buttons/audiosettingsbtn.png").convert_alpha()
    audiosettingsbtn = pygame.transform.scale(audiosettingsbtn, (300, 90))

    videosettingsbtn = pygame.image.load("data/images/buttons/videosettingsbtn.png").convert_alpha()
    videosettingsbtn = pygame.transform.scale(videosettingsbtn, (300, 90))


    #main menu buttons
    start_button =  button.Button(centerx - startbtn.get_width() / 2 , centery - startbtn.get_height() / 0.9, startbtn, 1)
    load_button = button.Button(centerx - loadbtn.get_width() / 2 , centery + startbtn.get_height() / 5, loadbtn, 1)
    quit_button = button.Button (centerx - quitbtn.get_width() / 2 , centery + startbtn.get_height() / 0.5 , quitbtn, 1)
    settings_button = button.Button(screen.get_width() - settingsbtn.get_width() - 10, 10, settingsbtn, 1)

    #settings menu buttons
    videosettingsbtn = button.Button(centerx - videosettingsbtn.get_width() / 2, centery - startbtn.get_height() / 0.9,videosettingsbtn, 1)
    audiosettingsbtn = button.Button(centerx - audiosettingsbtn.get_width() / 2, centery + startbtn.get_height() / 5 ,audiosettingsbtn, 1)
    back_button = button.Button(centerx - backbtn.get_width() / 2 , centery + startbtn.get_height() / 0.5, backbtn, 1)


    #settings variable
    settingsmenu = False

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

        if settingsmenu:
            start_button.active = False
            load_button.active = False
            quit_button.active = False

            if back_button.draw(screen):
                pygame.time.delay(100)
                settingsmenu = False


            if videosettingsbtn.draw(screen):
                print("video settings")
            if audiosettingsbtn.draw(screen):
                print("audio settings")
        else :
            start_button.active = True
            load_button.active = True
            quit_button.active = True
            if settings_button.draw(screen):
                print("settings")
                settingsmenu = True

            if start_button.draw(screen):
                print("start")
            if load_button.draw(screen):
                print("load")
            if quit_button.draw(screen):
                running = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        pygame.display.update()

        clock.tick(30)

    pygame.quit()