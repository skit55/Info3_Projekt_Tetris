from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("Tetris/Sound/rotate.wav")
        self.clear_sound = pygame.mixer.Sound("Tetris/Sound/clear.mp3")
        self.game_over_played = False
        with open("Tetris\highscore.txt","r") as file:
            self.highscore = int(file.read())

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points
        
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0, -1)
        passt = self.block_inside()
        if passt == True:
            if self.block_fits() == False:
                self.current_block.move(0,1)
        else: 
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0, 1)
        passt = self.block_inside()
        if passt == True:
            if self.block_fits() == False:
                self.current_block.move(0,-1)
        else: 
            self.current_block.move(0,-1)

    def move_down(self):
        self.current_block.move(1, 0)
        passt = self.block_inside()
        if passt == True:
            if self.block_fits() == False:
                self.current_block.move(-1,0)
                self.lock_block()
        else: 
            self.current_block.move(-1,0)
            self.lock_block()

    def save_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Tetris\highscore.txt", "w") as file:    
                file.write(str(self.highscore))

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for pos in tiles:
            self.grid.grid[pos[0]][pos[1]] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()

        if not self.block_fits():
            self.game_over = True
            self.save_highscore()
            return
        rows = self.grid.clear_full_rows()
        if rows >0:
            self.clear_sound.play()
            self.update_score(rows, 0)

    def restart(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.game_over_played = False

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            row, col = tile
            if self.grid.is_empty(row, col) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile[0], tile[1]) == False:
                return False
        return True
        
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        #diffrent start point for diffrent blocks
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 405)
        elif self.next_block.id ==4:
            self.next_block.draw(screen, 255, 395)
        else:
            self.next_block.draw(screen, 270, 385)