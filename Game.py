import numpy as np
import pygame
import sys
import math
from threading import Timer
import random

# colors for GUI
BLUE = (0, 0, 255) # FRAME
BLACK = (0, 0, 0) # BACKGROUND
RED = (255, 0, 0) # AI
YELLOW = (255, 255, 0)

class Connect_4:
    def __init__(self, rows = 10, column = 10, sq_size = 40, color = YELLOW):
        self.Rows = rows
        self.Column = column
        self.SqSize = sq_size
        self.Color = color

        self.Player_Turn = 0
        self.AI_Turn = 1
        self.Player_Piece = 1
        self.AI_Piece = 2

        self.Width = self.Column * self.SqSize
        self.Height = (self.Rows + 1) * self.SqSize
        self.Circle_Radius = int(self.SqSize / 2 - 4)
        self.Size = (self.Width, self.Height)
        self.Screen = pygame.display.set_mode(self.Size)

        # Test Code:
        pygame.init()
        self.Font = pygame.font.SysFont("Bebas Neue", 50)
        self.board = self.create_board()
        self.game_over = False # initially no one won the game.
        self.not_over = True
        self.turn = random.randint(self.Player_Turn, self.AI_Turn)

        self.draw_frame(self.board)
        pygame.display.update()

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # WINDOW CROSS
                    sys.exit()

                if event.type == pygame.MOUSEMOTION and self.not_over:  # Hovering Top
                    pygame.draw.rect(self.Screen, BLACK, (0, 0, self.Width, self.SqSize))
                    x_position = pygame.mouse.get_pos()[0]
                    if self.turn == self.Player_Turn:
                        pygame.draw.circle(self.Screen, self.Color, (x_position, int(self.SqSize / 2)), self.Circle_Radius)

                if event.type == pygame.MOUSEBUTTONDOWN and self.not_over: # if player clicks the button, drop piece down.
                    pygame.draw.rect(self.Screen, BLACK, (0, 0, self.Width, self.SqSize))
                    if self.turn == self.Player_Turn:
                        x_position = event.pos[0]
                        col = int(math.floor(x_position / self.SqSize))

                        if self.is_valid_column_location(self.board, col):
                            row = self.get_next_free_row(self.board, col)
                            self.drop_piece(self.board, row, col, self.Player_Piece)
                            if self.is_winning_move(self.board, self.Player_Piece):
                                label = self.Font.render("YOU WON!", True, BLUE)
                                self.Screen.blit(label, (40, 10))
                                self.not_over = False
                                t = Timer(5, self.end_game)
                                t.start()
                        self.draw_frame(self.board)
                        self.turn += 1 # increment turn by 1
                        self.turn = self.turn % 2 # this will alternate between 0 and 1 with every turn
                pygame.display.update()

            if self.turn == self.AI_Turn and not self.game_over and self.not_over: # the column to drop in is found using algorithm
                col, minimax_score = self.minimax_algorithm(self.board, 5, -math.inf, math.inf, True)
                if self.is_valid_column_location(self.board, col):
                    pygame.time.wait(10)
                    row = self.get_next_free_row(self.board, col)
                    self.drop_piece(self.board, row, col, self.AI_Piece)
                    if self.is_winning_move(self.board, self.AI_Piece):
                        label = self.Font.render("YOU LOST", True, BLUE) # AI WON
                        self.Screen.blit(label, (20, 10))
                        self.not_over = False
                        t = Timer(5, self.end_game)
                        t.start()
                self.draw_frame(self.board)
                self.turn += 1
                self.turn = self.turn % 2

    def create_board(self):
        self.board = np.zeros((self.Rows, self.Column))
        return self.board

    @staticmethod
    def drop_piece(board, row, col, piece):
        board[row][col] = piece

    @staticmethod
    def is_valid_column_location(board, col):
        return board[0][col] == 0

    def get_next_free_row(self, board, col):
        for an_row in range(self.Rows - 1, -1, -1): # INVERT
            if board[an_row][col] == 0:
                return an_row

    def is_winning_move(self, board, piece):
        for c in range(self.Column - 3):
            for r in range(self.Rows):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                    return True
        for c in range(self.Column):
            for r in range(self.Rows - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                    return True
        for c in range(self.Column - 3):
            for r in range(3, self.Rows):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                    return True
        for c in range(3, self.Column):
            for r in range(3, self.Rows):
                if board[r][c] == piece and board[r - 1][c - 1] == piece and board[r - 2][c - 2] == piece and board[r - 3][c - 3] == piece:
                    return True

    def draw_frame(self, board):
        Size = self.SqSize
        for column in range(self.Column):
            for row in range(self.Rows):
                pygame.draw.rect(self.Screen, BLUE, (column * Size, row * Size + Size, Size, Size))
                if board[row][column] == 0:
                    pygame.draw.circle(self.Screen, BLACK, (int(column * Size + Size/2), int(row * Size + Size + Size/2)), self.Circle_Radius)
                elif board[row][column] == 1:
                    pygame.draw.circle(self.Screen, self.Color, (int(column * Size + Size/2), int(row * Size + Size + Size/2)), self.Circle_Radius)
                else:
                    pygame.draw.circle(self.Screen, RED, (int(column * Size + Size/2), int(row * Size + Size + Size/2)), self.Circle_Radius)
        pygame.display.update()

    def get_valid_places(self, board): # get all the columns where a piece can be placed.
        valid_locations = []
        for column in range(self.Column):
            if self.is_valid_column_location(board, column):
                valid_locations.append(column)
        return valid_locations

    def window_evaluation(self, window, piece):
        # by default the opponent is the player
        opponent_piece = self.Player_Piece
        if piece == self.Player_Piece:
            opponent_piece = self.AI_Piece
        score = 0  # initial score of a window is 0
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 50
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 30
        if window.count(opponent_piece) == 3 and window.count(0) == 1:
            score -= 30
        return score

    def each_position_score(self, board, piece):
        score = 0
        center_array = [int(i) for i in list(board[:, self.Column // 2])]
        center_count = center_array.count(piece)
        score += center_count * 6
        for r in range(self.Rows): # horizontal
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(self.Column - 3):
                window = row_array[c:c + 4]
                score += self.window_evaluation(window, piece)
        for c in range(self.Column):   # vertical
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(self.Rows - 3):
                window = col_array[r:r + 4]
                score += self.window_evaluation(window, piece)
        for r in range(3, self.Rows): # +ve sloped
            for c in range(self.Column - 3):
                window = [board[r - i][c + i] for i in range(4)]
                score += self.window_evaluation(window, piece)
        for r in range(3, self.Rows): # -ve sloped
            for c in range(3, self.Column):
                window = [board[r - i][c - i] for i in range(4)]
                score += self.window_evaluation(window, piece)
        return score

    def is_node_terminal(self, board):
        return self.is_winning_move(board, self.Player_Piece) or self.is_winning_move(board, self.AI_Piece) or len(self.get_valid_places(board)) == 0

    def minimax_algorithm(self, board, depth, a_value, b_value, maximizing_player):
        valid_locations = self.get_valid_places(board) # all valid locations on board
        is_terminal = self.is_node_terminal(board)
        if depth == 0 or is_terminal:
            if is_terminal:  # winning move
                if self.is_winning_move(board, self.AI_Piece): return None, 10000000
                elif self.is_winning_move(board, self.Player_Piece): return None, -10000000
                else: return None, 0
            else:  return None, self.each_position_score(board, self.AI_Piece)

        if maximizing_player: # AI
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_free_row(board, col)
                board_copy = board.copy()
                self.drop_piece(board_copy, row, col, self.AI_Piece)
                new_score = self.minimax_algorithm(board_copy, depth - 1, a_value, b_value, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                a_value = max(value, a_value)
                if a_value >= b_value:
                    break
            return column, value

        else:  # USER
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_free_row(board, col)
                board_copy = board.copy()
                self.drop_piece(board_copy, row, col, self.Player_Piece)
                new_score = self.minimax_algorithm(board_copy, depth - 1, a_value, b_value, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                b_value = min(value, b_value)
                if a_value >= b_value: break
            return column, value

    def end_game(self):
        self.game_over = True