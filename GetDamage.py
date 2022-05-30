import pygame


class GetDamage:
    def __init__(self, health):
        self.health = health

    def get_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            pygame.mixer.Sound.play(self.get_damage_sound)
        else:
            pygame.mixer.Sound.play(self.dead_sound)

