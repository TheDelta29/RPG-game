import pygame
from main import give_loot
from . import button

class EndOfBattleState:
    def __init__(self, party, day, screen_width = 1280, screen_height = 720):
        self.party = party
        self.day = day
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.centerx = screen_width / 2
        self.centery = screen_height / 2
        self.rewardsgiven = False

        bg = pygame.image.load('placeholder').convert_alpha()
        self.bg = pygame.transform.scale(bg, (screen_width, screen_height))

        nextbutton = pygame.image.load('placeholder').convert_alpha()
        nextbutton = pygame.transform.scale(nextbutton, (300, 90))

        self.nextbutton = button.Button(self.centerx - nextbutton.get_width() / 2, 600, nextbutton, 1)

    def handle_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return None

        if self.rewardsgiven:
            if self.nextbutton.rect.collidepoint(event.pos):
                give_loot(self.party, self.day)
                rewardsgiven = True
                return None
        else:
            return ("switch", "overworld")
        return None

    def update(self, dt):
        return None


    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.nextbutton.draw(screen)
