import pygame
import random
import time
from config import *

class Character:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.timeCreated = time.time()
        self.timeAlive = random.uniform(0.25, 1.0)

    def isAlive(self):
        return time.time() > (self.timeCreated + self.timeAlive)
    
    def isClicked(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                xMin = (self.x * cellSize)
                xMax = (self.x * cellSize) + cellSize
                yMin = (self.y * cellSize)
                yMax = (self.y * cellSize) + cellSize
                if xMin <= mouseX < xMax and yMin <= mouseY < yMax:
                    return True
        return False