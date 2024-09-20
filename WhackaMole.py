import pygame
import random
import time
from config import *
from Mario import Mario
from Bomb import Bomb
from Luigi import Luigi

# Initialize Pygame
pygame.init()

# Load images
pipe_img = pygame.image.load('graphics/pipe.png')
pipe_img = pygame.transform.scale(pipe_img, (cellSize, cellSize))

# Create screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Whack-a-Mario")

# Font for score....
font = pygame.font.Font(None, 36)

# Initialize clock
clock = pygame.time.Clock()

# Game variables
score = 0
characters = []
grid = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]

# Function to draw the grid
def draw_grid():
	for row in range(GRID_SIZE):
		for col in range(GRID_SIZE):
			x = col * cellSize
			y = row * cellSize
			screen.blit(pipe_img, (x, y))

# Main game loop
running = True
timeUp = False

while running:
	while not timeUp:
		screen.fill(WHITE)
		draw_grid()

		seed = random.random()
		randomX = random.randint(0,2) * cellSize
		randomY = random.randint(0,2) * cellSize
		if not grid[randomY//cellSize][randomX//cellSize]:
			if seed < 0.03:
				characters.append(Mario(screen, randomX, randomY))
				grid[randomY//cellSize][randomX//cellSize] = 1
			elif seed < 0.045:
				characters.append(Bomb(screen, randomX, randomY))
				grid[randomY//cellSize][randomX//cellSize] = 2
			elif seed < 0.06:
				characters.append(Luigi(screen, randomX, randomY))
				grid[randomY//cellSize][randomX//cellSize] = 3

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouseX, mouseY = event.pos
				for character in characters:
					if character.isClicked(mouseX, mouseY):
						if character.__class__.__name__ == "Mario":
							score += 1
						elif character.__class__.__name__ == "Bomb":
							#code for when you click bomb
							timeUp = True
							pass
						elif character.__class__.__name__ == "Luigi":
							score += 3
							#code for when you click luigi
			
							pass
						characters.remove(character)
						grid[character.y//cellSize][character.x//cellSize] = 0

		# different actions depending on type of character
		for character in characters:
			character.display()
			# print("x: ", character.x, "y: ", character.y)
			# print(character.isClicked())

		# Draw score
		score_text = font.render(f"Score: {score}", True, BLACK)
		screen.blit(score_text, (10, 10))

		# Update display
		pygame.display.flip()

		# Cap the frame rate
		clock.tick(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	screen.fill(BLUE)
	pygame.display.flip()

# Quit Pygame
pygame.quit()