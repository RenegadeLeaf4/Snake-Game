import pygame
import sys
import random
pygame.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

FPS = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

MAIN_FONT = pygame.font.SysFont("helvetica", 40)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BLACK = (0, 0, 0)
WHITE =  (255, 255, 255)
RED = (255, 0, 0)
SILVER = (240, 255, 240)
CORAL = (240, 128, 128)
LIGHT_BLUE = (173, 239, 209)
LIGHT_GREY = (96, 106, 116)
DARK_GREY = (33, 41, 48)

clock = pygame.time.Clock()

class Snake():
	def __init__(self, score):
		self.position = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]


		self.length = 1
		self.direction = UP
		self.block = GRID_SIZE

		self.score = score

	def move(self):
		head_pos = self.position[0]
		dir_x, dir_y = self.direction
		self.new = (((head_pos[0] + (dir_x * GRID_SIZE)) % SCREEN_WIDTH), (head_pos[1] + (dir_y * GRID_SIZE)) % SCREEN_HEIGHT)
		if len(self.position) > 1 and self.new in self.position:
			self.reset()
		else:
			self.position.insert(0, self.new)
			if len(self.position) > self.length:
				self.position.pop()

	def turn(self, direction):
		self.direction = direction

	def reset(self):
		self.position = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
		self.length = 1
		self.direction = UP
		self.score = 0

	def draw(self, screen):
		for position in self.position:
			self.rect = pygame.Rect((position[0], position[1]), (self.block, self.block))
			pygame.draw.rect(screen, LIGHT_BLUE, self.rect)
			pygame.draw.rect(screen, LIGHT_GREY, self.rect, 1)

class Food():
	def __init__(self):
		self.position = (random.randint(0, GRID_WIDTH- 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

		self.block = GRID_SIZE

	def reset_pos(self):
		self.position = (random.randint(0, GRID_WIDTH- 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

	def draw(self, screen):
		self.rect = pygame.Rect((self.position[0], self.position[1]), (self.block, self.block))
		pygame.draw.rect(screen, CORAL, self.rect)
		pygame.draw.rect(screen, RED, self.rect, 1)

def main():
	run = True
	score = 0

	snake = Snake(score)
	food = Food()

	def draw_grid(screen):
		for y in range(int(GRID_HEIGHT)):
			for x in range(int(GRID_WIDTH)):
				if (x + y) % 2 == 0:
					light_rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
					pygame.draw.rect(screen, LIGHT_GREY, light_rect)
				else:
					dark_rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
					pygame.draw.rect(screen, DARK_GREY, dark_rect)

	def redraw_game_win(self):
		draw_grid(screen)
		snake.draw(screen)
		food.draw(screen)

		score_text = MAIN_FONT.render(str(snake.score), 1, SILVER)
		screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, 10))
        
		pygame.display.update()

	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		snake.move()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP] and snake.direction != DOWN: 
			snake.direction = UP
		elif keys[pygame.K_DOWN] and snake.direction != UP:
			snake.direction = DOWN
		elif keys[pygame.K_LEFT] and snake.direction != RIGHT: 
			snake.direction = LEFT
		elif keys[pygame.K_RIGHT] and snake.direction != LEFT: 
			snake.direction = RIGHT

		if snake.position[0] == food.position:
			snake.length += 1
			snake.score += 1
			food.reset_pos()

		redraw_game_win(screen)
main()