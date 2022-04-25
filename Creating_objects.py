from Player import *
from Walls import Wall
from Settings import *
from Camera import Camera

pygame.mixer.music.load('sounds/digidai.mp3')
pygame.mixer.music.set_volume(0.17)

display_width = 900  # 1400
display_height = 550  # 650
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('InsanePokemons')
display_image = pygame.image.load('images/background.jpg').convert()
#фон за картой
fon = pygame.Surface((2000, 2000))
fon_image = pygame.image.load('images/fon.jpg').convert()

camera = Camera(0, 0, display_width, display_height)

players_images = ['pikachu.png', 'bulbazavr.png']
player_surf = [pygame.image.load('images/' + i).convert_alpha() for i in players_images]
walls_images = ['vert_wall.jpg', 'gor_wall.jpg']
wall_surf = [pygame.image.load('images/' + i).convert() for i in walls_images]

players = pygame.sprite.Group()
static_walls = pygame.sprite.Group()
bullets = pygame.sprite.Group()
smokes = pygame.sprite.Group()

pika = Player(display_width / 2, display_height / 2, 5, player_surf[0], players, 777, 0, 60, 0, 300, 0, 600, Setting1(), [],
              bullets, smokes)
bulba = Player(910, 400, 5, player_surf[1], players, 777, 0, 30, 0, 300, 0, 600, Setting2(), [], bullets, smokes)

left_border = Wall(25, 325, 0, wall_surf[0], static_walls)
right_border = Wall(1375, 325, 0, wall_surf[0], static_walls)
up_border = Wall(700, 25, 0, wall_surf[1], static_walls)
down_border = Wall(700, 625, 0, wall_surf[1], static_walls)

objects = [pika, bulba, left_border, right_border, up_border, down_border]

pika.fill_obj(objects)
bulba.fill_obj(objects)
