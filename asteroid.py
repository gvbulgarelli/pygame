
import pygame
import random
from circleshape import *
from constants import *
from score import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            Score.kill_point()
            return
        else:
            angle = random.uniform(20, 50)
            vector_a = self.velocity.rotate(-angle)
            vector_b = self.velocity.rotate(angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = vector_a * 1.2
            asteroid_b.velocity = vector_b * 1.2
            Score.hit_point()
    

