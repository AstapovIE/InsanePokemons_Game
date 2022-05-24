import pygame

pygame.init()

get_damage_sound = pygame.mixer.Sound('sounds/get_damage_sound2.mp3')
pygame.mixer.Sound.set_volume(get_damage_sound, 0.4)

game_sound = pygame.mixer.music.load('sounds/digidai.mp3')
pygame.mixer.music.set_volume(0.17)