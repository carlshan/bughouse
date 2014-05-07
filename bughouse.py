### An internal representation of the chess board

#

import numpy as np
import pandas as pd

EMPTY_BOARD = pd.DataFrame(index=range(1, 9)[::-1], columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
RUN = True

def initialize_board(board):
  assert board.shape == (8, 8), 'Yo, what? Your board is: {}'.format(board.shape)

  # White Pieces
  for file in board.columns:
    for rank in range(1, 3):
      board[file][rank] = 1

  # Black Pieces
  for file in board.columns:
    for rank in range(7, 9):
      board[file][rank] = -1

  return board


def get_color_of_piece_on_square(board, rank, file):
  return board[file][rank]


def get_piece_on_square(board, rank, file):
  # should have different implementation
  # need to figure out representation of pieces on board
  return board[file][rank]


def move_piece(board, start, placement):
  # start and placement are both tuples of file and rank
  starting_piece_color = board[start[0]][start[1]]
  placement_piece_color = board[placement[0]][placement[1]]
  assert starting_piece_color != 0 and starting_piece_color != placement_piece_color, 'You cannot move there'
  board[start[0]][start[1]] = 0
  board[placement[0]][placement[1]] = starting_piece_color
  return board


if __name__ == '__main__' and RUN:
  game_board = initialize_board(EMPTY_BOARD)
  start = ('e', 2) #e4 pawn
  placement = ('e', 4)
  print move_piece(game_board, start, placement)
