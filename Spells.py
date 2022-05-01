import pygame
from Point import *
from Smoke import Smoke
from StanImage import StanImage


class Spell:
    def __init__(self, timer, cooldown):
        self.timer = timer
        self.cooldown = cooldown


class Blink(Spell):
    def __init__(self, timer, cooldown, range):
        super().__init__(timer, cooldown)
        self.range = range

    def update(self, keys, player, key):
        if keys[key] and self.timer == 0:
            pos = pygame.mouse.get_pos()
            pos_to_blink = Point2D(pos[0], pos[1])  # не смог сделать конструктор на основе кортежа(см Point.py)
            start_pos = Vector(player.rect.centerx, player.rect.centery)
            distance = start_pos.calculate_distance(pos_to_blink)

            if distance <= self.range:
                self.timer = self.cooldown
                player.rect.centerx = pos_to_blink.x
                player.rect.centery = pos_to_blink.y
                if pygame.sprite.spritecollideany(player, player.get_another()):
                    player.rect.centerx = start_pos.x
                    player.rect.centery = start_pos.y
        if self.timer > 0:
            self.timer -= 1


class MakeSmoke(Spell):
    def __init__(self, timer, cooldown, life_time, group):
        super().__init__(timer, cooldown)
        self.life_time = life_time
        self.group = group

    def update(self, keys, player, key):
        if keys[key] and self.timer == 0:
            smoke = Smoke(player.rect.centerx, player.rect.centery,
                          pygame.image.load('images/smoke.png').convert_alpha(),
                          self.group, self.life_time)
            self.timer = self.cooldown
        if self.timer > 0:
            self.timer -= 1

class MakeShield(Spell):
    def __init__(self, timer, cooldown, life_time):
        super().__init__(timer, cooldown)
        self.life_time = life_time

class Stan(Spell):
    def __init__(self, timer, cooldown, range, activate_time, stan_time, group, stan_image):
        super().__init__(timer, cooldown)
        self.range = range
        self.activate_time = activate_time
        self.stan_time = stan_time
        self.group = group
        self.stan_image = stan_image

    def update(self, keys, player, key, target):

        if keys[key] and self.timer == 0:
            pos = pygame.mouse.get_pos()
            pos_to_draw = Point2D(pos[0], pos[1])  # не смог сделать конструктор на основе кортежа(см Point.py)
            start_pos = Vector(player.rect.centerx, player.rect.centery)
            distance = start_pos.calculate_distance(pos_to_draw)

            if distance <= self.range:

                stan_image = StanImage(pos_to_draw.x, pos_to_draw.y,
                              pygame.image.load('images/stan.png').convert_alpha(),
                              self.group, self.activate_time)
                self.stan_image = stan_image

            self.timer = self.cooldown

        if isinstance(self.stan_image, StanImage) and self.timer+1 == self.cooldown - self.activate_time:
            if pygame.sprite.collide_rect(self.stan_image, target):
                self.stan_image.do_stan(target, self.stan_time)
                self.stan_image = None

        if self.timer > 0:
            self.timer -= 1



