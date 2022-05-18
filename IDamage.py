import pygame
pygame.init()

get_damage_sound = pygame.mixer.Sound('sounds/get_damage_sound.mp3')
pygame.mixer.Sound.set_volume(get_damage_sound, 0.4)

class IDamage:
    def __init__(self, damage):
        self.damage = damage

    def do_damage(self, target):
        target.health -= self.damage
        if target.health > 0:
            pygame.mixer.Sound.play(get_damage_sound)
