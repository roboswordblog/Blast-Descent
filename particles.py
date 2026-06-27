import random
import pygame

particleList = []
class Particle:
    def __init__(self,x,y, color):
        self.x = x
        self.y = y
        self.vel = [
            random.uniform(-2, 2),
            random.uniform(-2, 2)
        ]
        self.particleTimer = 50
        particleList.append(self)
        self.vel[0] *= 0.97
        self.vel[1] *= 0.97
        self.color = color

    def update(self):
        self.particleTimer -= 1
        self.x += self.vel[0]
        self.y += self.vel[1]
        if self.particleTimer <= 0:
            particleList.remove(self)


    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), int(self.particleTimer/10))
