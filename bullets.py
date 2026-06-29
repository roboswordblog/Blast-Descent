import pygame
bulletList = []

class Bullet:
    def __init__(self, x, y, dir, tag):
        self.x = x
        self.y = y
        self.dir = dir
        self.tag = tag
        self.image = pygame.transform.flip(pygame.transform.scale2x(pygame.image.load(f"assets/bullets/{tag}.png")), dir, False)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        bulletList.append(self)

    def update(self):
        self.x -= self.dir

    def draw(self):
        pass
