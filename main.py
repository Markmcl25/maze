import pygame
import sys
from maze import Maze  # You'll create this later
from player import Player  # You'll create this too

# Initialize Pygame
pygame.init()

# Screen settings
TILE_SIZE = 32
MAZE_WIDTH, MAZE_HEIGHT = 25, 20  # 20x15 tiles
SCREEN_WIDTH = MAZE_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAZE_HEIGHT * TILE_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape the Maze")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Timer
START_TIME = 180  # 3 minutes
start_ticks = pygame.time.get_ticks()

# Create maze and player
maze = Maze(MAZE_WIDTH, MAZE_HEIGHT)
player = Player(maze.start_pos, TILE_SIZE)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Timer countdown
    seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
    time_left = max(0, START_TIME - seconds_passed)
    timer_text = font.render(f"Time Left: {time_left}s", True, WHITE)
    screen.blit(timer_text, (10, 10))

    if time_left <= 0:
        game_over_text = font.render("Time's up! You lost!", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player input
    keys = pygame.key.get_pressed()
    player.handle_input(keys, maze)

    # Draw maze and player
    maze.draw(screen, TILE_SIZE)
    player.draw(screen)

    # Check for win
    if player.rect.colliderect(maze.exit_rect):
        win_text = font.render("You escaped!", True, (0, 255, 0))
        screen.blit(win_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
        continue

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
