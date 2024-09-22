import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect = None, special_flags= 0)
        dt = clock.tick(60)/1000

        for item in updatable:
            item.update(dt)
        
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                return
            
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()


        
        pygame.display.flip()

if __name__ == "__main__":
    main()