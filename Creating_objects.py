from Player import *
from Walls import Wall
from Settings import *

pygame.mixer.music.load('sounds/digidai.mp3')
pygame.mixer.music.set_volume(0.17)

#setting1 = Setting1()
#etting2 = Setting2()

display_width = 1400
display_height = 650
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('InsanePokemons')
display_image = pygame.image.load('images/background.jpg').convert()

players_images = ['pikachu.png', 'bulbazavr.png']
player_surf = [pygame.image.load('images/' + i).convert_alpha() for i in players_images]
walls_images = ['vert_wall.jpg', 'gor_wall.jpg']
wall_surf = [pygame.image.load('images/' + i).convert() for i in walls_images]


players = pygame.sprite.Group()
static_walls = pygame.sprite.Group()
bullets = pygame.sprite.Group()

pika = Player(500, 350, 5, player_surf[0], players, 777, 0, 60, 0, 300, Setting1(), [], bullets)
bulba = Player(910, 400, 5, player_surf[1], players, 777, 0, 30, 0 , 300, Setting2(), [], bullets)

left_border = Wall(25, 325, 0, wall_surf[0], static_walls)
right_border = Wall(1375, 325, 0, wall_surf[0], static_walls)
up_border = Wall(700, 25, 0, wall_surf[1], static_walls)
down_border = Wall(700, 625, 0, wall_surf[1], static_walls)


objects = [pika, bulba, left_border, right_border, up_border, down_border]

pika.fill_obj(objects)
bulba.fill_obj(objects)