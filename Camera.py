import pygame

class Camera:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def move_on_vector(self, vector):
        self.rect[0] += vector[0]
        self.rect[1] += vector[1]

