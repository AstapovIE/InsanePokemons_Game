from Point import Vector
import pygame

pygame.init()


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/' + surf).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.add(group)

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("second operand not Vector")
        self.rect.x += other.x
        self.rect.y += other.y
        return self

    def update(self, vector):
        self += vector
