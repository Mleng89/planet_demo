import pygame
import math
from planet import Planet

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation!")

WHITE = (255, 255, 255)


def main():
    run = True
    # Clock is a FPS lock, setting to 60fps
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        # WIN.fill(WHITE)
        # pygame.display.update()

        for event in pygame.event.get():
            print("what are my events:", event)
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


main()
