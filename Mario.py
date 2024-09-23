import pygame

from PIL import Image
from Character import Character
from config import *

from util import clamp

class Mario(Character):

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        
        # Makes list of frames
        self.frames = []

        # Turns going up gif into frames and stores into list frames
        gif_path = 'graphics/mario_Up.gif'
        gif = Image.open(gif_path)
        for frame in range(gif.n_frames):
            gif.seek(frame)
            frame_image = gif.convert("RGBA")
            frame_surface = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
            frame_surface = pygame.transform.scale(frame_surface, (cellSize, cellSize))
            for i in range(2):
                self.frames.append(frame_surface)

        # Finds index for middleframe insertion
        indexMid = len(self.frames)

        # Turns going down gif into frames and stores into list frames
        gif_path = 'graphics/mario_Down.gif'
        gif = Image.open(gif_path)
        for frame in range(gif.n_frames):
            gif.seek(frame)
            frame_image = gif.convert("RGBA")
            frame_surface = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
            frame_surface = pygame.transform.scale(frame_surface, (cellSize, cellSize))
            for i in range(2):
                self.frames.append(frame_surface)

        # Turns total time into total amount of frames
        totalFrames = round(self.timeAlive * 30)


        # Finds the amount of frames for the middle part
        middleFrames = totalFrames - len(self.frames)

        # Creates middle frame
        middleFrame = pygame.image.load('graphics/mario.png')
        middleFrame = pygame.transform.scale(middleFrame, (cellSize, cellSize))

        # Inputs all the middle frames
        for i in range(middleFrames):
            self.frames.insert(indexMid, middleFrame)

    def display(self):
        # convert time remaining alive into a specific frame
        frameIndex = round((self.timeAlive - self.timeRemaining()) * 30)
        frameIndex = clamp(frameIndex, 0, len(self.frames) - 1)
        mario_img = self.frames[frameIndex]
        self.screen.blit(mario_img, (self.x, self.y))

