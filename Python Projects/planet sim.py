import pygame
import math

pygame.init()

width, height = 800, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Planet Simulation ")
white = (255, 255, 255)
yellow = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
GRAY = (80, 78, 81)


class Planet:
    AU = 149.6e6 * 1000
    g = 6.67428e-11
    scale = 240 / AU  # 1 Au = 100 pixels
    timestep = 3600 * 24  # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.scale + width / 2
        y = self.y * self.scale + height / 2
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.scale + width / 2
                y = y * self.scale + height / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)
        if other.sun:
            self.distance_to_sun = distance
        force = self.g * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, Planets):
        total_fx = total_fy = 0
        for Planet in Planets:
            if self == Planet:
                continue
            fx, fy = self.attraction(Planet)
            total_fx += fx
            total_fy += fy
        self.x_vel += total_fx / self.mass * self.timestep
        self.y_vel += total_fy / self.mass * self.timestep

        self.x += self.x_vel * self.timestep
        self.y += self.y_vel * self.timestep
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()
    sun = Planet(0, 0, 30, yellow, 1.98892 * 10**30)
    sun.sun = True
    erth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
    erth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, white, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, GRAY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, RED, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    planets = [sun, erth, mars, mercury, venus]

    while run:
        clock.tick(60)
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.update_position(planets)
            planet.draw(win)
        pygame.display.update()
    pygame.quit()


main()
