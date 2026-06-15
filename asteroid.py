import pygame
import random
from logger import log_event
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)
        new_radius_1 = self.radius - ASTEROID_MIN_RADIUS
        new_radius_2 = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius_1)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius_2)
        new_asteroid_1.velocity = new_vector_1 * 1.2
        new_asteroid_2.velocity = new_vector_2 * 1.2
        

