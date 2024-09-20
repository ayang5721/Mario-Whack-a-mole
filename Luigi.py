import pygame
import random
import time

from Character import Character
from config import *


class Luigi(Character):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.luigiImage = 'graphics/luigi.png'
     
    def display(self):
        luigiImg = pygame.image.load(self.luigiImage)
        luigiImg = pygame.transform.scale(luigiImg, (cellSize, cellSize))
        self.screen.blit(luigiImg, (self.x, self.y))
