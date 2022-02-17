import pygame


class Ball:
    MAX_VEL = 5
    WHITE = (255,255,255)
    COLOR = WHITE
    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.orignal_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset_ball(self):
        self.x = self.original_x
        self.y = self.orignal_y
        self.y_vel = 0
        self.x_vel *= -1