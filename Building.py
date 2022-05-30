from Object import Object


class Building(Object):
    def __init__(self, x, y, speed, surf, group):
        super().__init__(x, y, speed, surf, group)