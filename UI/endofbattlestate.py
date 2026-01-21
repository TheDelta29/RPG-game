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
        self.gold = None
        self.xp = None

        self.font = pygame.font.Font('data/font/medieval-pixel.ttf',30)

        bg = pygame.image.load('data/images/backgrounds/battlebg.png').convert_alpha()
        self.bg = pygame.transform.scale(bg, (screen_width, screen_height))

        blankbutton = pygame.image.load('data/images/buttons/blanksign.png').convert_alpha()
        blankbutton = pygame.transform.scale(blankbutton, (800, 220))

        summarybutton = pygame.image.load('data/images/buttons/battle/battleendsummary.png').convert_alpha()
        summarybutton = pygame.transform.scale(summarybutton, (300, 90))

        nextbutton = pygame.image.load('data/images/buttons/campfire/nextbutton.png').convert_alpha()
        nextbutton = pygame.transform.scale(nextbutton, (300, 90))

        self.blankbutton = button.Button(self.centerx - blankbutton.get_width() / 2, 330, blankbutton, 1)
        self.nextbutton = button.Button(self.centerx - nextbutton.get_width() / 2, 575, nextbutton, 1)
        self.summarybutton = button.Button(self.centerx - summarybutton.get_width() / 2, 30, summarybutton, 1)

    def handle_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return None

        if not self.rewardsgiven:
            if self.nextbutton.rect.collidepoint(event.pos):
                self.gold, self.xp = give_loot(self.party, self.enemy)
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
        self.summarybutton.draw(screen)

        if self.rewardsgiven:
            self.blankbutton.draw(screen)
            text = self.font.render(f"Each of your characters have gained {self.gold} gold and {self.xp} xp", True, (0, 0, 0))
            x = self.centerx - text.get_width() / 2
            y = 400
            screen.blit(text, (x, y))
