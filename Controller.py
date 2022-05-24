from Player import *
from Walls import Wall
from Settings import *
from Spells import *
from Sounds import game_sound




class Controller:
    def __init__(self, FPS, display):

        self.players = pygame.sprite.Group()
        self.static_walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.smokes = pygame.sprite.Group()
        self.stans_images = pygame.sprite.Group()
        self.explosion_images = pygame.sprite.Group()


        self.FPS = FPS
        self.display = display
        self.delta = Vector(0, 0)
        self.vector = Vector(0, 0)

        self.fon_image = pygame.image.load('images/fon.jpg').convert()
        self.display_image = pygame.image.load('images/background.jpg').convert()

        self.objects = self.init_objects()

        self.player = self.init_player()
        self.enemy = self.init_enemy()
        self.filling()

    def init_player(self):
        return Player(450, 225,
                      5,  # speed
                      'pikachu.png',
                      self.players,
                      None,  # enemy
                      20,  # health
                      Setting1(),
                      self.objects,
                      self.bullets,
                      Blink(0, 300, 400),
                      Stan(0, 300, 400, 40, 300, self.stans_images, None),
                      Explosion(0, 600, 150, 10, 100, 20, self.explosion_images))

    def init_enemy(self):
        return Player(910, 400,
                      5,  # speed
                      'bulbazavr.png',
                      self.players,
                      None,  # enemy
                      10,  # health
                      Setting2(),
                      self.objects,
                      self.bullets,
                      MakeSmoke(0, 600, 300, self.smokes),
                      Stan(0, 600, 400, 40, 300, self.stans_images, None),
                      Explosion(0, 600, 150, 10, 100, 20, self.explosion_images))

    def init_objects(self):
        objects = []
        objects.append(Wall(25, 325, 0, 'vert_wall.jpg', self.static_walls))
        objects.append(Wall(1375, 325, 0, 'vert_wall.jpg', self.static_walls))
        objects.append(Wall(700, 25, 0, 'gor_wall.jpg', self.static_walls))
        objects.append(Wall(700, 625, 0, 'gor_wall.jpg', self.static_walls))
        return objects

    def filling(self):
        self.player.fill_obj(self.objects)
        self.enemy.fill_obj(self.objects)
        self.player.fill_enemy(self.enemy)
        self.enemy.fill_enemy(self.player)
        self.objects.append(self.player)
        self.objects.append(self.enemy)

    def tracking_the_offset(self):
        self.vector = Vector(self.player.rect.x, self.player.rect.y)
        self.players.update()
        self.vector -= self.player
        self.player += self.vector
        self.delta += self.vector

    def run_game(self):
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.display.blit(self.fon_image, (0, 0))
            self.display.blit(self.display_image, (self.delta.x, self.delta.y))
            # drawing
            self.bullets.draw(self.display)
            self.players.draw(self.display)
            self.smokes.draw(self.display)
            self.static_walls.draw(self.display)
            self.stans_images.draw(self.display)
            self.explosion_images.draw(self.display)

            # отслеживаем смещение главного игрока
            self.tracking_the_offset()
            # moving other
            self.enemy.move_on_vector(self.vector)
            # updating objects
            self.static_walls.update(self.vector)
            self.bullets.update(self.enemy, self.vector)
            self.smokes.update(self.vector)
            self.stans_images.update(self.vector)
            self.explosion_images.update()

            pygame.display.update()
            self.FPS.tick(60)

