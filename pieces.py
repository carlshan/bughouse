import util
from util import *

class Position(object):

  def __init__(self, board, movement):
    self.board = board
    if type(movement) not in (tuple, list):
      raise TypeError, 'Movements must be passed as tuple or list'
    if movement[0] not in board.columns or movement[1] not in board.index:
      raise TypeError, 'Invalid movement'
    self.file = movement[0]
    self.rank = movement[1]



class EmptySquare(object):

  def __init__(self, board):
    self.color = None

  def __repr__(self):
    return '-'


class ChessPiece(object):

  def move(self, board, start, placement):
    util.set_square_to_empty(board, start)
    board[placement.file][placement.rank] = self
    self.current_position = placement



class Pawn(ChessPiece):

  def __init__(self, board, position, color):
    self.board = board
    self.color = color
    self.current_position = position
    self.taken_two_steps = False


  def __repr__(self):
    return self.color + 'P'


  def check_legal_move(self, board, start, placement):
    # TBD: Checks that pawns can take on diagonals
    placement_piece = get_piece_on_square(board, placement)
    if self.color == placement_piece.color:
      # print 'You have two pieces of the same color on: {start} and {placement}'.format(start=start, placement=placement)
      return False
    if self.color == 'w':
      if placement[1] > start[1]: # moving forward
        if self.taken_two_steps: # no longer two moves
          if (placement[1] - start[1] == 1): # doesn't take into account if there's a piece in the way!
            return True
        else:
          if isinstance(get_piece_on_square(board, (placement[0], placement[1]+1)), EmptySquare):
            return True
          else:
            self.taken_two_steps = True
            if (placement[1] - start[1] < 3):
              return True
    elif self.color == 'b':
      if start[1] > placement[1]: # move forward
        if self.taken_two_steps: # no longer two moves
           if (start[1] - placement[1] == 1):
            return True
        else:
          if isinstance(get_piece_on_square(board, (placement[0], placement[1]-1)), EmptySquare):
            return True
          else:
            self.taken_two_steps = True
            if (start[1] - placement[1] < 3):
              return True
    return False


class Rook(ChessPiece):

  def __init__(self, board, position, color):
    self.board = board
    self.current_position = position
    self.color = color
    self.taken_two_steps = False


  def __repr__(self):
    return self.color + 'R'


  def check_legal_move(self, board, start, placement):
    placement_piece = get_piece_on_square(board, placement)
    if self.color == placement_piece.color:
      pass
    elif start[0] == placement[0]: # same file
      if start[1] + 1 == placement[1]:
        return True
      elif start[1] + 1 < placement[1]: # moving forward
        for rank in range(start[1]+1, placement[1]): # checking pieces in way
          if get_piece_on_square(board, (start[0], rank)).color != None:
            return False
        return True
      else: # moving backwards
        for rank in range(placement[1]+1, start[1]):
          if get_piece_on_square(board, (start[0], rank)).color != None:
            return False
        return True
    elif start[1] == placement[1]: # same rank
      if char(ord(start[0])+1) == placement[0]:
        return True
      elif char(ord(start[0])+1) < placement[0]: # moving towards H file
        for file in range(ord(start[0]+1, ord(placement[0]))):
          if get_piece_on_square(board, (chr(file), start[1])).color != None:
            return False
        return True
      else: # moving towards A file
        for file in range(ord(placement[0]+1, ord(start[0]))):
          if get_piece_on_square(board, (chr(file), start[1])).color != None:
            return False
        return True
    return False

class Knight(ChessPiece):

  def __init__(self, board, position, color):
    self.board = board
    self.color = color
    self.current_position = position


  def __repr__(self):
    return self.color + 'N'


class Bishop(ChessPiece):

  def __init__(self, board, position, color):
    self.board = board
    self.color = color
    self.current_position = position


  def __repr__(self):
    return self.color + 'B'


class Queen(ChessPiece):

  def __init__(self, board, position, color):
    self.board = board
    self.color = color
    self.current_position = position
    self.taken_two_steps = False


  def __repr__(self):
    return self.color + 'Q'


class King(ChessPiece):

  def __init__(self, board, position, color):
    self.board = board
    self.color = color
    self.current_position = position
    self.taken_two_steps = False


  def __repr__(self):
    return self.color + 'K'
