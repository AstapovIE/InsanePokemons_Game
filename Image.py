from Object import *

class Image(Object):
    def __init__(self, x, y, speed, surf, group, life_time):
        super().__init__(x, y, speed, surf, group)
        self.life_time = life_time

    def update(self, vector):
        super().update(vector)
        self.life_time -= 1
        if self.life_time == 0:
            self.kill()