import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mode = "idle"
        self.ammo = 25
        self.health = 100
        self.firingCooldown = 0
        self.reloadCooldown = 0
        # reload time should be 4 seconds
        self.image = pygame.image.load(f"images/player.{self.mode}.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.ammo < 0:
            self.mode = "reload"


    def draw(self, window):
        self.image = pygame.image.load(f"images/player.{self.mode}.png")
        window.blit(self.image, self.rect)