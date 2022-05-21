import pygame

pygame.init()

get_damage_sound = pygame.mixer.Sound('sounds/get_damage_sound2.mp3')
pygame.mixer.Sound.set_volume(get_damage_sound, 0.4)


class IGetDamage:
    def __init__(self, health):
        self.health = health

    def get_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            pygame.mixer.Sound.play(get_damage_sound)
