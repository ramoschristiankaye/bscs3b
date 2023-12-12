import sys, cell
import pygame as py
py.init()

screen = py.display.set_mode((500, 500))
py.display.set_caption("Game of Life")
clock = py.time.Clock()

cells = cell.Cell(screen)

while True:
    clock.tick(24)
    screen.fill((255, 0, 0))
    
    cells.showCells()
    cells.shift()
    cells.showGrid()

    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()

        cells.eventHandler(event)

    py.display.flip()