import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCOREPLUS
from logger import log_state
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from circleshape import *
from shot import Shot



def main():

    pygame.init()
    
    score = 0
    my_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    AsteroidFields = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
   
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    font = pygame.font.SysFont(None, 40)
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return  
        
        screen.fill("black")
        
        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid) == True:
                log_event("player_hit")
                print("Game Over!")
                print(f"your Score: {score}")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    
                    log_event("asteroid_shot")
                    score += SCOREPLUS
                    shot.kill()
                    asteroid.split()
        text = font.render(f"your score: {score}", True, (255, 255, 255))
        screen.blit(text, (20, 20))
        pygame.display.flip()
        dt = my_clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
