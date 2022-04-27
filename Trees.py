from Object import Object
import pygame


class Tree(Object):
    def __init__(self, x, y, speed, surf, group):
        super().__init__(x, y, speed, surf, group)

    def update(self, vector):
        self.rect.x += vector[0]
        self.rect.y += vector[1]