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


def check_distance(x0, y0, x, y, kef):
    if ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5 < kef:
        return True
    return False


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

    def use_spell1(self, display_width, display_height, keys):
        blink_kef = 400
        pos = pygame.mouse.get_pos()
        start = [self.rect.centerx, self.rect.centery]
        if keys[self.setting.spell1] and check_distance(start[0], start[1], pos[0], pos[1], blink_kef):
            self.rect.centerx = pos[0]
            self.rect.centery = pos[1]
            if pygame.sprite.spritecollideany(self, self.another_objects):
                self.rect.centerx = start[0]
                self.rect.centery = start[1]

    def re_group(self, objects):
        re_objects = []
        for object in objects:
            if self != object:
                re_objects.append(object)
        self.another_objects = re_objects

    def update(self, width, height):
        keys = pygame.key.get_pressed()
        # mouse_pressed = pygame.mouse.get_pressed()
        self.attack(self.setting.hit, keys)
        self.use_spell1(1400, 650, keys)
        if keys[self.setting.up]:
            self.rect.y -= self.speed
            if pygame.sprite.spritecollideany(self, self.another_objects):
                self.rect.y += self.speed

        if keys[self.setting.down]:
            self.rect.y += self.speed
            if pygame.sprite.spritecollideany(self, self.another_objects):
                self.rect.y -= self.speed

        if keys[self.setting.left]:
            self.rect.x -= self.speed
            if pygame.sprite.spritecollideany(self, self.another_objects):
                self.rect.x += self.speed

        if keys[self.setting.right]:
            self.rect.x += self.speed
            if pygame.sprite.spritecollideany(self, self.another_objects):
                self.rect.x -= self.speed
