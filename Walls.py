from Object import Object
from IGetDamage import IGetDamage
from Sounds import break_wall_sound, dead_wall_sound


class Wall(Object):
    def __init__(self, x, y, speed, surf, group):
        super().__init__(x, y, speed, surf, group)


class BreakableWall(Wall, IGetDamage):
    def __init__(self, x, y, speed, surf, group, health, obj):
        super().__init__(x, y, speed, surf, group)
        self.health = health
        self.get_damage_sound = break_wall_sound
        self.dead_sound = dead_wall_sound
        self.obj = obj

    def update(self, vector):
        super().update(vector)
        self.is_dead()

    def is_dead(self):
        if self.health < 0:
            self.kill()
            self.del_from_objects()

    def del_from_objects(self):  # удаляет из глобального списка объектов
        for i in range(len(self.obj)):
            if self == self.obj[i]:
                self.obj.pop(i)
                break
