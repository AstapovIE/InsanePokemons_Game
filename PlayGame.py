from Controller import Controller
from Object import pygame

FPS = pygame.time.Clock()

display_width = 900  # 1400
display_height = 550  # 650
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('InsanePokemons')

controller = Controller(FPS, display)

controller.run_game()
