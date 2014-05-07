### An internal representation of the chess board

#

import numpy as np
import pandas as pd
import util
import pieces

EMPTY_BOARD = pd.DataFrame(index=range(1, 9)[::-1], columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
RUN = False


def initialize_board(board):
  assert board.shape == (8, 8), 'Yo, what? Your board is: {}'.format(board.shape)

  for file in board.columns:
    board[file][2] = pieces.Pawn(board, position=(file, 2), color='w')
    board[file][7] = pieces.Pawn(board, position=(file, 7), color='b')
    board[file][6] = pieces.EmptySquare(board)
    board[file][5] = pieces.EmptySquare(board)
    board[file][4] = pieces.EmptySquare(board)
    board[file][3] = pieces.EmptySquare(board)

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
  if piece.color == None:
    print 'There is no piece there! No move made'
    return board
  if piece.check_legal_move(start, placement):
    util.set_square_to_zero(start)
    piece.move(board, start, placement)
  return board


if __name__ == '__main__' and RUN:
  game_board = initialize_board(EMPTY_BOARD)
  start = ('e', 2) #e4 pawn
  placement = ('e', 4)
  print move_piece(game_board, start, placement)
