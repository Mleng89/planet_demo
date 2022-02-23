import pygame
import math

pygame.font.init()

WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont("arial", 12)


class Planet:
    # Astronomical Units * Meters (1000) -- Distance from the Sun
    AU = 149.6e6 * 1000
    # Gravitational constance
    G = 6.67428e-11
    SCALE = 200 / AU  # 1 AU = ~100px in pygame
    # Representing 1 day (3600 seconds in an hour * 24 hours)
    TIMESTEP = 3600 * 24

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

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if not self.sun:
            distance_text = FONT.render(
                f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE
            )
            win.blit(
                distance_text,
                (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2),
            )

    def force_of_attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance
        # Straight line force
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)  # atan2 -> special function
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_force_x = total_force_y = 0
        for planet in planets:
            if self == planet:
                continue

            force_x, force_y = self.force_of_attraction(planet)
            total_force_x += force_x
            total_force_y += force_y

        self.x_velocity += total_force_x / self.mass * self.TIMESTEP
        # F = mass / acceleration
        self.y_velocity += total_force_y / self.mass * self.TIMESTEP

        self.x += self.x_velocity * self.TIMESTEP
        self.y += self.y_velocity * self.TIMESTEP

        self.orbit.append((self.x, self.y))
