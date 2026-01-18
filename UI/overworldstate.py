import pygame
from main import choose_random_enemy, rest_at_campfire, give_loot, party_is_alive, save_game, load_game

class OverworldState:
    def __init__(self, party, day = 1, screen_width = 1280, screen_height = 720):
        self.party = party
        self.day = day
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.font = pygame.font.SysFont("arialblack", 40)
        self.small_font = pygame.font.SysFont("arialblack", 24)
        self.text_color = (255, 255, 255)
        bg = pygame.image.load("data/images/backgrounds/overworldbg.png").convert_alpha()
        self.bg = pygame.transform.scale(bg, (screen_width, screen_height))

        self.message_log = []

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return None
        if event.key == pygame.K_1:
            enemy = choose_random_enemy(self.day)
            return("switch_to_battle", enemy)
        elif event.key == pygame.K_2:
            rest_at_campfire(self.party)
            return None
        elif event.key == pygame.K_3:
            return("switch","village")
        elif event.key == pygame.K_4:
            return("switch", "stats")
        elif event.key == pygame.K_5:
            save_game(self.day, self.party)
            self.message_log.append("Game saved!")
            return None
        elif event.key == pygame.K_6:
            return("switch", "menu")

        return None

    def update(self, dt):
        if not party_is_alive(self.party):
            return ("switch", "menu")
        return None

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))

        day_text = self.font.render(f"Day {self.day}", True , self.text_color)
        screen.blit(day_text, (20, 20))

        options = [
            "1) Battle",
            "2) Rest at Campfire",
            "3) Visit village",
            "4) Check a player's stat page",
            "5) Save & Quit",
            "6) Quit without saving"
        ]

        y = 150
        for option in options:
            text = self.small_font.render(option, True, self.text_color)
            screen.blit(text, (50, y))
            y += 60

        y = 150
        x = 700
        for player in self.party:
            player_text = self.small_font.render(f"{player["name"]}: {player["hp"]}/{player["max_hp"]} HP", True, self.text_color)
            screen.blit(player_text, (x, y))
            y += 40

