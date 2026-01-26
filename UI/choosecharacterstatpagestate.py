import pygame
from . import button

class ChooseCharacterStatPageState:
    def __init__(self,party, screen_width = 1280, screen_height = 720):
        self.party = party
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.centerx = screen_width/2
        self.centery = screen_height/2

        self.character1 = False
        self.character2 = False
        self.character3 = False
        self.selectedamount = 0

        bg = pygame.image.load("data/images/backgrounds/statpagebg.png").convert_alpha()
        self.bg = pygame.transform.scale(bg, (screen_width, screen_height))

        # menu buttons
        firstcharacterbutton = pygame.image.load("data/images/buttons/statpage/firstcharacterbutton.png").convert_alpha()
        firstcharacterbutton = pygame.transform.scale(firstcharacterbutton, (300, 90))
        secondcharacterbutton = pygame.image.load("data/images/buttons/statpage/secondcharacterbutton.png").convert_alpha()
        secondcharacterbutton = pygame.transform.scale(secondcharacterbutton, (300, 90))
        thirdcharacterbutton = pygame.image.load("data/images/buttons/statpage/thirdcharacterbutton.png").convert_alpha()
        thirdcharacterbutton = pygame.transform.scale(thirdcharacterbutton, (300, 90))
        backbutton = pygame.image.load("data/images/buttons/mainmenu/backbtn.png").convert_alpha()
        backbutton = pygame.transform.scale(backbutton, (300, 90))

        # stat buttons
        howmanystatstospend = pygame.image.load("data/images/buttons/statpage/howmanystatstospend.png").convert_alpha()
        howmanystatstospend = pygame.transform.scale(howmanystatstospend, (300, 90))
        maxhpbutton = pygame.image.load("data/images/buttons/statpage/maxhpbutton.png").convert_alpha()
        maxhpbutton = pygame.transform.scale(maxhpbutton, (300, 90))
        attackbutton = pygame.image.load("data/images/buttons/statpage/attackbutton.png").convert_alpha()
        attackbutton = pygame.transform.scale(attackbutton, (300, 90))
        defensebutton = pygame.image.load("data/images/buttons/statpage/defensebutton.png").convert_alpha()
        defensebutton = pygame.transform.scale(defensebutton, (300, 90))
        agilitybutton = pygame.image.load("data/images/buttons/statpage/agilitybutton.png").convert_alpha()
        agilitybutton = pygame.transform.scale(agilitybutton, (300, 90))
        intelligencebutton = pygame.image.load("data/images/buttons/statpage/intelligencebutton.png").convert_alpha()
        intelligencebutton = pygame.transform.scale(intelligencebutton, (300, 90))

        # buttons to select the number of points to spend
        minusonebutton = pygame.image.load("data/images/buttons/statpage/minusonebutton.png").convert_alpha()
        minusonebutton = pygame.transform.scale(minusonebutton, (300, 90))
        plusonebutton = pygame.image.load("data/images/buttons/statpage/plusonebutton.png").convert_alpha()
        plusonebutton = pygame.transform.scale(plusonebutton, (300, 90))
        minusfivebutton = pygame.image.load("data/images/buttons/statpage/minustenbutton.png").convert_alpha()
        minusfivebutton = pygame.transform.scale(minusfivebutton, (300, 90))
        plusfivebutton = pygame.image.load("data/images/buttons/statpage/plusfivebutton.png").convert_alpha()
        plusfivebutton = pygame.transform.scale(plusfivebutton, (300, 90))
        removeallpointsbutton = pygame.image.load("data/images/buttons/statpage/removeallpointsbutton.png").convert_alpha()
        removeallpointsbutton = pygame.transform.scale(removeallpointsbutton, (300, 90))
        allpointsbutton = pygame.image.load("data/images/buttons/statpage/allpointsbutton.png").convert_alpha()
        allpointsbutton = pygame.transform.scale(allpointsbutton, (300, 90))
        confirmbutton = pygame.image.load("data/images/buttons/statpage/confirmbutton.png").convert_alpha()
        confirmbutton = pygame.transform.scale(confirmbutton, (300, 90))


        self.firstcharacterbutton = button.Button(self.centerx - firstcharacterbutton.get_width() / 2, 400, firstcharacterbutton, 1)
        self.secondcharacterbutton = button.Button(self.centerx - secondcharacterbutton.get_width() / 2, 600, secondcharacterbutton, 1)
        self.thirdcharacterbutton = button.Button(self.centerx - thirdcharacterbutton.get_width() / 2, 800, thirdcharacterbutton, 1)
        self.backbutton = button.Button(self.centerx - backbutton.get_width() / 2, 1000, backbutton, 1)

        self.minusonebutton = button.Button(self.centerx - minusonebutton.get_width() / 2, 200, minusonebutton, 1)
        self.minusfivebutton = button.Button(self.centerx - minusfivebutton.get_width() / 2, 400, minusfivebutton, 1)
        self.removeallpointsbutton = button.Button(self.centerx - removeallpointsbutton.get_width() / 2, 600, removeallpointsbutton, 1)
        self.plusonebutton = button.Button(self.centerx - plusonebutton.get_width() / 2, 100, plusonebutton, 1)
        self.plusfivebutton = button.Button(self.centerx - plusfivebutton.get_width() / 2, 300, plusfivebutton, 1)
        self.allpointsbutton = button.Button(self.centerx - allpointsbutton.get_width() / 2, 500, allpointsbutton, 1)
        self.confirmbutton = button.Button(self.centerx - confirmbutton.get_width() / 2, 700, confirmbutton, 1)

        self.howmanystatstospend = button.Button(self.centerx - howmanystatstospend.get_width() / 2, 100, howmanystatstospend, 1)
        self.maxhpbutton = button.Button(self.centerx - maxhpbutton.get_width() / 2, 200, maxhpbutton, 1)
        self.attackbutton = button.Button(self.centerx - attackbutton.get_width() / 2, 400, attackbutton, 1)
        self.defensebutton = button.Button(self.centerx - defensebutton.get_width() / 2, 600, defensebutton, 1)
        self.agilitybutton = button.Button(self.centerx - agilitybutton.get_width() / 2, 800, agilitybutton, 1)
        self.intelligencebutton = button.Button(self.centerx - intelligencebutton.get_width() / 2, 1000, intelligencebutton, 1)

    def handle_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return None
        elif self.firstcharacterbutton.rect.collidepoint(event.pos):
            self.character1 = True
        elif self.secondcharacterbutton.rect.collidepoint(event.pos):
            self.character2 = True
        elif self.thirdcharacterbutton.rect.collidepoint(event.pos):
            self.character3 = True
        elif self.backbutton.rect.collidepoint(event.pos) and not (self.character1 or self.character2 or self.character3):
            return ("switch", "overworld")
        elif self.backbutton.rect.collidepoint(event.pos) and (self.character1 or self.character2 or self.character3):
            self.character1 = False
            self.character2 = False
            self.character3 = False
        elif self.plusonebutton.rect.collidepoint(event.pos):
            self.selectedamount += 1
        elif self.plusfivebutton.rect.collidepoint(event.pos):
            self.selectedamount += 5
        elif self.allpointsbutton.rect.collidepoint(event.pos):
            return None # all the players available stat points
        elif self.minusonebutton.rect.collidepoint(event.pos):
            self.selectedamount -= 1
        elif self.minusfivebutton.rect.collidepoint(event.pos):
            self.selectedamount -= 5
        elif self.removeallpointsbutton.rect.collidepoint(event.pos):
            self.selectedamount = 0
        elif self.confirmbutton.rect.collidepoint(event.pos):
            return None # update the players stats with the selected amount and return to the character selection screen
        return None


    def update(self, dt):
        return None

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        if not self.character1 and not self.character2 and not self.character3:
            self.firstcharacterbutton.draw(screen)
            self.secondcharacterbutton.draw(screen)
            self.thirdcharacterbutton.draw(screen)
            self.backbutton.draw(screen)
        elif self.character1 or self.character2 or self.character3:
            self.howmanystatstospend.draw(screen)
            self.minusonebutton.draw(screen)
            self.minusfivebutton.draw(screen)
            self.removeallpointsbutton.draw(screen)
            self.plusonebutton.draw(screen)
            self.plusfivebutton.draw(screen)
            self.allpointsbutton.draw(screen)
            self.maxhpbutton.draw(screen)
            self.attackbutton.draw(screen)
            self.defensebutton.draw(screen)
            self.agilitybutton.draw(screen)
            self.intelligencebutton.draw(screen)
            self.backbutton.draw(screen)
            self.confirmbutton.draw(screen)

