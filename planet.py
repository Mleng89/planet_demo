class Planet:
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        # Generating the circle for planets to move
        self.x_velocity = 0
        self.y_velocity = 0
