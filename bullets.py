import pygame
from particles import *
bulletList = []

class Bullet:
    def __init__(self, x, y, dir, tag):
        self.x = x
        self.y = y
        self.dir = dir
        self.tag = tag
        self.image = pygame.transform.flip(pygame.transform.scale2x(pygame.image.load(f"assets/bullets/{tag}Bullet.png")), dir, False)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.timer = 100
        bulletList.append(self)

    def update(self):
        self.x -= self.dir
        self.timer -= 1
        if self.timer <= 0:
            for i in range(50):
                Particle(
                    self.x,
                    self.y,
                    random.choice([
                        (120, 120, 120),
                        (180, 180, 180),
                        (255, 60, 60),
                        (200, 30, 30),
                        (255, 140, 0),
                        (255, 180, 40),
                    ])
                )

    def draw(self, window):
        window.blit(self.image, self.rect)
