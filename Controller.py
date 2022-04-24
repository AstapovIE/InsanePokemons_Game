from Creating_objects import *

pygame.init()
FPS = pygame.time.Clock()


def run_game():
    game = True
    # pygame.mixer.music.play(-1)a
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(display_image, (0, 0))
        bullets.draw(display)
        players.draw(display)
        static_walls.draw(display)

        players.update()
        bullets.update(bulba)

        pygame.display.update()
        FPS.tick(60)


run_game()
