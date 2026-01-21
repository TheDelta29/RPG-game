import pygame

class VillageState:
    def __init__(self, party, screen_width = 1280, screen_height= 720):
        self.party = party
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.centerx = screen_width/2
        self.centery = screen_height/2


    def update(self,dt):
        pass

