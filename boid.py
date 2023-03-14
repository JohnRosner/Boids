import math

import pygame.mouse

from constants import *


def rotate(x, y, theta, orig_x, orig_y):
    return x * math.cos(theta) - y * math.sin(theta) + orig_x, x * math.sin(theta) + y * math.cos(theta) + orig_y


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def constrain_theta(theta):
    while theta < 0:
        theta += 2 * math.pi
    while theta > 2 * math.pi:
        theta -= 2 * math.pi
    return theta


def get_close_boids(boids, x, y):
    close_boids = []
    for boid in boids:
        if 2 < distance(boid.x, boid.y, x, y) < close_distance:
            close_boids.append(boid)
    return close_boids


def in_obstacle(x, y):
    if border_width < x < window_width - border_width and border_width < y < window_height - border_width:
        return False
    return True


class Boid:
    def get_points(self):
        points = [(self.x, self.y),
                  rotate(-0.3 * boid_size, -boid_size, -self.theta, self.x, self.y),
                  rotate(0.3 * boid_size, -boid_size, -self.theta, self.x, self.y)]
        return points

    def steer(self, x, y):
        # This looks weird because of the coordinates of pygame
        diff_x, diff_y = x - self.x, self.y - y
        target_theta = math.atan2(diff_y, diff_x) + math.pi / 2
        theta_diff = target_theta - self.theta
        theta_diff = constrain_theta(theta_diff)
        return theta_diff

    def align(self, boids):
        if len(boids) == 0:
            return 0
        avg_theta_i = 0
        avg_theta_j = 0
        for boid in boids:
            avg_theta_i += math.sin(boid.theta)
            avg_theta_j += math.cos(boid.theta)
        avg_theta_i /= len(boids)
        avg_theta_j /= len(boids)

        target_theta = math.atan2(avg_theta_j, avg_theta_i)
        theta_diff = target_theta - self.theta
        theta_diff = constrain_theta(theta_diff)
        return theta_diff

    def separate(self, boids):
        return 0

    def cohere(self, boids):
        return 0

    # If not close to the walls, do nothing, else steer towards the center of the screen
    def avoid_walls(self):
        if close_to_walls < self.x < window_width - close_to_walls and \
                close_to_walls < self.y < window_height - close_to_walls:
            return 0
        return self.steer(window_width / 2, window_height / 2)

    def constrain(self):
        if self.x < 0:
            self.x = window_width - 10
        if self.x > window_width:
            self.x = 10
        if self.y < 0:
            self.y = window_height - 10
        if self.y > window_height:
            self.y = 10

        self.theta = constrain_theta(self.theta)

    def move(self, boids):
        self.x += math.sin(self.theta) * boid_speed
        self.y += math.cos(self.theta) * boid_speed
        close_boids = get_close_boids(boids, self.x, self.y)
        self.theta += align_force * self.align(close_boids) + \
                      separate_force * self.separate(close_boids) + \
                      cohere_force * self.cohere(close_boids) + \
                      walls_force * self.avoid_walls() + \
                      mouse_force * self.steer(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.constrain()

    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
