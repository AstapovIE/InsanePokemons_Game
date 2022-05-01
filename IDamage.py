import pygame

pygame.init()
hit_sound = pygame.mixer.Sound('sounds/HitSound.mp3')
pygame.mixer.Sound.set_volume(hit_sound, 0.05)

class IDamage:
    def __init__(self, damage):
        self.damage = damage

    def attack(self, LKM):
        if LKM:
            pygame.mixer.Sound.play(hit_sound)


