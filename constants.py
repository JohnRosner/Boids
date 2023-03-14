import pygame

window_height = 800
window_width = 1200
border_width = 10

pause_key = pygame.K_SPACE

border_color = (50, 50, 50)
background_color = (255, 255, 255)
boid_color = (0, 0, 150)

boid_size = 15
boid_speed = 3
num_boids = 50

close_distance = 60
close_to_walls = 60
separate_force = 0.0
align_force = 0.1
cohere_force = 0.0
walls_force = 0.1
mouse_force = 0.0

