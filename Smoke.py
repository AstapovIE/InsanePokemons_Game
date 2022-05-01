import pygame
from Object import Object


class Smoke(Object):
    def __init__(self, x, y, surf, group, live_time):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)
        self.live_time = live_time

    def update(self, vector):
        super().update(vector)
        self.live_time -= 1
        if self.live_time == 0:
            self.kill()
