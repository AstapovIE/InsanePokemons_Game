from Point import *
from Images import *
from IDamage import IDamage

blink_sound = pygame.mixer.Sound('sounds/blink_sound1.mp3')
pygame.mixer.Sound.set_volume(blink_sound, 0.4)

smoke_sound = pygame.mixer.Sound('sounds/smoke_sound.mp3')
pygame.mixer.Sound.set_volume(smoke_sound, 0.4)

ult_sound = pygame.mixer.Sound('sounds/UaA_mem_sound.mp3')
pygame.mixer.Sound.set_volume(ult_sound, 0.4)



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
            pos_to_blink = Point2D(*pos)
            start_pos = Vector(player.rect.centerx, player.rect.centery)
            distance = start_pos.calculate_distance(pos_to_blink)

            if distance <= self.range:
                self.timer = self.cooldown
                pygame.mixer.Sound.play(blink_sound)
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
            pygame.mixer.Sound.play(smoke_sound)
            smoke = SmokeImage(player.rect.centerx, player.rect.centery, 0, 'smoke.png', self.group, self.life_time)
            self.timer = self.cooldown
        if self.timer > 0:
            self.timer -= 1


ex = ['ex1.png', 'ex2.png', 'ex3.png', 'ex4.png', 'ex5.png', 'ex6.png', 'ex7.png', 'ex8.png',
      'ex9.png', 'ex10.png']


class Explosion(Spell, IDamage):
    def __init__(self, timer, cooldown, range, damage, activate_time, delay_for_im, group):
        super().__init__(timer, cooldown)
        self.range = range
        self.damage = damage
        self.activate_time = activate_time
        self.delay_for_im = delay_for_im
        self.group = group
        self.arr_of_im = ex

    def update(self, keys, player, key, target):
        if keys[key] and self.timer == 0:
            pygame.mixer.Sound.play(ult_sound)
            self.timer = self.cooldown

        if self.timer == self.cooldown - self.activate_time:
            p1 = Point2D(player.rect.centerx, player.rect.centery)
            p2 = Point2D(target.rect.centerx, target.rect.centery)
            if self.range > p1.calculate_distance(p2):
                target.get_damage(self.damage)

        if self.cooldown - self.delay_for_im - self.activate_time <= self.timer <= self.cooldown - self.activate_time + self.delay_for_im:
            explosion_image = ExplosionImage(player.rect.centerx, player.rect.centery, 0,
                                             self.arr_of_im[self.timer % 10], self.group, 5)
        if self.timer > 0:
            self.timer -= 1


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
            pos_to_draw = Point2D(*pos)
            start_pos = Vector(player.rect.centerx, player.rect.centery)
            distance = start_pos.calculate_distance(pos_to_draw)

            if distance <= self.range:
                stan_image = StanImage(pos_to_draw.x, pos_to_draw.y, 0, 'stan.png', self.group, self.activate_time)
                self.stan_image = stan_image

            self.timer = self.cooldown

        if self.timer == self.cooldown - self.activate_time:
            if pygame.sprite.collide_rect(self.stan_image, target):
                self.stan_image.do_stan(target, self.stan_time)
                self.stan_image = None

        if self.timer > 0:
            self.timer -= 1
