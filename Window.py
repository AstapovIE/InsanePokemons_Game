from pygame import *

init()

size = (800,600)

screen = display.set_mode(size)

ARIAL_50 = font.SysFont('arial', 50)

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0
        self._gameflag = False

    def append_option(self, option, callback):
        self._option_surfaces.append(ARIAL_50.render(option, True, (255,255,255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option,option_rect)


menu = Menu()
menu.append_option('Играть', lambda: print('Играть'))
menu.append_option('Офнуть помойку', quit)


running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                menu.switch(-1)
            elif e.key == K_s:
                menu.switch(1)
            elif e.key == K_SPACE:
                menu.select()

    screen.fill((0, 0, 0))

    menu.draw(screen, 100, 100, 75)

    display.flip()
quit()