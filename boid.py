import math

from constants import *


def rotate(x, y, theta, orig_x, orig_y):
    return x * math.cos(theta) - y * math.sin(theta) + orig_x, x * math.sin(theta) + y * math.cos(theta) + orig_y


class Boid:
    def get_points(self):
        points = [(self.x, self.y),
                  rotate(-0.3 * boid_size, -boid_size, -self.theta, self.x, self.y),
                  rotate(0.3 * boid_size, -boid_size, -self.theta, self.x, self.y)]
        return points

    def move(self):
        self.x += math.sin(self.theta) * boid_speed
        self.y += math.cos(self.theta) * boid_speed

    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
