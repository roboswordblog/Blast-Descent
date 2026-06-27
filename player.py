from particles import *
import pygame
import math
balloons = 3
class Balloon:
    def __init__(self, type,num, player):
        self.type = type
        self.player = player
        self.num = num
        self.image = pygame.transform.rotate(pygame.image.load(f"assets/balloons/{self.type}.png"), (num*30)-30)
        self.rect = self.image.get_rect()
        self.dead = False

    def draw(self, window):
        if self.dead:
            return
        base_image = pygame.image.load(f"assets/balloons/{self.type}.png")
        wobble = math.sin(pygame.time.get_ticks() * 0.005 + self.num) * 3
        angle = (self.num * 30) - 30 + wobble

        image = pygame.transform.rotate(base_image, angle)

        rect = image.get_rect(center=self.rect.center)

        window.blit(image, rect)

    def update(self, bulletList):
        if self.dead:
            return
        global balloons
        self.rect.x = self.player.x
        self.rect.y = self.player.y + 10
        for bullet in bulletList:
            if self.rect.colliderect(bullet.rect):
                if bullet.type == "enemy":
                    for i in range(10):
                        Particle(self.rect.x, self.rect.y, (180, 180, 180))
                        balloons -= 1
                        self.dead = True


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
        self.balloon1 = Balloon("0", )

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.ammo < 0:
            self.mode = "reload"


    def draw(self, window):
        self.image = pygame.image.load(f"images/player.{self.mode}.png")
        window.blit(self.image, self.rect)
