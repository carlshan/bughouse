### An internal representation of the chess board

#

import numpy as np
import pandas as pd
import util


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


def move_piece(board, start, placement):
  # start and placement are both tuples of file and rank
  # move_piece(game_board, start=('e', 2), placement=('e', 4))
  # checks that placement is on the board
  # invokes move method of each piece to check for valid moves
  if placement[0] != board.columns or placement[1] not in board.index:
    print 'You are moving off the board Move not made.'
    return board
  piece = util.get_piece_on_board(board, start)
  if piece == empty_piece:

  if piece.check_legal_move(start, placement):
    util.set_square_to_zero(start)
    piece.move(board, start, placement)
  return board


  starting_piece_color = board[start[0]][start[1]]
  placement_piece_color = board[placement[0]][placement[1]]
  assert starting_piece_color != 0, 'There is no piece there!'
  assert starting_piece_color != placement_piece_color, 'You cannot move on top of your own piece'
  board[start[0]][start[1]] = 0
  board[placement[0]][placement[1]] = starting_piece_color
  return board


if __name__ == '__main__' and RUN:
  game_board = initialize_board(EMPTY_BOARD)
  start = ('e', 2) #e4 pawn
  placement = ('e', 4)
  print move_piece(game_board, start, placement)
