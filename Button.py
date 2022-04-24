import pygame.mouse
from pygame import *

init()
size = (800, 600)
screen = display.set_mode(size)
ARIAL_50 = font.SysFont('arial', 50)
button_sound = pygame.mixer.Sound('sounds/button.wav')


def print_text(message, x, y, font_color=(0, 0, 0), font =ARIAL_50):
    text = font.render(message, True, font_color)
    screen.blit(text, (x, y))


class Button:
    def __init__(self, name, width, height):
        self.name = name
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

play = Button(100, 50, 'Играть')
settings = Button(100, 50, 'Настройки')
pause = Button(100, 50, 'Пауза')
Quit = Button(100, 50, 'Офнуть')
mainmenu = Button(100, 50, 'Главное меню')

MenuButtons = []
MenuButtons.append(play)
MenuButtons.append(settings)
MenuButtons.append(Quit)

GameButtons = []
GameButtons.append(pause)
GameButtons.append(settings)

PauseButtons = []
PauseButtons.append(play)
PauseButtons.append(mainmenu)