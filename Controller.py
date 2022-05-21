from Creating_objects import *

pygame.init()


class Controller:

    def run_game(self, Player, FPS):
        game = True
        # pygame.mixer.music.play(-1)
        delta = Vector(0, 0)  # для движения backgrond'a
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.blit(fon_image, (0, 0))
            display.blit(display_image, (delta.x, delta.y))
            bullets.draw(display)
            players.draw(display)
            smokes.draw(display)
            static_walls.draw(display)
            stans_images.draw(display)
            explosion_images.draw(display)


            vector = Vector(Player.rect.x, Player.rect.y)  # отслеживаем смещение главного игрока
            players.update()
            vector -= Player
            Player += vector
            delta += vector

            bulba.move_on_vector(vector)

            static_walls.update(vector)
            bullets.update(bulba, vector)
            smokes.update(vector)
            stans_images.update(vector)
            explosion_images.update()


            pygame.display.update()
            FPS.tick(60)
