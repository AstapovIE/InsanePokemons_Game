import pygame

FPS = pygame.time.Clock()
clock = pygame.time.Clock()

game_field = pygame.display.set_mode((800,600))

screen = pygame.Surface((200,200))
screen.fill((255,0,0))
game_field.blit(screen, (50,50))
x = 50
y = 50

def run_game():
    game = True
    global x, y

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        screen.fill((255, 0, 0))
        game_field.blit(screen, (x, y))

        if x < 800:
            x += 2
        else:
            x = 0

        pygame.display.update()
        FPS.tick(60)
run_game()
