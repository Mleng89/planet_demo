import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation!")


def main():
    run = True

    while run:
        for event in pygame.event.get():
            print("what are my events:", event)
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


main()