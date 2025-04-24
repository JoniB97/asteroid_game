# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from pygame.locals import *
from constants import * # Because this is a smaller project, and we don't risk conflicting import names, we're going to use a wildcard import for convenience. In a larger project, you'd want to import only the constants you need.

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Game loop
    #Change
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()