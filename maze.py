import pygame
import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[1 for _ in range(width)] for _ in range(height)]
        self.start_pos = (1, 1)
        self.exit_pos = (width - 2, height - 2)
        self.exit_rect = None

        self.generate_maze()

    def generate_maze(self):
        # Start from (1, 1)
        stack = [(1, 1)]
        self.grid[1][1] = 0  # mark as path

        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        while stack:
            x, y = stack[-1]
            random.shuffle(directions)
            moved = False

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1:
                    if self.grid[ny][nx] == 1:
                        self.grid[ny][nx] = 0
                        self.grid[y + dy // 2][x + dx // 2] = 0  # carve path
                        stack.append((nx, ny))
                        moved = True
                        break

            if not moved:
                stack.pop()

        # Define exit
        ex, ey = self.exit_pos
        self.grid[ey][ex] = 0
        self.exit_rect = pygame.Rect(ex * 32, ey * 32, 32, 32)

    def is_walkable(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x] == 0
        return False

    def draw(self, surface, tile_size):
        for y in range(self.height):
            for x in range(self.width):
                color = (255, 255, 255) if self.grid[y][x] == 0 else (50, 50, 50)
                pygame.draw.rect(
                    surface,
                    color,
                    pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                )

        # Draw exit tile in green
        pygame.draw.rect(surface, (0, 255, 0), self.exit_rect)
