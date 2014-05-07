import unittest
import bughouse
import pieces
from util import *
from bughouse import initialize_board, EMPTY_BOARD


class PawnUnitTests(unittest.TestCase):
  def setUp(self):
    self.board = initialize_board(EMPTY_BOARD.copy())


  def test_cannot_move_more_than_two_squares(self):
    e2 = get_piece_on_square(self.board, position=('e', 2))
    self.assertFalse(e2.check_legal_move(self.board, e2.current_position, ('e', 5)))


  def test_cannot_move_on_top_of_own_piece(self):
    e2 = get_piece_on_square(self.board, position=('e', 2))
    self.board['e'][4] = pieces.Pawn(self.board, position=('e', 4), color='w')
    self.assertFalse(e2.check_legal_move(self.board, e2.current_position, ('e', 4)))


  def test_can_move_two_squares_once(self):
    e2 = pieces.Pawn(self.board, position=('e', 2), color='w')
    self.assertTrue(e2.check_legal_move(self.board, e2.current_position, ('e', 4)))


  def test_cannot_move_two_squares_twice(self):
    e2 = pieces.Pawn(self.board, position=('e', 2), color='w')
    e2.move(self.board, e2.current_position, ('e', 4))
    self.assertFalse(e2.check_legal_move(self.board, e2.current_position, ('e', 6)))


  def test_white_pawn_cannot_move_backwards(self):
    self.board['e'][4] = pieces.Pawn(self.board, ('e', 4), 'w')
    e4 = get_piece_on_square(self.board, position=('e', 4))
    self.assertFalse(e4.check_legal_move(self.board, e4.current_position, ('e', 3)))


  def test_black_pawn_cannot_move_backwards(self):
    self.board['e'][5] = pieces.Pawn(self.board, ('e', 5), 'b')
    e5 = get_piece_on_square(self.board, position=('e', 5))
    self.assertFalse(e5.check_legal_move(self.board, e5.current_position, ('e', 6)))

  def test_cannot_move_laterally(self):
    pass

  def test_cannot_take_on_empty_square(self):
    pass


class RookUnitTests(unittest.TestCase):

  def setUp(self):
    self.board = EMPTY_BOARD.copy()


  def test_rook_cannot_take_own_color(self):
    rook = pieces.Rook(board=self.board, position=('a', 1), color='w')
    pawn = pieces.Pawn(board=self.board, position = ('a', 2), color='w')
    self.board['a'][1] = rook
    self.board['a'][2] = pawn
    self.assertFalse(rook.check_legal_move(rook.board, rook.current_position, pawn.current_position))


  def test_rook_can_take_opposite_color(self):
    rook = pieces.Rook(board=self.board, position=('a', 1), color='w')
    pawn = pieces.Pawn(board=self.board, position = ('a', 2), color='b')
    self.board['a'][1] = rook
    self.board['a'][2] = pawn
    print self.board
    self.assertTrue(rook.check_legal_move(rook.board, rook.current_position, pawn.current_position))
