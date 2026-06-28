import pygame
import random

cloudList = []
class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"assets/clouds/{random.choice([0,1])}.png")

    def update(self):
        self.x -= 1


    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
