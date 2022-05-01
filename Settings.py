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
        self.shoot_timer = 0
        self.shoot_delay = 60
        self.bullet_speed = 10
        self.spell1 = pygame.K_q #blink
        self.blink_timer = 0
        self.blink_delay = 300
        self.blink_kef = 400
        self.spell2 = pygame.K_e #smoke
        self.smoke_timer = 0
        self.smoke_delay = 600
        self.smoke_life_time = 300

class Setting2(Settings):
    def __init__(self):
        self.up = pygame.K_UP
        self.down = pygame.K_DOWN
        self.left = pygame.K_LEFT
        self.right = pygame.K_RIGHT
        self.shoot_timer = 0
        self.shoot_delay = 30
        self.bullet_speed = 10
        self.spell1 = pygame.K_o #blink
        self.blink_timer = 0
        self.blink_timer = 0
        self.blink_delay = 300
        self.blink_kef = 400
        self.spell2 = pygame.K_i #smoke
        self.smoke_timer = 0
        self.smoke_delay = 600
        self.smoke_life_time = 300
