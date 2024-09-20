import pygame
import random
import time
from config import *
from Mario import Mario
from Bomb import Bomb
from Luigi import Luigi

# Initialize Pygame
pygame.init()

# Score file
SCORE_FILE = "scores.txt"

def save_score(score):
    with open(SCORE_FILE, "a") as file:
        file.write(f"{score}\n")

def load_scores():
    try:
        with open(SCORE_FILE, "r") as file:
            scores = [int(line.strip()) for line in file]
    except FileNotFoundError:
        scores = []
    return scores.sort()

# Load images
pipe_img = pygame.image.load('graphics/pipe.png')
pipe_img = pygame.transform.scale(pipe_img, (cellSize, cellSize))

brick_img = pygame.image.load('graphics/brick.png')

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

# Main game loop
running = True
timeUp = False

while running:
	while not timeUp:
		print(load_scores())
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
				timeUp = True
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
			if not character.isAlive():
				characters.remove(character)
				grid[character.y//cellSize][character.x//cellSize] = 0

		# Draw score
		score_text = font.render(f"Score: {score}", True, BLACK)
		screen.blit(score_text, (10, 10))

		# Update display
		pygame.display.flip()

		# Cap the frame rate
		clock.tick(30)

	# Game over screen
	screen.fill(BLUE)
	draw_text(f'Score: {score}', font, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 100)
    
    # Buttons
	quit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
	restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 50)
    
	pygame.draw.rect(screen, WHITE, quit_button)
	pygame.draw.rect(screen, WHITE, restart_button)
    
	draw_text('Quit', font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 25)
	draw_text('Restart', font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 85)

	draw_text(load_scores(), font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 200)

	# Event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouseX, mouseY = event.pos
			if quit_button.collidepoint(mouseX, mouseY):
				save_score(score)
				running = False
			elif restart_button.collidepoint(mouseX, mouseY):
				save_score(score)
				score = 0
				characters = []
				grid = [[0, 0, 0],
						[0, 0, 0],
						[0, 0, 0]]
				timeUp = False
    
	pygame.display.flip()

# Quit Pygame
pygame.quit()