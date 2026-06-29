import pygame
import random

cloudList = []
class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load(f"assets/clouds/{random.choice([0,1])}.png")))

    def update(self, player):
        self.y += player.ay


    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
