from particles import *
import pygame
pygame.init()

window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Sky Fighter")

while True:
    window.fill((200, 220, 226))
    for particle in particleList:
        particle.draw(window)
        particle.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()