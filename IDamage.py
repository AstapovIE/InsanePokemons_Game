import pygame

pygame.init()
hit_sound = pygame.mixer.Sound('sounds/HitSound.mp3')
pygame.mixer.Sound.set_volume(hit_sound, 0.05)

class IDamage:
    def __init__(self, damage):
        self.damage = damage

    def attack(self, mouse):
        if mouse[0]:
            pygame.mixer.Sound.play(hit_sound)


