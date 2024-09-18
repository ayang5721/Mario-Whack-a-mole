import pygame
import random
import time

from Character import Character
from config import *


class Bomb(Character):

    def __init__(self):
        self.marioImage = 'graphics/marioPipe.png'
     
    def display(self):
        mario_img = pygame.image.load(self.marioImage)
        mario_img = pygame.transform.scale(mario_img, (cellSize, cellSize))
        self.screen.blit(mario_img, (self.x, self.y))
