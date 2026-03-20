from circleshape import CircleShape
from constants import *
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    
    Score = 0
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.Score += SCOREPLUS 
            return
        else:
            
            log_event("asteroid_split")
            self.Score += SCOREPLUS * 2
            random_angle = random.uniform(20, 50)
            new_vector = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            split_Asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            vc1 = new_vector * 1.2
            vc2 = new_vector2 * 1.2
            split_Asteroid.velocity = vc1
            split_Asteroid2.velocity = vc2
            
#        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
#        velocity *= PLAYER_SHOOT_SPEED
#        shot.velocity = velocity