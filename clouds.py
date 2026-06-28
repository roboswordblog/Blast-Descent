import pygame
import random

cloudList = []
class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"assets/clouds/{random.choice([0,1])}.png")

    def update(self, player):
        self.x += 0.5
        self.y += player.ay


    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
