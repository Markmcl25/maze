import pygame

class Player:
    def __init__(self, start_pos, tile_size):
        self.tile_size = tile_size
        self.x, self.y = start_pos
        self.rect = pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)
        self.color = (0, 0, 255)  # Blue player

    def handle_input(self, keys, maze):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1

        new_x = self.x + dx
        new_y = self.y + dy

        if maze.is_walkable(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.rect.topleft = (self.x * self.tile_size, self.y * self.tile_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
