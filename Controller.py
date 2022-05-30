from Player import *
from Walls import *
from Building import Building
from Settings import *
from Spells import *
from Nature import *

pygame.mixer.music.load('sounds/game_sound.mp3')
pygame.mixer.music.set_volume(0.05)


class Controller:
    def __init__(self, FPS, display):

        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.breakeable_walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.smokes = pygame.sprite.Group()
        self.stans_images = pygame.sprite.Group()
        self.explosion_images = pygame.sprite.Group()
        self.bushes = pygame.sprite.Group()
        self.lakes = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()
        self.trunks = pygame.sprite.Group()
        self.crowns = pygame.sprite.Group()

        self.FPS = FPS
        self.display = display
        self.delta = Vector(0, 0)
        self.vector = Vector(0, 0)

        self.fon_image = pygame.image.load('images/fon.jpg').convert()
        self.display_image = pygame.image.load('images/background1.jpg').convert()

        self.objects = self.init_objects()

        self.player = self.init_player()
        self.enemy = self.init_enemy()
        self.filling()
        self.creatre_obj_without_collision()

    def init_player(self):
        return Player(700, 325,
                      5,  # speed
                      'pikachu.png',
                      self.players,
                      None,  # enemy
                      20,  # health
                      2,  # damage
                      Setting1(),
                      self.objects,
                      self.bullets,
                      Blink(0, 300, 400),
                      Stan(0, 300, 400, 40, 300, self.stans_images, None),
                      Explosion(0, 600, 150, 10, 100, 20, self.explosion_images))

    def init_enemy(self):
        return Player(1150, 825,
                      5,  # speed
                      'bulbazavr.png',
                      self.players,
                      None,  # enemy
                      15,  # health
                      2,  # damage
                      Setting2(),
                      self.objects,
                      self.bullets,
                      MakeSmoke(0, 600, 300, self.smokes),
                      Stan(0, 600, 400, 40, 300, self.stans_images, None),
                      Explosion(0, 600, 150, 10, 100, 20, self.explosion_images))

    def init_objects(self):
        objects = []
        objects.append(Wall(25, 325, 0, 'vert_wall.jpg', self.walls))
        objects.append(Wall(25, 975, 0, 'vert_wall.jpg', self.walls))
        objects.append(Wall(1375, 325, 0, 'vert_wall.jpg', self.walls))
        objects.append(Wall(1375, 975, 0, 'vert_wall.jpg', self.walls))
        objects.append(Wall(700, 25, 0, 'gor_wall.jpg', self.walls))
        objects.append(Wall(700, 1275, 0, 'gor_wall.jpg', self.walls))

        objects.append(BreakableWall(700, 600, 0, 'wall_to_break.jpg', self.breakeable_walls, 3, objects))
        objects.append(BreakableWall(550, 1005, 0, 'kalitka.png', self.breakeable_walls, 3, objects))
        objects.append(BreakableWall(800, 690, 0, 'kalitka.png', self.breakeable_walls, 3, objects))

        objects.append(Building(250, 250, 0, 'house.png', self.buildings))
        objects.append(Building(350, 550, 0, 'zabor_gor.png', self.buildings))
        objects.append(Building(560, 350, 0, 'zabor_vert.png', self.buildings))

        objects.append(Building(250, 750, 0, 'house.png', self.buildings))
        objects.append(Building(350, 1075, 0, 'zabor_gor.png', self.buildings))
        objects.append(Building(560, 750, 0, 'zabor_vert.png', self.buildings))

        objects.append(Building(1050, 1000, 0, 'house.png', self.buildings))
        objects.append(Building(1050, 600, 0, 'zabor_gor.png', self.buildings))
        objects.append(Building(800, 950, 0, 'zabor_vert.png', self.buildings))

        objects.append((Building(1050, 200, 0, 'pokevillage.png', self.buildings)))

        objects.append(Stvol(475, 450, 0, 'stvol1.png', self.trunks))
        objects.append(Stvol(475, 850, 0, 'stvol1.png', self.trunks))
        objects.append(Stvol(275, 1100, 0, 'stvol1.png', self.trunks))
        objects.append(Stvol(1225, 1100, 0, 'stvol2.png', self.trunks))

        return objects

    def creatre_obj_without_collision(self):
        for i in range(1, 14):
            bush = Bush(100 * i, 100, 0, 'bush.png', self.bushes)
        for i in range(1, 14):
            bush = Bush(100 * i, 1200, 0, 'bush.png', self.bushes)
        for i in range(2, 12):
            bush = Bush(100, 100 * i, 0, 'bush.png', self.bushes)
        for i in range(2, 12):
            bush = Bush(1300, 100 * i, 0, 'bush.png', self.bushes)
        for i in range(1, 5):
            bush = Bush(875, 700 + 100 * i, 0, 'bush.png', self.bushes)

        lake = Lake(1050, 425, 0, 'lake.png', self.lakes)
        road = Building(850, 650, 0, 'road.png', self.buildings)

        krona1 = (Krona(487, 341, 0, 'krona1.png', self.crowns))  # 12, -109
        krona1 = (Krona(487, 741, 0, 'krona1.png', self.crowns))
        krona1 = (Krona(287, 1001, 0, 'krona1.png', self.crowns))
        krona2 = (Krona(1236, 992, 0, 'krona2.png', self.crowns))  # 21, -109

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
        pygame.mixer.music.play(-1)

        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.display.blit(self.fon_image, (0, 0))
            self.display.blit(self.display_image, (self.delta.x, self.delta.y))

            # drawing
            self.lakes.draw(self.display)
            self.buildings.draw(self.display)
            self.players.draw(self.display)
            self.bushes.draw(self.display)
            self.trunks.draw(self.display)
            self.crowns.draw(self.display)
            self.smokes.draw(self.display)
            self.walls.draw(self.display)
            self.breakeable_walls.draw(self.display)
            self.stans_images.draw(self.display)
            self.explosion_images.draw(self.display)
            self.bullets.draw(self.display)

            # отслеживаем смещение главного игрока
            self.tracking_the_offset()

            # moving other
            self.enemy.move_on_vector(self.vector)

            # updating objects
            self.walls.update(self.vector)
            self.breakeable_walls.update(self.vector)
            self.buildings.update(self.vector)
            self.bullets.update(self.vector)
            self.smokes.update(self.vector)
            self.stans_images.update(self.vector)
            self.bushes.update(self.vector)
            self.trunks.update(self.vector)
            self.crowns.update(self.vector)
            self.lakes.update(self.vector)

            self.explosion_images.update()

            pygame.display.update()
            self.FPS.tick(60)
