import pygame
from sudoku.Square import Square
from sudoku.Constants import WIN_WIDTH, WIN_HEIGHT, SQUARE_SIZE, WHITE, BLACK

class Sudoku:
    def __init__(self, win, starting_board):
        self.win = win
        self.rows = len(starting_board)
        self.cols = len(starting_board[0])
        self.board = [[Square(self.win, starting_board[i][j], i, j) for j in range(self.cols)] for i in range(self.rows)]


    def solve(self):
        pass

    def isValid(self):
        pass

    def first_empty_square(self):
        pass

    def draw(self):
        self.win.fill(WHITE)
        self.draw_lines()
        self.draw_squares()
        pygame.display.update()

    def draw_lines(self):
        for i in range(len(self.board) + 1):
            if i == 0 or i % 3 == 0:
                thickness = 6
            else:
                thickness = 1
            pygame.draw.line(self.win, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIN_HEIGHT), thickness)
            pygame.draw.line(self.win, BLACK, (0, i * SQUARE_SIZE), (WIN_WIDTH, i * SQUARE_SIZE), thickness)

    def draw_squares(self):
        for row in self.board:
            for square in row:
                if square.value != 0:
                    square.draw()
