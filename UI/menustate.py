import pygame
from . import button

class MenuState:
    def __init__(self, screen_width = 1280, screen_height = 720):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.centerx = screen_width/2
        self.centery = screen_height/2
        self.in_settings = False

        # setting the variable bg to the background image
        bg = pygame.image.load("data/images/backgrounds/dinosadventurebg.png").convert_alpha()
        self.bg = pygame.transform.scale(bg, (screen_width, screen_height))

        # setting startbtn to the button image
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

        # main menu buttons
        self.start_button = button.Button(self.centerx - startbtn.get_width() / 2, self.centery - startbtn.get_height() / 0.9, startbtn, 1)
        self.load_button = button.Button(self.centerx - loadbtn.get_width() / 2, self.centery + startbtn.get_height() / 5, loadbtn, 1)
        self.quit_button = button.Button(self.centerx - quitbtn.get_width() / 2, self.centery + startbtn.get_height() / 0.5, quitbtn, 1)
        self.settings_button = button.Button(self.screen_width - settingsbtn.get_width() - 10, 10, settingsbtn, 1)

        # settings menu buttons
        self.videosettingsbtn = button.Button(self.centerx - videosettingsbtn.get_width() / 2, self.centery - startbtn.get_height() / 0.9, videosettingsbtn, 1)
        self.audiosettingsbtn = button.Button(self.centerx - audiosettingsbtn.get_width() / 2, self.centery + startbtn.get_height() / 5, audiosettingsbtn, 1)
        self.back_button = button.Button(self.centerx - backbtn.get_width() / 2, self.centery + startbtn.get_height() / 0.5, backbtn, 1)

    def handle_event(self, event):

        if event.type != pygame.MOUSEBUTTONDOWN:
            return None

        if self.in_settings:

            if self.back_button.rect.collidepoint(event.pos):
                pygame.time.delay(100)
                self.in_settings = False

            if self.videosettingsbtn.rect.collidepoint(event.pos):
                print("video settings")

            if self.audiosettingsbtn.rect.collidepoint(event.pos):
                print("audio settings")

        else :

            if self.settings_button.rect.collidepoint(event.pos):
                self.in_settings = True

            if self.start_button.rect.collidepoint(event.pos):
                return("switch", "overworld")

            if self.load_button.rect.collidepoint(event.pos):
                return("switch", "load_overworld")

            if self.quit_button.rect.collidepoint(event.pos):
                return("quit", None)

        return None

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill("black")
        screen.blit(self.bg, (0, 0))

        if self.in_settings:
            self.back_button.draw(screen)
            self.videosettingsbtn.draw(screen)
            self.audiosettingsbtn.draw(screen)

        else:
            self.start_button.draw(screen)
            self.load_button.draw(screen)
            self.quit_button.draw(screen)
            self.settings_button.draw(screen)



