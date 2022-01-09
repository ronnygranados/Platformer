import pygame
from tiles import Tile
from settings import TILE_SIZE
from player import Player


class Level:
    def __init__(self, level_data, surface):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if cell == 'X':
                    tile = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def run(self):
        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # player
        self.player.update()
        self.player.draw(self.display_surface)
