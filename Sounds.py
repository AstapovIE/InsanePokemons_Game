import pygame

pygame.init()

get_damage_sound = pygame.mixer.Sound('sounds/get_damage_sound2.mp3')
pygame.mixer.Sound.set_volume(get_damage_sound, 0.4)

game_sound = pygame.mixer.music.load('sounds/digidai.mp3')
pygame.mixer.music.set_volume(0.17)

blink_sound = pygame.mixer.Sound('sounds/blink_sound1.mp3')
pygame.mixer.Sound.set_volume(blink_sound, 0.4)

smoke_sound = pygame.mixer.Sound('sounds/smoke_sound.mp3')
pygame.mixer.Sound.set_volume(smoke_sound, 0.4)

ult_sound = pygame.mixer.Sound('sounds/UaA_mem_sound.mp3')
pygame.mixer.Sound.set_volume(ult_sound, 0.4)

hit_sound = pygame.mixer.Sound('sounds/HitSound.mp3')
pygame.mixer.Sound.set_volume(hit_sound, 0.25)

dead_sound = pygame.mixer.Sound('sounds/dead_sound.mp3')
pygame.mixer.Sound.set_volume(dead_sound, 0.25)
