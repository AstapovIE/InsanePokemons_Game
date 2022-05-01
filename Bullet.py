import pygame
import math
from Object import Object


class Bullet(Object):
    def __init__(self, x, y, speed, surf, group, another_objects):
        super().__init__(x, y, speed, surf, group)
        self.another_objects = another_objects
        '''calculate_direction'''
        mx, my = pygame.mouse.get_pos()
        self.direction = (mx - x, my - y)
        length = math.hypot(*self.direction)
        if length == 0.0:
            self.kill()

        else:
            self.direction = (self.direction[0] / length, self.direction[1] / length)



    def update(self, pika_to_kill, vector):
        super().update(vector)
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        if pygame.sprite.spritecollideany(self, self.another_objects):
            if pygame.sprite.collide_rect(self, pika_to_kill):
                pika_to_kill.kill()
                pika_to_kill.del_from_objects()
            self.kill()

