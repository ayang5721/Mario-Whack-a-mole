import pygame
import random
import time
import config.cellSize
import config.width
import config.height




# Initialize Pygame
pygame.init()

# Screen dimensions

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
pipe_img = pygame.image.load('graphics/pipe.png')
mario_img = pygame.image.load('graphics/marioPipe.png')
pipe_img = pygame.transform.scale(pipe_img, (cellSize, cellSize))
mario_img = pygame.transform.scale(mario_img, (cellSize, cellSize))

# Create screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Whack-a-Mario")

# Font for score
font = pygame.font.Font(None, 36)

# Game variables
score = 0
mario_pos = None
mario_timer = 0

# Function to draw the grid
def draw_grid():
	for row in range(GRID_SIZE):
		for col in range(GRID_SIZE):
			x = col * cellSize
			y = row * cellSize
			screen.blit(pipe_img, (x, y))

# Function to show Mario head
def show_mario():
	global mario_pos, mario_timer
	row = random.randint(0, GRID_SIZE - 1)
	col = random.randint(0, GRID_SIZE - 1)
	mario_pos = (row, col)
	mario_timer = time.time() + random.uniform(0.15, 1.0)

# Main game loop
running = True
show_mario()
while running:
	screen.fill(WHITE)
	draw_grid()

	# Check if Mario head should disappear
	if mario_pos and time.time() > mario_timer:
		mario_pos = None
		show_mario()

	# Draw Mario head
	if mario_pos:
		row, col = mario_pos
		x = col * cellSize
		y = row * cellSize
		screen.blit(mario_img, (x, y))

	# Event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if mario_pos:
				mouse_x, mouse_y = event.pos
				row, col = mario_pos
				x = col * cellSize
				y = row * cellSize
				if x <= mouse_x < x + cellSize and y <= mouse_y < y + cellSize:
					score += 1
					mario_pos = None
					show_mario()

	# Draw score
	score_text = font.render(f"Score: {score}", True, BLACK)
	screen.blit(score_text, (10, 10))

	# Update display
	pygame.display.flip()

# Quit Pygame
pygame.quit()