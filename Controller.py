from Creating_objects import *

pygame.init()
FPS = pygame.time.Clock()


def run_game():
    game = True
    # pygame.mixer.music.play(-1)a
    d_x = 0
    d_y = 0
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(display_image, (d_x, d_y))
        bullets.draw(display)
        players.draw(display)
        static_walls.draw(display)

        vector = [pika.rect.x, pika.rect.y]
        players.update()
        vector[0] -= pika.rect.x
        vector[1] -= pika.rect.y
        pika.rect.x += vector[0]
        pika.rect.y += vector[1]
        d_x += vector[0]
        d_y += vector[1]
        bulba.move_on_vector(vector)
        camera.move_on_vector(vector)

        static_walls.update(vector)
        bullets.update(bulba, vector)


        pygame.display.update()
        FPS.tick(60)


run_game()
