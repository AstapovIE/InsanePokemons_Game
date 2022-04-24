import pygame.mouse
from pygame import *
from Button import *

class Window:
    def __init__(self, buttons):
        self._button_surfaces = []
        self._callbacks = []
        self._current_button_index = 0
        self._gameflag = False
        self.buttons = buttons

    def append_button(self, button, callback):
        y = 100
        button.draw(20, y, f'button.name')
        y += 50
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


Menu = Window(MenuButtons)
Game = Window(GameButtons)
Pause = Window(PauseButtons)

Menu.append_button(lambda: print('Играть'))
Menu.append_button(quit)

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                Menu.switch(-1)
            elif e.key == K_s:
                Menu.switch(1)
            elif e.key == K_SPACE:
                Menu.select()

    screen.fill((0, 0, 0))

    Menu.draw(screen, 100, 100, 75)

    display.flip()
quit()
