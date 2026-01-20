import pygame
from main import rest_at_campfire
from . import button

class CampfireState:
    def __init__(self, party, day, screen_width, screen_height):
        self.party = party
        self.day = day
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.centerx = screen_width/2
        self.centery = screen_height/2
        self.heal = False

        bg = pygame.image.load("data/images/backgrounds/campfirebg.png").convert_alpha()
        self.bg = pygame.transform.scale(bg, (screen_width, screen_height))

        nextbutton = pygame.image.load("data/images/buttons/campfire/nextbutton.png").convert_alpha()
        nextbutton = pygame.transform.scale(nextbutton, (300, 90))

        healbutton = pygame.image.load("data/images/buttons/campfire/campfireheal.png").convert_alpha()
        healbutton = pygame.transform.scale(healbutton, (520, 200))

        self.nextbutton = button.Button(self.centerx - nextbutton.get_width() / 2, 600, nextbutton, 1)
        self.healbutton = button.Button(self.centerx - healbutton.get_width() / 2, 200, healbutton, 1)


    def handle_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return None

        if not self.heal:
            if self.nextbutton.rect.collidepoint(event.pos):
                rest_at_campfire(self.party)
                self.heal = True
                return None
        else:
            return("switch", "overworld")
        return None

    def update(self, dt):
        return None

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        self.nextbutton.draw(screen)

        if self.heal:
            self.healbutton.draw(screen)

