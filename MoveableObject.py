import pygame
from Object import Object
display = pygame.display.set_mode((800, 600))


class MoveableObject(Object):
    def __init__(self, name, coordinates, size, image, speed, buttons=None):
        super().__init__(name, coordinates, size, image)
        self.speed = speed
        self.buttons = buttons

#localkeys
#enum