from Object import *
from IDamage import IDamage
from Bullet import Bullet

pygame.init()
hit_sound = pygame.mixer.Sound('sounds/HitSound.mp3')
pygame.mixer.Sound.set_volume(hit_sound, 0.05)


def check_distance(x0, y0, x, y, kef):  # ищет расстояние между двумя точками и сравнивает его с коэфициентом
    if ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5 < kef:
        return True
    return False


class Player(Object, IDamage):
    def __init__(self, x, y, speed, surf, group, damage, shoot_timer, shoot_delay, setting, obj, my_bullets):
        super().__init__(x, y, speed, surf, group)
        self.damage = damage
        self.shoot_timer = shoot_timer
        self.shoot_delay = shoot_delay
        self.setting = setting
        self.obj = obj
        self.my_bullets = my_bullets

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
        if keys[self.setting.spell1] and check_distance(start[0], start[1], pos[0], pos[1], blink_kef):
            self.rect.centerx = pos[0]
            self.rect.centery = pos[1]
            if pygame.sprite.spritecollideany(self, self.get_another()):
                self.rect.centerx = start[0]
                self.rect.centery = start[1]

    def attack(self, mouse):
        if mouse[0] and self.shoot_timer == 0:
            self.shoot_timer = self.shoot_delay
            pygame.mixer.Sound.play(hit_sound)
            bullet = Bullet(self.rect.centerx, self.rect.centery, 10,
                            pygame.image.load('images/cash.jpg').convert(), self.my_bullets, self.get_another())
        if self.shoot_timer > 0:
            self.shoot_timer -= 1

    def update(self, width, height):
        keys = pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()
        self.use_spell1(keys)
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
