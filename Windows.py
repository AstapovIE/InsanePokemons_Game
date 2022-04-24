import pygame.mouse
from pygame import *

init()

size = (800, 600)

screen = display.set_mode(size)

ARIAL_50 = font.SysFont('arial', 50)

button_sound = pygame.mixer.Sound('sounds/button.wav')


def print_text(message, x, y, font_color=(0, 0, 0), font = ARIAL_50):
    text = font.render(message, True, font_color)
    screen.blit(text, (x, y))


class Window:
    def __init__(self):
        self._button_surfaces = []
        self._callbacks = []
        self._current_button_index = 0
        self._gameflag = False
        self._buttons = []

    def append_button(self, button, callback):
        self._button_surfaces.append(ARIAL_50.render(button, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_button_index = max(0, min(self._current_button_index + direction, len(self._button_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_button_index]()

    def draw(self, surf, x, y, button_y_padding):
        for i, button in enumerate(self._button_surfaces):
            button_rect = button.get_rect()
            button_rect.topleft = (x, y + i * button_y_padding)
            if i == self._current_button_index:
                draw.rect(surf, (0, 100, 0), button_rect)
            surf.blit(button, button_rect)


class Button:
    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        self.inactive_color = (13, 162, 58)
        self.active_color = (23, 204, 58)

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300)
                    if action is not None:
                        action()
        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))

        print_text(message, x + 10, y + 10)


menu = Window()
menu.append_button('Играть', lambda: print('Играть'))
menu.append_button('Офнуть помойку', quit)

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
