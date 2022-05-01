import pygame
import math
from Object import *


class Bullet(Object):
    def __init__(self, x, y, speed, surf, group, another_objects):
        super().__init__(x, y, speed, surf, group)
        self.another_objects = another_objects
        '''calculate_direction'''
        mx, my = pygame.mouse.get_pos()
        self.direction = Vector(mx - x, my - y)
        length = math.hypot(self.direction.x, self.direction.y)
        if length == 0.0:
            self.kill()

        else:
            self.direction = Vector(self.direction.x / length, self.direction.y / length)



    def update(self, pika_to_kill, vector):
        super().update(vector)
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        if pygame.sprite.spritecollideany(self, self.another_objects):
            if pygame.sprite.collide_rect(self, pika_to_kill):
                pika_to_kill.kill()
                pika_to_kill.del_from_objects()
            self.kill()

