from Object import *
from IDamage import IDamage
from Bullet import Bullet

pygame.init()
hit_sound = pygame.mixer.Sound('sounds/HitSound.mp3')
pygame.mixer.Sound.set_volume(hit_sound, 0.05)


def if_lkm_pressed(mouse):
    if mouse[0]:
        return True
    return False


class Player(Object, IDamage):
    def __init__(self, x, y, speed, surf, group, damage, setting, obj, my_bullets, spell1, spell2=None):
        super().__init__(x, y, speed, surf, group)
        self.damage = damage
        self.setting = setting
        self.obj = obj
        self.my_bullets = my_bullets
        self.spell1 = spell1
        self.spell2 = spell2

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

    def attack(self, LKM):
        if LKM and self.setting.shoot_timer == 0:
            self.setting.shoot_timer = self.setting.shoot_delay
            pygame.mixer.Sound.play(hit_sound)
            bullet = Bullet(self.rect.centerx, self.rect.centery, self.setting.bullet_speed,
                            pygame.image.load('images/boom.png').convert_alpha(), self.my_bullets, self.get_another())
        if self.setting.shoot_timer > 0:
            self.setting.shoot_timer -= 1

    def update(self):
        keys = pygame.key.get_pressed()
        LKM = if_lkm_pressed(pygame.mouse.get_pressed())

        self.spell1.update(keys, self, self.setting.spell1)
        # self.spell2.update(keys, self, self.setting.spell2)
        self.attack(LKM)

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
        self += vector

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
