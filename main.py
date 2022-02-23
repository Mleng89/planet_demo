import pygame
import math
from planet import Planet

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation!")

WHITE = (255, 255, 255)
ODDLACE = (253, 245, 230)
YELLOW = (255, 255, 0)
BLUE = (135, 206, 235)
RED = (255, 0, 0)
DARK_GREY = (169, 169, 169)


def main():
    run = True
    # Clock is a FPS lock, setting to 60fps
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**24)
    venus = Planet(0.723 * Planet.AU, 0, 14, ODDLACE, 4.8685 * 10**24)

    planets = [sun, earth, mars, mercury, venus]
    while run:
        clock.tick(60)
        # WIN.fill(WHITE)

        for event in pygame.event.get():
            # print("what are my events:", event)
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.draw(WIN)
        # Updates to draw planets at the moment
        pygame.display.update()

    pygame.quit()


main()
