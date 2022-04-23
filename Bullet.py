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


    def update(self, tank1, tank2):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        if pygame.sprite.spritecollideany(self, self.another_objects):
            if pygame.sprite.collide_rect(self, tank1):
                tank1.kill()
                for i in range(len(tank1.obj)):
                    if tank1 == tank1.obj[i]:
                        tank1.obj.pop(i)
                        break
                for i in range(len(tank2.another_objects)):
                    if tank1 == tank2.another_objects[i]:
                        tank2.another_objects.pop(i)
                        break
            self.kill()
