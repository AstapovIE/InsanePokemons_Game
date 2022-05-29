class Damage:
    def __init__(self, damage):
        self.damage = damage

    def do_damage(self, target):
        target.get_damage(self.damage)

