import pygame
from Object import *
from Player import *
from Walls import Wall

pygame.init()
pygame.mixer.music.load('sounds/digidai.mp3')
pygame.mixer.music.set_volume(0.17)

setting1 = Settings('w', 's', 'a', 'd', 'space', 'q')
setting2 = Settings('up', 'down', 'left', 'right', 'l', 'o')

display_width = 1400
display_height = 650
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('InsanePokemons')
display_image = pygame.image.load('images/background.jpg').convert()

players_images = ['tank1.png', 'tank2.png']
player_surf = [pygame.image.load('images/' + i).convert_alpha() for i in players_images]
walls_images = ['vert_wall.jpg', 'gor_wall.jpg']
wall_surf = [pygame.image.load('images/' + i).convert() for i in walls_images]

players = pygame.sprite.Group()
static_walls = pygame.sprite.Group()

tank1 = Player(500, 350, 5, player_surf[0], players, 777, setting1, [])
tank2 = Player(910, 400, 5, player_surf[1], players, 777, setting2, [])
left_border = Wall(25, 325, 0, wall_surf[0], static_walls)
right_border = Wall(1375, 325, 0, wall_surf[0], static_walls)
up_border = Wall(700, 25, 0, wall_surf[1], static_walls)
down_border = Wall(700, 625, 0, wall_surf[1], static_walls)

objects = [tank1, tank2, left_border, right_border, up_border, down_border]
tank1.re_group(objects)
tank2.re_group(objects)

FPS = pygame.time.Clock()


def run_game():
    game = True
    #pygame.mixer.music.play(-1)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(display_image, (0, 0))
        players.draw(display)
        static_walls.draw(display)

        players.update(display_width, display_height)

        pygame.display.update()
        FPS.tick(60)


run_game()
