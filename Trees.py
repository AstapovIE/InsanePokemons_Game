from Object import Object
from Point import *
import pygame


class Krona(Object):
    def __init__(self, x, y, speed, surf, group):
        super().__init__(x, y, speed, surf, group)


class Stvol(Object):
    def __init__(self, x, y, speed, surf, group):
        super().__init__(x, y, speed, surf, group)


'''class Tree(Object):
    def __init__(self, kronax, kronay, stvolx, stvoly, speed, kronasurf, kronagroup, stvolsurf, stvolgroup):
        self.rect = self.image.get_rect(center=(x, y))
        self.kronax = kronax
        self.kronay = kronay
        self.stvolx = stvolx
        self.stvoly = stvoly
        self.speed = speed
        self.kronasurf = kronasurf
        self.kronagroup = kronagroup
        self.stvolsurf = stvolsurf
        self.stvolgroup = stvolgroup

    def update(self, vector):
        self.rect.x += vector[0]
        self.rect.y += vector[1]'''

class Tree(Object):
    def __init__(self, krona, stvol):
        self.krona = krona
        self.stvol = stvol

class Bush(Object):
    def __init__(self, x, y, speed, surf, group):
        super().__init__(x, y, speed, surf, group)
