from particles import *
import pygame
import math
from bullets import *
balloons = 3
class Balloon:
    def __init__(self, type, num, player):
        self.type = type
        self.player = player
        self.num = num

        self.base_image = pygame.image.load(f"assets/balloons/{self.type}.png")
        self.rect = self.base_image.get_rect()

        self.dead = False

        # IMPORTANT: initialize position immediately
        self.rect.midbottom = self.player.rect.midtop
        self.rect.y -= (self.num * 12)

    def draw(self, window):
        if self.dead:
            return

        wobble = math.sin(pygame.time.get_ticks() * 0.005 + self.num) * 3
        angle = 0 + wobble

        image = pygame.transform.rotate(self.base_image, angle)

        rect = image.get_rect(center=self.rect.center)
        window.blit(image, rect)

    def update(self):
        if self.dead:
            return

        base_x = self.player.rect.centerx
        base_y = self.player.rect.top

        self.rect.centerx = base_x
        self.rect.centery = base_y - (self.num * 18)

        for bullet in bulletList:
            if self.rect.colliderect(bullet.rect):
                if bullet.type == "enemy":
                    for i in range(10):
                        Particle(self.rect.centerx, self.rect.centery, (200, 200, 200))

                    self.dead = True

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ay = 0
        self.mode = "idle"
        self.ammo = 25
        self.health = 100
        self.firingCooldown = 0
        self.reloadCooldown = 0
        # reload time should be 4 seconds
        self.image = pygame.transform.scale(pygame.image.load(f"assets/player/{self.mode}.png"), (64, 48))
        self.rect = self.image.get_rect()
        self.balloon1 = Balloon("0", 0, self)
        self.balloon2 = Balloon("1", 1, self)
        self.balloon3 = Balloon("2", 2, self)
        self.rect.x = self.x
        self.rect.y = self.y
        self.imageDict = {
            "idle": pygame.transform.scale(pygame.image.load(f"assets/player/idle.png"), (64, 48)),
            "reload": pygame.transform.scale(pygame.image.load(f"assets/player/reload.png"), (64, 48))
        }

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.ammo < 0:
            self.mode = "reload"
        self.balloon1.update()
        self.balloon2.update()
        self.balloon3.update()

    def draw(self, window):
        self.image = self.imageDict[self.mode]
        self.balloon1.draw(window)
        self.balloon2.draw(window)
        self.balloon3.draw(window)
        window.blit(self.image, self.rect)
