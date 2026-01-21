import pygame
import copy
import os

from .campfirestate import CampfireState
from .menustate import MenuState
from .overworldstate import OverworldState
from main import party_template
from typing import Any



def mainloop():

    pygame.init()

    current_dir = os.path.dirname(__file__)

    # screen size
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Dino's Adventure")
    clock = pygame.time.Clock()

    # music

    MusicDir = os.path.join(current_dir, "..", "data", "music", "mainsong.mp3")


    current_state = "menu"
    running = True
    party = None
    day = 1
    if current_state == "menu":
        if os.path.exists(MusicDir):
            pygame.mixer.music.load(MusicDir)
            pygame.mixer.music.play(-1, 300, 3000)
            pygame.mixer.music.set_volume(0.1)
        else:
            print("No music found.")

    states: dict[str, Any] = {
        "menu": MenuState(),
    }

    def process_transition(transition):
        nonlocal party, day, current_state, running

        if not transition:
            return None

        action, target = transition
        if action == "switch":
            if target == "overworld":
                if party is None:
                    party = copy.deepcopy(party_template)
                    day = 1

                states["overworld"] = OverworldState(party, day, 1280, 720)
                current_state = "overworld"
            elif target == "menu":
                current_state = "menu"
            elif target == "campfire":
                states["campfire"] = CampfireState(party, day, 1280, 720)
                current_state = "campfire"
                day += 1
            elif target == "load_overworld":

                if party is None:
                    party = copy.deepcopy(party_template)
                    day = 1
                states["overworld"] = OverworldState(party, day, 1280, 720)
                current_state = "overworld"
        elif action == "switch_to_battle":
            from .battlestate import BattleState
            states["battle"] = BattleState(party, target, 1280, 720)
            current_state = "battle"

        elif action == "battle_end":
            target_state = target
            if target_state == "victory":
                from .endofbattlestate import EndOfBattleState
                enemy = states["battle"].enemy
                day += 1
                states["end_of_battle"] = EndOfBattleState(party, enemy, 1280, 720)
                current_state = "end_of_battle"
            else:
                party = None
                day = 1
                current_state = "menu"

        elif action == "quit":
            running = False
            return None
        return None

    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                transition = states[current_state].handle_event(event)
                process_transition(transition)

        transition = states[current_state].update(dt)
        process_transition(transition)

        states[current_state].draw(screen)
        pygame.display.flip()

    pygame.quit()