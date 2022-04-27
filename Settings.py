import pygame
pygame.init()

class Settings():
    pass

class Setting1(Settings):
    def __init__(self):
        self.up = pygame.K_w
        self.down = pygame.K_s
        self.left = pygame.K_a
        self.right = pygame.K_d
        self.spell1 = pygame.K_q
        self.spell2 = pygame.K_e

class Setting2(Settings):
    def __init__(self):
        self.up = pygame.K_UP
        self.down = pygame.K_DOWN
        self.left = pygame.K_LEFT
        self.right = pygame.K_RIGHT
        self.spell1 = pygame.K_o
        self.spell2 = pygame.K_i
