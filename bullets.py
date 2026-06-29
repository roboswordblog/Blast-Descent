import pygame
bulletList = []

class Bullet:
    def __init__(self, x, y, dir, tag):
        self.x = x
        self.y = y
        self.dir = dir
        self.tag = tag
