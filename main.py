from particles import *
from player import *
from bullets import *
from enemy import *
from ui import *
import pygame
pygame.init()

window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Sky Fighter")

class States:
    def __init__(self):
        pass
player = Player(500, 200)
clock = pygame.time.Clock()
for i in range(100):
    Particle(500, 200, (255,255,255))
while True:
    window.fill((200, 220, 226))

    player.draw(window)
    player.update()
    for particle in particleList:
        particle.draw(window)
        particle.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    clock.tick(60)
    pygame.display.update()