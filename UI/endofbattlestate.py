import pygame
from main import give_loot
from . import button

class EndOfBattleState:
    def __init__(self, party, enemy, screen_width = 1280, screen_height = 720):
        self.party = party
        self.enemy = enemy
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.centerx = screen_width / 2
        self.centery = screen_height / 2
        self.rewardsgiven = False

        bg = pygame.image.load('data/images/backgrounds/battlebg.png').convert_alpha()
        self.bg = pygame.transform.scale(bg, (screen_width, screen_height))

        nextbutton = pygame.image.load('data/images/buttons/campfire/nextbutton.png').convert_alpha()
        nextbutton = pygame.transform.scale(nextbutton, (300, 90))

        self.nextbutton = button.Button(self.centerx - nextbutton.get_width() / 2, 600, nextbutton, 1)

    def handle_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return None

        if not self.rewardsgiven:
            if self.nextbutton.rect.collidepoint(event.pos):
                give_loot(self.party, self.enemy)
                self.rewardsgiven = True
                return None
        else:
            if self.nextbutton.rect.collidepoint(event.pos):
                return ("switch", "overworld")
        return None

    def update(self, dt):
        return None


    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        self.nextbutton.draw(screen)
