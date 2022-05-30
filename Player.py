from Object import *
from Bullet import Bullet
from GetDamage import GetDamage
from Damage import Damage
from Sounds import dead_sound, hit_sound, get_damage_sound


def if_lkm_pressed(mouse):
    if mouse[0]:
        return True
    return False


class Player(Object, GetDamage, Damage):
    def __init__(self, x, y, speed, surf, group, enemies, health, damage, setting, obj, my_bullets, spell1, spell2,
                 spell3, stanned=0):
        Object.__init__(self, x, y, speed, surf, group)
        GetDamage.__init__(self, health)
        Damage.__init__(self, damage)

        self.enemies = []

        self.hit_sound = hit_sound
        self.get_damage_sound = get_damage_sound
        self.dead_sound = dead_sound

        self.setting = setting
        self.obj = obj
        self.my_bullets = my_bullets
        self.spell1 = spell1
        self.spell2 = spell2
        self.spell3 = spell3
        self.stanned = stanned

    def is_dead(self):
        if self.health <= 0:
            self.kill()
            self.del_from_objects()

    def is_stanned(self):
        if self.stanned == 0:
            return False
        self.stanned -= 1
        return True

    def fill_obj(self, objects):
        self.obj = objects

    def fill_enemy(self, enemy):
        self.enemies.append(enemy)

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
            pygame.mixer.Sound.play(self.hit_sound)
            bullet = Bullet(self.rect.centerx, self.rect.centery, self.setting.bullet_speed,
                            'boom.png', self.my_bullets, self.damage,
                            self.get_another(), self.enemies[0])
        if self.setting.shoot_timer > 0:
            self.setting.shoot_timer -= 1

    def update(self):
        self.is_dead()

        if not self.is_stanned():
            keys = pygame.key.get_pressed()
            LKM = if_lkm_pressed(pygame.mouse.get_pressed())

            self.spell1.update(keys, self, self.setting.spell1)
            for i in range(len(self.enemies)):
                self.spell2.update(keys, self, self.setting.spell2, self.enemies[i])
            for j in range(len(self.enemies)):
                self.spell3.update(keys, self, self.setting.spell3, self.enemies[j])
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
