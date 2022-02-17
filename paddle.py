from time import sleep
import pygame

class Paddle:
    WHITE = (255, 255, 255)
    COLOR = WHITE
    VEL = 4  # VEL is velocity for moving paddles up and down


    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.orignal_y = y
        self.width = self.original_width = width
        self.height = self.original_height = height


    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x, self.y, self.width, self.height))


    '''
    Function move(self, up=True) makes it so that the paddles can move up/down.
    When paddles move up, the y-coordinate will subtract by velocity since the top part
    of the window starts at y-coordinate = 0.
    So moving down, the y-coordinate will increase by the velocity.
    '''
    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
    
    def reset_paddle(self):
        self.x = self.original_x
        self.y = self.orignal_y