from pieces import Position, EmptySquare

def get_color_of_piece_on_square(board, position):
  assert isinstance(position, Position)
  file = position.file
  rank = position.rank
  return board[file][rank].color


def get_piece_on_square(board, position):
  assert isinstance(position, Position)
  file = position.file
  rank = position.rank
  return board[file][rank]


def set_square_to_empty(board, position):
  assert isinstance(position, Position)
  file = position.file
  rank = position.rank
  board[file][rank] = EmptySquare(board)
  return board
