import pygame
from sudoku.Constants import WIN_WIDTH, WIN_HEIGHT, SQUARE_SIZE, FONT, WHITE, BLACK

class Square:
    def __init__(self, win, value, row, col):
        self.win = win
        self.value = value
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.get_pos()

    def get_pos(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def set_value(self,value):
        self.value = value

    def get_value(self):
        return self.value

    def draw(self):
        text = FONT.render(str(self.value), True, BLACK)
        rect = text.get_rect(center = (self.x, self.y))
        self.win.blit(text, rect)

    def draw_change(self):
        pass