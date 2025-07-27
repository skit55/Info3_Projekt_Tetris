import pygame
from colors import Colors

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, r,c):
        self.row_offset += r
        self.column_offset += c
    
    #pos + offset
    def get_cell_positions(self):
        current = self.cells[self.rotation_state]
        final = []
        for r,c in current:
            final.append((r+self.row_offset, c+self.column_offset))
        return final
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0: 
            self.rotation_state = len(self.cells) - 1

    #draws every cell of the block
    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile[1] * self.cell_size, offset_y + tile[0] * self.cell_size,
                                     self.cell_size - 1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)