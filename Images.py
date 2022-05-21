from Image import Image


class StanImage(Image):
    def __init__(self, x, y, speed, surf, group, life_time):
        super().__init__(x, y, speed, surf, group, life_time)

    def do_stan(self, target, stan_time):
        target.stanned = stan_time


class SmokeImage(Image):
    def __init__(self, x, y, speed, surf, group, life_time):
        super().__init__(x, y, speed, surf, group, life_time)

class ExplosionImage(Image):
    def __init__(self, x, y, speed, surf, group, life_time):
        super().__init__(x, y, speed, surf, group, life_time)

    def update(self):
        self.life_time -= 1
        if self.life_time == 0:
            self.kill()

