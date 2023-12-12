import pygame as py
import numpy as np
import random, string, sys

class Cell():
    def __init__(self, screen):
        self.screen = screen
        self.gs = 25
        self.cells = np.zeros((self.gs, self.gs), dtype=np.int64)
        self.nextcells = np.copy(self.cells)
        self.showL = False
        self.start = False
        self.temp = None
    
    def showGrid(self):
        color = (255, 0, 0) if self.start else (0, 0, 0)
        for i in range(2):
            for j in range(0, 500, self.gs):
                if i == 0:
                    py.draw.line(self.screen, color, (j, 0), (j, 500), 2)
                else:
                    py.draw.line(self.screen, color, (0, j), (500, j), 2)
    
    def showCells(self):
        gs = self.gs
        for i in range(gs):
            for j in range(gs):
                if self.nextcells[i][j] == 0:
                    py.draw.rect(self.screen, (255, 255, 255), (i*gs, j*gs, gs, gs))
                else:
                    py.draw.rect(self.screen, (0, 0, 0), (i*gs, j*gs, gs, gs))

    def shift(self):
        self.nextcells = np.copy(self.cells)
        for i in range(self.gs):
            for j in range(self.gs):
                if (j < 24 and i < 24) and self.start:
                    self.temp = np.copy(self.cells[i-1:i+2, j-1:j+2])
                    population = sum(self.temp.flatten())
                    if self.cells[i][j] == 1:
                        population -= 1
                        if population < 2 or population > 3:
                            self.nextcells[i][j] = 0
                    elif self.cells[i][j] == 0 and population == 3:
                        self.nextcells[i][j] = 1
        self.cells = np.copy(self.nextcells)

    def random(self, event):
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                for i in range(150):
                    self.cells[random.randrange(0, 25)][random.randrange(0, 25)] = 1
            if event.key == py.K_RETURN:
                self.start = not self.start

            if py.key.get_pressed()[py.K_LCTRL]:
                if py.key.get_pressed()[py.K_z]:
                    self.cells.fill(0)
                elif py.key.get_pressed()[py.K_w]:
                    sys.exit()
                elif py.key.get_pressed()[py.K_q]:
                    print(self.temp)

    def selected(self, event):
        mx, my = py.mouse.get_pos()
        mx, my = mx//25, my//25
        if mx >= 0 and mx <= 25 and my >= 0 and my <= 25 and py.mouse.get_pressed()[0]:
            self.cells[mx][my] = 1
        if mx >= 0 and mx <= 25 and my >= 0 and my <= 25 and py.mouse.get_pressed()[2]:
            self.cells[mx][my] = 0

    def eventHandler(self, event):
        self.random(event)
        self.selected(event)