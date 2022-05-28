from Controller import Controller
from Object import pygame
from Window import Window, get_font
from Button import Button

FPS = pygame.time.Clock()

display_width = 1400  # 1400
display_height = 650  # 650
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('InsanePokemons')

controller = Controller(FPS, display)

MENU_BG = pygame.image.load("images/backg.jpg")
OPTIONS_BG = pygame.image.load("images/Optionsbg.jpg")
MENU_COLOR = "#b68f40"
OPTIONS_COLOR = "white"

MENU = Window("MAIN MENU", 100, MENU_COLOR, 700, 100, MENU_BG, display)
OPTIONS = Window("Отожмись 10 раз или я заберу твою душу", 35, OPTIONS_COLOR, 700, 260, OPTIONS_BG, display)

PLAY_BUTTON = Button(image=pygame.image.load("images/play_rect.jpg"), pos=(700, 250),
                                text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White", run_window = controller.run_game)
OPTIONS_BUTTON = Button(image=pygame.image.load("images/options_rect.jpg"), pos=(700, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White", run_window = OPTIONS.start)
QUIT_BUTTON = Button(image=pygame.image.load("images/quit_rect.jpg"), pos=(700, 550),
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White", run_window = pygame.quit)
BACK_BUTTON = Button(image=None, pos=(700, 460),
                                text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green", run_window = MENU.start)

MENU.append_button(PLAY_BUTTON)
MENU.append_button(OPTIONS_BUTTON)
MENU.append_button(QUIT_BUTTON)
OPTIONS.append_button(BACK_BUTTON)
