from Object import *
from IDamage import IDamage
from Bullet import Bullet
from Smoke import Smoke

pygame.init()
hit_sound = pygame.mixer.Sound('sounds/HitSound.mp3')
pygame.mixer.Sound.set_volume(hit_sound, 0.05)


def if_lkm_pressed(mouse):
    if mouse[0]:
        return True
    return False


class Player(Object, IDamage):
    def __init__(self, x, y, speed, surf, group, damage, setting, obj, my_bullets, my_smokes):
        super().__init__(x, y, speed, surf, group)
        self.damage = damage
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
        pos = pygame.mouse.get_pos()
        pos_to_blink = Point2D(pos[0], pos[1])  #не смог сделать конструктор на основе кортежа(см Point.py)
        start_pos = Vector(self.rect.centerx, self.rect.centery)
        distance = start_pos.calculate_distance(pos_to_blink)

        if keys[self.setting.spell1] and self.setting.blink_timer == 0 and distance <= self.setting.blink_kef:
            self.setting.blink_timer = self.setting.blink_delay
            self.rect.centerx = pos_to_blink.x
            self.rect.centery = pos_to_blink.y
            if pygame.sprite.spritecollideany(self, self.get_another()):
                self.rect.centerx = start_pos.x
                self.rect.centery = start_pos.y
        if self.setting.blink_timer > 0:
            self.setting.blink_timer -= 1

    def use_spell2(self, keys):
        if keys[self.setting.spell2] and self.setting.smoke_timer == 0:
            smoke = Smoke(self.rect.centerx, self.rect.centery, pygame.image.load('images/smoke.png').convert_alpha(),
                          self.my_smokes, self.setting.smoke_life_time)
            self.setting.smoke_timer = self.setting.smoke_delay
        if self.setting.smoke_timer > 0:
            self.setting.smoke_timer -= 1


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

        self.use_spell1(keys)
        self.use_spell2(keys)
        self.attack(LKM)

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
        self += vector

