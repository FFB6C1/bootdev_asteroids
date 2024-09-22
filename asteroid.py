import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(split_angle) * 1.2
        velocity_2 = self.velocity.rotate(-split_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        child_ast_1.velocity = velocity_1
        child_ast_2.velocity = velocity_2