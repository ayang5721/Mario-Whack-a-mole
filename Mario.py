import pygame
import config.cellSize


class Mario:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.marioImage = 'graphics/marioPipe.png'
        self.x = x
        self.y = y
     
    def display(self):
        mario_img = pygame.image.load(self.marioImage)
        mario_img = pygame.transform.scale(mario_img, (cellSize, cellSize))
        screen.blit(mario_img, (self.x, self.y))