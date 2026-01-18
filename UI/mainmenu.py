import pygame
import copy
from .menustate import MenuState
from .overworldstate import OverworldState
from main import party_template
from typing import Any


def mainloop():

    pygame.init()

    # screen size
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Dino's Adventure")
    clock = pygame.time.Clock()

    current_state = "menu"
    running = True
    party = None
    day = 1

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
                day += 1
                states["overworld"] = OverworldState(party, day, 1280, 720)
                current_state = "overworld"
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