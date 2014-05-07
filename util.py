def get_color_of_piece_on_square(board, position):
  # should have different implementation
  # need to figure out representation of pieces on board
  file = position[0]
  rank = position[1]
  return board[file][rank].color


def get_piece_on_square(board, position):
  # should have different implementation
  # need to figure out representation of pieces on board
  file = position[0]
  rank = position[1]
  return board[file][rank]


def set_square_to_zero(board, square_position):
  board[square_position[0]][square_position[1]] = 0
  return board
