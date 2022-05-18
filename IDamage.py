class IDamage:
    def __init__(self, damage):
        self.damage = damage

    def do_damage(self, target):
        target.health -= self.damage
