from Sounds import get_damage_sound, pygame


class IGetDamage:
    def __init__(self, health):
        self.health = health

    def get_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            pygame.mixer.Sound.play(get_damage_sound)
