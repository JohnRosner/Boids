import pygame

from constants import *
from boid import *

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
boids = [Boid(500, 500, 0)]


def draw():
    window.fill(border_color)
    pygame.draw.rect(window, background_color, (border_width, border_width, window_width - 2 * border_width, window_height - 2 * border_width))
    for boid in boids:
        points = boid.get_points()
        pygame.draw.polygon(window, boid_color, points)


def loop():
    boids[0].theta += 0.05
    boids[0].move()
    draw()


def main():
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
