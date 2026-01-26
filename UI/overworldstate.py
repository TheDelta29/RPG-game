import pygame
from main import choose_random_enemy, rest_at_campfire, give_loot, party_is_alive, save_game, load_game
from . import button

class OverworldState:
    def __init__(self, party, day = 1, screen_width = 1280, screen_height = 720):
        self.party = party
        self.day = day
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.centerx = screen_width/2
        self.centery = screen_height/2

        pygame.mixer.music.fadeout(1500)

        self.font = pygame.font.SysFont("arialblack", 40)
        self.small_font = pygame.font.SysFont("arialblack", 24)
        self.text_color = (255, 255, 255)
        bg = pygame.image.load("data/images/backgrounds/overworldbg.png").convert_alpha()
        self.bg = pygame.transform.scale(bg, (screen_width, screen_height))

        battlebutton = pygame.image.load("data/images/buttons/overworld/battlebutton.png").convert_alpha()
        battlebutton = pygame.transform.scale(battlebutton, (300, 90))
        campfirebutton = pygame.image.load("data/images/buttons/overworld/campfirebutton.png").convert_alpha()
        campfirebutton = pygame.transform.scale(campfirebutton, (300, 90))
        villagebutton = pygame.image.load("data/images/buttons/overworld/villagebutton.png").convert_alpha()
        villagebutton = pygame.transform.scale(villagebutton, (300, 90))
        statsbutton = pygame.image.load("data/images/buttons/overworld/playerstatpagebutton.png").convert_alpha()
        statsbutton = pygame.transform.scale(statsbutton, (300, 90))
        savebutton = pygame.image.load("data/images/buttons/overworld/saveandquitbutton.png").convert_alpha()
        savebutton = pygame.transform.scale(savebutton, (300, 90))
        quitwithoutsavingbutton = pygame.image.load("data/images/buttons/overworld/quitwithoutsavingbutton.png").convert_alpha()
        quitwithoutsavingbutton = pygame.transform.scale(quitwithoutsavingbutton, (300, 90))

        self.battlebutton = button.Button(100,50, battlebutton, 1)
        self.campfirebutton = button.Button(100, 150, campfirebutton, 1)
        self.villagebutton = button.Button(100, 250, villagebutton, 1)
        self.statsbutton = button.Button(100, 350, statsbutton, 1)
        self.savebutton = button.Button(100, 450, savebutton, 1)
        self.quitwithoutsavingbutton = button.Button(100, 550, quitwithoutsavingbutton, 1)

        self.message_log = []

    def handle_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return None
        if self.battlebutton.rect.collidepoint(event.pos):
            enemy = choose_random_enemy(self.day)
            return("switch_to_battle", enemy)
        if self.campfirebutton.rect.collidepoint(event.pos):
            return("switch", "campfire")
        if self.villagebutton.rect.collidepoint(event.pos):
            return("switch","village")
        if self.statsbutton.rect.collidepoint(event.pos):
            return("switch", "stats")
        if self.savebutton.rect.collidepoint(event.pos):
            save_game(self.day, self.party)
            self.message_log.append("Game saved!")
            return("switch", "menu")
        if self.quitwithoutsavingbutton.rect.collidepoint(event.pos):
            return("switch", "menu")

        return None

    def update(self, dt):
        if not party_is_alive(self.party):
            return ("switch", "menu")
        return None

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))

        self.battlebutton.draw(screen)
        self.campfirebutton.draw(screen)
        self.villagebutton.draw(screen)
        self.statsbutton.draw(screen)
        self.savebutton.draw(screen)
        self.quitwithoutsavingbutton.draw(screen)

        #
        # day_text = self.font.render(f"Day {self.day}", True , self.text_color)
        # screen.blit(day_text, (20, 20))
        #
        # options = [
        #     "1) Battle",
        #     "2) Rest at Campfire",
        #     "3) Visit village",
        #     "4) Check a player's stat page",
        #     "5) Save & Quit",
        #     "6) Quit without saving"
        # ]
        #
        # y = 150
        # for option in options:
        #     text = self.small_font.render(option, True, self.text_color)
        #     screen.blit(text, (50, y))
        #     y += 60
        #
        # y = 150
        # x = 700
        # for player in self.party:
        #     player_text = self.small_font.render(f"{player["name"]}: {player["hp"]}/{player["max_hp"]} HP", True, self.text_color)
        #     screen.blit(player_text, (x, y))
        #     y += 40

