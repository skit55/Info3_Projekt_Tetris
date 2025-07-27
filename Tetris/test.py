import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Grid Tetris")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.tick(60)

    rows = 20
    columns = 10
    cell_size = 30

    for row in range(rows):
        for column in range(columns):
            cell_rect = pygame.Rect(column*cell_size+1, row * cell_size+1, cell_size-1, cell_size-1)
            pygame.draw.rect(screen, (255, 255, 255), cell_rect)
            

            