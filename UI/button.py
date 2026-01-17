import pygame

class Button:
    def __init__(self, x, y, img, scale):
        width = img.get_width()
        height = img.get_height()
        self.image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.active = True

    def draw(self,surface):

        action = False


        # get mouse position
        pos = pygame.mouse.get_pos()

        # check if the mouse is over the button
        if self.active == True:
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
        # if the mouse is not clicked, set the clicked variable to False
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action