import math
from Object import *
from Damage import Damage
from Walls import BreakableWall


class Bullet(Object, Damage):
    def __init__(self, x, y, speed, surf, group, damage, another_objects, enemy):
        super().__init__(x, y, speed, surf, group)
        Damage.__init__(self, damage)

        self.another_objects = another_objects
        '''calculate_direction'''
        mx, my = pygame.mouse.get_pos()
        self.direction = Vector(mx - x, my - y)
        length = math.hypot(self.direction.x, self.direction.y)
        if length == 0.0:
            self.kill()

        else:
            self.direction = Vector(self.direction.x / length, self.direction.y / length)

        self.enemy = enemy

    def update(self, vector):
        super().update(vector)
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        if pygame.sprite.spritecollideany(self, self.another_objects):
            collided = pygame.sprite.spritecollide(self, self.another_objects, False)
            for obj in collided:
                if type(obj) == type(self.enemy) or type(obj) == BreakableWall:
                    self.do_damage(obj)

            self.kill()

