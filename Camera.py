import pygame

class Camera:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def move_on_vector(self, vector):
        self.rect.x += vector.x
        self.rect.y += vector.y


