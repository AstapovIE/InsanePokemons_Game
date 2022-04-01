from Object import Object
from IDamage import DamageObject


class SpikeWall(Object, DamageObject):
    def __init__(self, name, coordinates, size, image, damage):
        super().__init__(name, coordinates, size, image)
        DamageObject.__init__(self, damage)