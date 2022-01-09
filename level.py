import pygame
from tiles import Tile
from settings import TILE_SIZE


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        # self.level_data = level_data
        self.tiles = pygame.sprite.Group()

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'X':
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    tile = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.draw(self.display_surface)
