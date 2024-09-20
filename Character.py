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
        self.timeAlive = round(random.uniform(2.0, 5.0), 2)

    def isAlive(self):
        return time.time() < (self.timeCreated + self.timeAlive)
    
    def timeRemaining(self):
        return (self.timeCreated + self.timeAlive) - time.time()

    def isClicked(self, mouseX, mouseY):
        xMin = (self.x)
        xMax = (self.x) + cellSize      
        yMin = (self.y)
        yMax = (self.y) + cellSize
        if xMin <= mouseX <= xMax and yMin <= mouseY <= yMax:
            return True
        return False