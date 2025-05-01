# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from pygame.locals import *
from constants import * # Because this is a smaller project, and we don't risk conflicting import names, we're going to use a wildcard import for convenience. In a larger project, you'd want to import only the constants you need.



def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create limit to 60fps
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()


    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                print("Game over")
                sys.exit()
            for shot in shots:
                if asteroid.checkCollision(shot):
                    asteroid.split() 
                    shot.kill()
        
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # limit framerate
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()