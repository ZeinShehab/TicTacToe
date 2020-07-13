import pygame
import os
import sys
import time

pygame.init()
pygame.font.init()
pygame.display.set_caption('TIC TAC TOE!')

# GLOBAL CONSTANTS
BLOCK_SIZE = 100 
MARGIN = 50

# GAME WINDOW
WIDTH = 500
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# COLORS
O_COLOR = (155,0,0)
X_COLOR = (0,0,155)
TEXT_COLOR = (155,0,0)

# LOADING IMAGES
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/Images", "bg.png")), (WIDTH, HEIGHT-100))

# LOADING FONTS
NUM_FONT = pygame.font.Font(os.path.join("assets/Montserrat", "Montserrat-Light.ttf"), 200)
WIN_FONT = pygame.font.Font(os.path.join("assets/Montserrat", "Montserrat-Medium.ttf"), 100)

turn = 1
grid = [[0,0,0],
		[0,0,0],
		[0,0,0]]


def show_letters():
	for column in range(3):
		for row in range(3):
			x = (MARGIN + BLOCK_SIZE) * column + MARGIN
			y = (MARGIN + BLOCK_SIZE) * row + MARGIN - 20

			text = NUM_FONT.render("",1,(0,0,0))
			if grid[row][column] == 1:
				text = NUM_FONT.render("o", 1, O_COLOR)
			elif grid[row][column] == 2:
				text = NUM_FONT.render("x", 1, X_COLOR)

			text_rect = text.get_rect()
			text_rect.x = int(x + (BLOCK_SIZE/2) - text_rect.width/2)
			text_rect.y = int(y + (BLOCK_SIZE/2) - text_rect.height/2)


			WIN.blit(text, (text_rect.x,text_rect.y))


def show_line():
	pass


def show_scores():
	pass


def on_click():
	global grid, turn

	pos = pygame.mouse.get_pos()
	column = pos[0] // (BLOCK_SIZE + MARGIN)
	row = pos[1] // (BLOCK_SIZE + MARGIN)

	if row < 3 and column < 3:
		if turn % 2 != 0:
			if grid[row][column] != 1 and grid[row][column] != 2:
				grid[row][column] = 2
				turn += 1
		else:
			if grid[row][column] != 2 and grid[row][column] != 1:
				grid[row][column] = 1
				turn += 1


def logic():
	for i in range(3):
		# HORIZONTAL
		if grid[i].count(1) == 3:
			return 0
		if grid[i].count(2) == 3:
			return 1

		# VERTICAL
		if grid[0][i] == grid[1][i] and grid[0][i] == grid[2][i]:
			if grid[0][i] == 1:
				return 0
			if grid[0][i] == 2:
				return 1

	if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2]:
		if grid[0][0] == 1:
			return 0
		if grid[0][0] == 2:
			return 1

	if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0]:
		if grid[0][2] == 1:
			return 0
		if grid[0][2] == 2:
			return 1	


def main():
	global grid, turn, O_COLOR, X_COLOR

	run =  True
	
	while run:
		WIN.blit(BG, (0, 0))

		show_letters()
		winner = logic()

		win_text = WIN_FONT.render("", 1, TEXT_COLOR)
		if winner == 1:
			win_text = WIN_FONT.render("X WINS", 1, TEXT_COLOR)
			O_COLOR = (200,200,200)
			X_COLOR = (200,200,200)
		elif winner == 0:
			O_COLOR = (200,200,200)
			X_COLOR = (200,200,200)
			win_text = WIN_FONT.render("O WINS", 1, TEXT_COLOR)

		if winner == 1 or winner == 0:
			win_text_rect = win_text.get_rect()
			win_text_rect.x = int(WIDTH / 2 - win_text_rect.width / 2)
			win_text_rect.y = int(HEIGHT / 2 - win_text_rect.height / 2) 
			
			show_letters()
			WIN.blit(win_text, (win_text_rect.x, win_text_rect.y))

			pygame.display.flip()

			O_COLOR = (155,0,0)
			X_COLOR = (0,0,155)

			time.sleep(2)

			run = False
			turn = 1
			grid = [[0,0,0],
					[0,0,0],
					[0,0,0]]
			main()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				on_click()

		pygame.display.flip()
main()