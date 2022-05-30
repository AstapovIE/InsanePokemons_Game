import sys
import pygame


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)


class Window:
    def __init__(self, text, text_font, text_color, x, y, window_bg, surf):
        self.text = text
        self.buttons = []
        self.text_font = text_font
        self.text_color = text_color
        self.x = x
        self.y = y
        self.window_bg = window_bg
        self.surf = surf

    def append_button(self, button):
        self.buttons.append(button)

    def start(self):

        while True:
            MOUSE_POS = pygame.mouse.get_pos()

            self.surf.blit(self.window_bg, (0, 0))

            TEXT = get_font(self.text_font).render(f'{self.text}', True, self.text_color)
            TEXT_RECT = TEXT.get_rect(center=(self.x, self.y))
            self.surf.blit(TEXT, TEXT_RECT)

            for i in range(len(self.buttons)):
                self.buttons[i].changeColor(MOUSE_POS)
                self.buttons[i].update(self.surf)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.buttons)):
                        if self.buttons[i].checkForInput(MOUSE_POS):
                            self.buttons[i].click()
            pygame.display.update()
