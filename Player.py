from Object import *
from IDamage import IDamage
from Bullet import Bullet
from Smoke import Smoke

pygame.init()
hit_sound = pygame.mixer.Sound('sounds/HitSound.mp3')
pygame.mixer.Sound.set_volume(hit_sound, 0.05)


def check_distance(x0, y0, x, y, kef):  # ищет расстояние между двумя точками и сравнивает его с коэфициентом
    if ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5 < kef:
        return True
    return False


class Player(Object, IDamage):
    def __init__(self, x, y, speed, surf, group, damage, shoot_timer, shoot_delay, blink_timer, blink_delay,
                 smoke_timer, smoke_delay, setting, obj, my_bullets, my_smokes):
        super().__init__(x, y, speed, surf, group)
        self.damage = damage
        self.shoot_timer = shoot_timer
        self.shoot_delay = shoot_delay
        self.blink_timer = blink_timer
        self.blink_delay = blink_delay
        self.smoke_timer = smoke_timer
        self.smoke_delay = smoke_delay
        self.setting = setting
        self.obj = obj
        self.my_bullets = my_bullets
        self.my_smokes = my_smokes

    def fill_obj(self, objects):
        self.obj = objects

    def get_another(self):  # возвращает список обьектов, в котором нет самого себя
        re_objects = []
        for object in self.obj:
            if self != object:
                re_objects.append(object)
        return re_objects

    def del_from_objects(self):  # удаляет игрока из глобального списка объектов
        for i in range(len(self.obj)):
            if self == self.obj[i]:
                self.obj.pop(i)
                break

    def use_spell1(self, keys):
        blink_kef = 400
        pos = pygame.mouse.get_pos()
        start = [self.rect.centerx, self.rect.centery]
        if keys[self.setting.spell1] and self.blink_timer == 0 and check_distance(start[0], start[1], pos[0], pos[1],
                                                                                  blink_kef):
            self.blink_timer = self.blink_delay
            self.rect.centerx = pos[0]
            self.rect.centery = pos[1]
            if pygame.sprite.spritecollideany(self, self.get_another()):
                self.rect.centerx = start[0]
                self.rect.centery = start[1]
        if self.blink_timer > 0:
            self.blink_timer -= 1

    def use_spell2(self, keys):
        if keys[self.setting.spell2] and self.smoke_timer == 0:
            smoke = Smoke(self.rect.centerx, self.rect.centery, pygame.image.load('images/smoke.png').convert_alpha(), self.my_smokes, 300)
            self.smoke_timer = self.smoke_delay
        if self.smoke_timer > 0:
            self.smoke_timer -= 1


    def attack(self, mouse):
        if mouse[0] and self.shoot_timer == 0:
            self.shoot_timer = self.shoot_delay
            pygame.mixer.Sound.play(hit_sound)
            bullet = Bullet(self.rect.centerx, self.rect.centery, 10,
                            pygame.image.load('images/boom.png').convert_alpha(), self.my_bullets, self.get_another())
        if self.shoot_timer > 0:
            self.shoot_timer -= 1

    def update(self):
        keys = pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()
        self.use_spell1(keys)
        self.use_spell2(keys)
        self.attack(mouse_pressed)

        '''xy = [0, 0]
        if keys[self.setting.up]:
            xy[1] -= self.speed
        if keys[self.setting.down]:
            xy[1] += self.speed
        if keys[self.setting.left]:
            xy[0] -= self.speed
        if keys[self.setting.right]:
            xy[0] += self.speed
        if not pygame.sprite.spritecollideany(self, self.get_another()):
            self.rect.x += xy[0]
            self.rect.y += xy[1]'''

        if keys[self.setting.up]:
            self.rect.y -= self.speed
            if pygame.sprite.spritecollideany(self, self.get_another()):
                self.rect.y += self.speed

        if keys[self.setting.down]:
            self.rect.y += self.speed
            if pygame.sprite.spritecollideany(self, self.get_another()):
                self.rect.y -= self.speed

        if keys[self.setting.left]:
            self.rect.x -= self.speed
            if pygame.sprite.spritecollideany(self, self.get_another()):
                self.rect.x += self.speed

        if keys[self.setting.right]:
            self.rect.x += self.speed
            if pygame.sprite.spritecollideany(self, self.get_another()):
                self.rect.x -= self.speed

    def move_on_vector(self, vector):
        self.rect.x += vector[0]
        self.rect.y += vector[1]
