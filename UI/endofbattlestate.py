import pygame

class EndOfBattleState:
    def __init__(self, party, day, screen_width = 1280, screen_height = 720):
        self.party = party
        self.day = day
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.centerx = screen_width / 2
        self.centery = screen_height / 2
