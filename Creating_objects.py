from Player import *
from Walls import Wall
from Settings import *
from Camera import Camera
from Spells import *
from Trees import *
from Window import Window, get_font
from Button import *
from Controller import Controller

pygame.mixer.music.load('sounds/digidai.mp3')
pygame.mixer.music.set_volume(0.17)

display_width = 1400  # 1400
display_height = 650  # 650
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('InsanePokemons')
#фон за картой
fon = pygame.Surface((1400, 650))
fon_image = pygame.image.load('images/fon.jpg').convert()


camera = Camera(5000, 5000, display_width, display_height)

MENU_BG = pygame.image.load("images/normbackground.jpg")
OPTIONS_BG = pygame.image.load("images/Optionsbg.png")
MENU_COLOR = "#b68f40"
OPTIONS_COLOR = "white"

MENU = Window("MAIN MENU", 100, MENU_COLOR, 700, 100, MENU_BG, display)
OPTIONS = Window("This is the options screen", 45, OPTIONS_COLOR, 700, 260, OPTIONS_BG, display)

PLAY_BUTTON = Button(image=pygame.image.load("images/Play Rect.png"), pos=(700, 250),
                                text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White", run_window = Controller.run_game)
OPTIONS_BUTTON = Button(image=pygame.image.load("images/Options Rect.png"), pos=(700, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White", run_window = OPTIONS.start)
QUIT_BUTTON = Button(image=pygame.image.load("images/Quit Rect.png"), pos=(700, 550),
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White", run_window = pygame.quit)
BACK_BUTTON = Button(image=None, pos=(700, 460),
                                text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green", run_window = MENU.start)

players_images = ['pikachu.png', 'bulbazavr.png']
player_surf = [pygame.image.load('images/' + i).convert_alpha() for i in players_images]
walls_images = ['vert_wall.jpg', 'gor_wall.jpg']
wall_surf = [pygame.image.load('images/' + i).convert() for i in walls_images]
krona_images = ['Krona1.png']
krona_surf = [pygame.image.load('images/' + i).convert_alpha() for i in krona_images]
stvol_images = ['Stvol1.2.png']
stvol_surf = [pygame.image.load('images/' + i).convert_alpha() for i in stvol_images]
bush_images = ['Bush1.png']
bush_surf = [pygame.image.load('images/' + i).convert_alpha() for i in bush_images]


players = pygame.sprite.Group()
static_walls = pygame.sprite.Group()
bullets = pygame.sprite.Group()
smokes = pygame.sprite.Group()
stans_images = pygame.sprite.Group()
kronas = pygame.sprite.Group()
stvols = pygame.sprite.Group()
bushes = pygame.sprite.Group()

blink = Blink(0, 300, 400)
make_smoke = MakeSmoke(0, 600, 300, smokes)
stan1 = Stan(0, 300, 400, 40, 300, stans_images, None)
stan2 = Stan(0, 600, 400, 40, 300, stans_images, None)
pika = Player(display_width/2, display_height/2, 5, player_surf[0], players, None, 5, Setting1(), [],
              bullets, blink, stan1)


bulba = Player(910, 400, 5, player_surf[1], players, None, 5, Setting2(), [], bullets, make_smoke, stan2)

# left_border = Wall(25, 325, 0, wall_surf[0], static_walls)
# right_border = Wall(1375, 325, 0, wall_surf[0], static_walls)
# up_border = Wall(700, 25, 0, wall_surf[1], static_walls)
# down_border = Wall(700, 625, 0, wall_surf[1], static_walls)

krona1 = Krona(-100, -100, 0, krona_surf[0], kronas)
stvol1 = Stvol(-112, 9, 0, stvol_surf[0], stvols)
Tree1 = Tree(krona1, stvol1)

Bush1 = Bush(0, 0, 0, bush_surf[0], bushes)

objects = [pika, bulba, Tree1.stvol]

pika.fill_obj(objects)
bulba.fill_obj(objects)
pika.fill_enemy(bulba)
bulba.fill_enemy(pika)