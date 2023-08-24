import pygame
from math import *

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
        pygame.draw.circle(win, self.color, (x, y), self.radius)


def update_planet_positions(planets, sun):
    for planet in planets:
        if not planet.sun:
            # Calculate gravitational force between planet and sun
            dx = sun.x - planet.x
            dy = sun.y - planet.y
            r = sqrt(dx**2 + dy**2)
            f = Planet.g * sun.mass * planet.mass / r**2

            # Calculate acceleration of planet
            ax = f * dx / r / planet.mass
            ay = f * dy / r / planet.mass

            # Update velocity and position of planet using Euler's method
            planet.x_vel += ax * Planet.timestep
            planet.y_vel += ay * Planet.timestep
            planet.x += planet.x_vel * Planet.timestep
            planet.y += planet.y_vel * Planet.timestep


def main():
    run = True
    clock = pygame.time.Clock()
    sun = Planet(0, 0, 30, yellow, 1.98892 * 10**30)
    sun.sun = True
    erth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
    moon = Planet(-1.524 * Planet.AU, 0, 12, white, 6.39 * 10**23)
    mercury = Planet(0.387 * Planet.AU, 0, 8, GRAY, 3.30 * 10**23)
    venus = Planet(0.723 * Planet.AU, 0, 14, RED, 4.8685 * 10**24)
    planets = [sun, erth, moon, mercury, venus]

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update_planet_positions(planets, sun)

        for planet in planets:
            planet.draw(win)

        pygame.display.update()
    pygame.quit()


main()
