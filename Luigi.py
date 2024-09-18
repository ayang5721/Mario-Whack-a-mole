import pygame
import random
import time

from Character import Character
from config import *


class Luigi(Character):

    def __init__(self):
        self.luigiImage
     
    def display(self):
        luigiImg = pygame.image.load(self.marioImage)
        luigiImg = pygame.transform.scale(luigiImg, (cellSize, cellSize))
        self.screen.blit(luigiImg, (self.x, self.y))
