import pygame

WIDTH, HEIGHT = 800, 800


class Planet:
    # Astronomical Units * Meters (1000) -- Distance from the Sun
    AU = 149.6e6 * 1000
    # Gravitational constance
    G = 6.67428e-11
    SCALE = 200 / AU  # 1 AU = ~100px in pygame
    TIMESTEP = 3600 * 24  # Representing 1 day (3600 seconds in an hour * 24 hours)

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        # Generating the circle for planets to move
        self.x_velocity = 0  # in meters
        self.y_velocity = 0  # in meters

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)
