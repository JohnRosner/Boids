import math

import pygame

from constants import *
from boid import *
import random

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
boids = []


def init():
    for i in range(num_boids):
        boids.append(Boid(random.randint(50, window_width - 100), random.randint(50, window_height - 100), random.random() * 2 * math.pi))


def draw():
    window.fill(border_color)
    pygame.draw.rect(window, background_color, (border_width, border_width, window_width - 2 * border_width, window_height - 2 * border_width))
    for boid in boids:
        points = boid.get_points()
        pygame.draw.polygon(window, boid_color, points)


def loop():
    # boids[0].theta += 0.05
    for boid in boids:
        boid.move()
        pass
    draw()


def main():
    init()
    run = True
    while run:
        pygame.time.delay(16)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        loop()
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
