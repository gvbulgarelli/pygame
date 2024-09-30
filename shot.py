from circleshape import CircleShape
from constants import *
import pygame


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "purple", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

class Bomb(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt):
        self.position += pygame.Vector2(0, 1) * dt * PLAYER_BOMB_SPEED



        