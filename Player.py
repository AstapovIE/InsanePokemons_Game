from Object import *
from IDamage import IDamage

buttons_dict = {'w': pygame.K_w,
                's': pygame.K_s,
                'a': pygame.K_a,
                'd': pygame.K_d,
                'up': pygame.K_UP,
                'down': pygame.K_DOWN,
                'left': pygame.K_LEFT,
                'right': pygame.K_RIGHT,
                'space': pygame.K_SPACE,
                'l': pygame.K_l,
                'q': pygame.K_q,
                'o': pygame.K_o,
                }


class Settings():
    def __init__(self, up, down, left, right, hit, spell1):
        self.up = buttons_dict[up]
        self.down = buttons_dict[down]
        self.left = buttons_dict[left]
        self.right = buttons_dict[right]
        self.hit = buttons_dict[hit]
        self.spell1 = buttons_dict[spell1]


class Player(Object, IDamage):
    def __init__(self, x, y, speed, surf, group, damage, setting, another_objects):
        super().__init__(x, y, speed, surf, group)
        self.damage = damage
        self.setting = setting
        self.another_objects = another_objects

    def use_spell1(self, display_width, display_height):
        keys = pygame.key.get_pressed()
        blink_kef = 50
        if keys[self.setting.spell1]:
            if keys[self.setting.up]:
                self.rect.y -= blink_kef
                if self.rect.y < 0 or pygame.sprite.spritecollideany(self, self.another_objects):
                    self.rect.y += blink_kef
                    return
            if keys[self.setting.down]:
                self.rect.y += blink_kef
                if self.rect.y > display_height or pygame.sprite.spritecollideany(self, self.another_objects):
                    self.rect.y -= blink_kef
                    return
            if keys[self.setting.left]:
                self.rect.x -= blink_kef
                if self.rect.x < 0 or pygame.sprite.spritecollideany(self, self.another_objects):
                    self.rect.x += blink_kef
                    return
            if keys[self.setting.right]:
                self.rect.x += blink_kef
                if self.rect.x > display_width or pygame.sprite.spritecollideany(self, self.another_objects):
                    self.rect.x -= blink_kef
                    return


    def re_group(self, objects):
        re_objects = []
        for object in objects:
            if self != object:
                re_objects.append(object)
        self.another_objects = re_objects

    def update(self, width, height):
        keys = pygame.key.get_pressed()
        self.attack(self.setting.hit)
        self.use_spell1(1364, 683)
        if keys[self.setting.up]:
            self.rect.y -= self.speed
            if pygame.sprite.spritecollideany(self, self.another_objects):
                self.rect.y += self.speed
            if self.rect.y < 0:
                self.rect.y = 0

        if keys[self.setting.down]:
            self.rect.y += self.speed
            if pygame.sprite.spritecollideany(self, self.another_objects):
                self.rect.y -= self.speed
            if self.rect.y > height - self.rect.height:
                self.rect.y = height - self.rect.height

        if keys[self.setting.left]:
            self.rect.x -= self.speed
            if pygame.sprite.spritecollideany(self, self.another_objects):
                self.rect.x += self.speed
            if self.rect.x < 0:
                self.rect.x = 0

        if keys[self.setting.right]:
            self.rect.x += self.speed
            if pygame.sprite.spritecollideany(self, self.another_objects):
                self.rect.x -= self.speed
            if self.rect.x > width - self.rect.width:
                self.rect.x = width - self.rect.width


'''
        if keys[setting.up]:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0
        if keys[setting.down]:
            self.rect.y += self.speed
            if self.rect.y > height - self.rect.height:
                self.rect.y = height - self.rect.height
        if keys[setting.left]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
        if keys[setting.right]:
            self.rect.x += self.speed
            if self.rect.x > width - self.rect.width:
                self.rect.x = width - self.rect.width'''
