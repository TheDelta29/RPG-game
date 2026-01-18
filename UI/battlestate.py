import pygame

from main import (
    apply_damage,
    apply_spell_damage,
    use_potion,
    enemy_turn,
    party_is_alive,
    remove_dead,
    spells,
    crits,
    give_loot,
    is_alive,
)

class BattleState:
    def __init__(self, party, enemy, screen_width = 1280, screen_height = 720):
        self.party = party
        self.enemy = enemy
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.actor_i = 0
        self.phase = "CHOOSE_ACTION"
        self.message_log = []
        self.waiting_for_confirm = False
        self.battle_over = False
        self.battle_result = None


        self.font = pygame.font.SysFont("arialblack", 40)
        self.small_font = pygame.font.SysFont("arialblack", 24)
        self.text_color = (255, 255, 255)
        bg = pygame.image.load("data/images/backgrounds/battlebg.png").convert_alpha()
        self.bg = pygame.transform.scale(bg, (screen_width, screen_height))

        self.log(f"A wild {enemy['name']} has appeared!")
        self.log(f"Enemy HP : {enemy["hp"]}/{enemy['max_hp']}")

    def log(self, text):

        self.message_log.append(text)

        if len(self.message_log) > 5:
            self.message_log.pop(0)

    def current_player(self):
        while self.actor_i < len(self.party):
            if is_alive(self.party[self.actor_i]):
                return self.party[self.actor_i]
            self.actor_i += 1
        return None

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return None

        if self.waiting_for_confirm:
            if event.key == pygame.K_RETURN:
                self.waiting_for_confirm = False
                self.advance_turn()
            return None

        player = self.current_player()
        if player is None:
            return None

        if self.phase == "CHOOSE_ACTION":
            if event.key == pygame.K_1:
                self.player_attack(player)
            if event.key == pygame.K_2:
                self.phase = "CHOOSE_SPELL"
            if event.key == pygame.K_3:
                self.phase = "CHOOSE_ITEM"
            if event.key == pygame.K_4:
                self.log(f"{player["name"]} tried to run !")
                self.waiting_for_confirm = True


        elif self.phase == "CHOOSE_SPELL":
            if event.key == pygame.K_1:
                self.cast_spell(player, 0)
            if event.key == pygame.K_2:
                self.cast_spell(player, 1)
            if event.key == pygame.K_3:
                self.phase = "CHOOSE_ACTION"

        elif self.phase == "CHOOSE_ITEM":
            if event.key == pygame.K_1:
                self.use_item(player)
            elif event.key == pygame.K_2:
                self.phase = "CHOOSE_ACTION"
        return None

    def player_attack(self, player):
        dmg = apply_damage(player, self.enemy)
        self.log(f"{player["name"]} has dealt {dmg} to {self.enemy['name']} !")
        self.log(f"{self.enemy["name"]}: {self.enemy["hp"]}/{self.enemy["max_hp"]} HP")

        self.waiting_for_confirm = True

    def cast_spell(self, player, spell_index):
        spell = spells[spell_index]
        if player["mana"] < spell["mana_cost"]:
            self.log(f"{player['name']} doesn't have enough mana !")
            self.waiting_for_confirm = True
            return
        dmg = apply_spell_damage(spell, player, self.enemy)
        self.log(f"{player["name"]} casts {spell['name']} for {dmg} damage !")
        self.log(f"{self.enemy["name"]}: {self.enemy["hp"]}/{self.enemy["max_hp"]} HP")

        self.waiting_for_confirm = True

    def use_item(self, player):
        if use_potion(player, 30):
            self.log(f"{player['name']} has been healed for 30 HP!")
            self.log(f"{player['name']} : {player['hp']}/{player['max_hp']} HP")
        else:
            self.log(f"{player['name']} doesn't have any potions !")
        self.waiting_for_confirm = True

    def advance_turn(self):
        if is_alive(self.enemy):
            enemy_turn(self.enemy, self.party)

        self.actor_i += 1
        if self.actor_i >= len(self.party):
            self.actor_i = 0

        self.phase = "CHOOSE_ACTION"

    def update(self,dt):
        if self.battle_over:
            return None

        if self.enemy["hp"] <= 0:
            self.log(f"{self.enemy["name"]} has been defeated !")
            give_loot(self.party, self.enemy)
            for player in self.party:
                player["mana"] = player["max_mana"]
            self.battle_over = True
            self.battle_result = "victory"
            return ("battle_end", "victory")

        if not party_is_alive(self.party):
            self.log("Party has been defeated !")
            self.battle_over = True
            self.battle_result = "defeat"
            return ("battle_end", "defeat")

        return None

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))

        enemy_text = self.font.render(f"{self.enemy["name"]}: {self.enemy["hp"]}/{self.enemy["max_hp"]} HP", True, (255, 0 ,0 ))
        screen.blit(enemy_text, (50, 50))

        y = 150
        for player in self.party:
            if is_alive(player):
                color = (0, 255 , 0)
            else:
                color = (100, 100 ,100)

            player_text = self.small_font.render(f"{player['name']}: {player['hp']}/{player['max_hp']} HP", True, color)
            screen.blit(player_text, (50, y))
            y += 40

        player = self.current_player()
        if player:
            current_text = self.small_font.render(f">> {player['name']}'s turn <<", True, (255, 255 , 0))
            screen.blit(current_text, (50, y + 40))

        menu_y = 400
        menu_options = []
        if self.phase == "CHOOSE_ACTION":
            menu_options = [
                "1) Attack"
                "2) Cast Spell"
                "3) Use Item"
                "4) Run"
            ]
        elif self.phase == "CHOOSE_SPELL":
            menu_options = [
                f"1) Fireball {spells[0]['mana_cost']} MP"
                f"2) Icequake {spells[1]['mana_cost']} MP"
            ]
        elif self.phase == "CHOOSE_ITEM":
            menu_options = [
                "1) Use Potion"
                "2) Back"
            ]

        for i, option in enumerate(menu_options):
            option_text = self.small_font.render(option, True, self.text_color)
            screen.blit(option_text, (50, menu_y + i * 40))

        log_y = 580

        for msg in self.message_log[-3:]:
            msg_text = self.small_font.render(msg, True, (200,200,200))
            screen.blit(msg_text, (50, log_y))
            log_y += 30

        if self.waiting_for_confirm:
            confirm_text = self.small_font.render("Press ENTER to continue", True, (255,255,0))
            screen.blit(confirm_text, (400, 650))