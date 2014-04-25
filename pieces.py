import util

class Pawns(object):

  def __init__(self, position, color):
    self.current_position = position
    self.color = color
    self.taken_two_steps == False


  def __repr__(self):
    return self.color + 'P'


  def check_legal_move(self, start, placement):
    # checks that pawns can only move forward 1 step
    if self.color == 'w':
      if placement[1] > start[1]: # move forward
        if taken_two_steps: # no longer two moves
           if (placement[1] - start[1] == 1):
            return True
        else:
          if (placement[1] - start[1] < 3):
            return True
    elif self.color == 'b':
      if start[1] > placement[1]: # move forward
        if taken_two_steps: # no longer two moves
           if (start[1] - placement[1] == 1):
            return True
        else:
          if (start[1] - placement[1] < 3):
            return True
    return False


  def move(self, board, start, placement):
    if self.check_legal_move(start, placement):
      util.set_square_to_zero(start)
      board[placement[0]][placement[1]] = self
      self.current_position = placement
    else:
      print "Invalid move! Move not made."
