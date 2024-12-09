def convert_to_array_matrix(input):
  matrix = []
  for line in input:
    # drop the newline characters before appending to matrix
    matrix.append(list(line[:-1]))

  return matrix

def traverse_grid(num_rows: int, num_cols: int):
  for row_i in range(num_rows):
    for col_i in range(num_cols):
      yield row_i, col_i

class Position:
  def __init__(self, row_i: int, col_i: int):
    self.row_i = row_i
    self.col_i = col_i

  def to_string(self):
    return str(self.row_i) + "," + str(self.col_i)

  @staticmethod
  def from_string(string: str):
    coordinates = string.split(",")
    return Position(int(coordinates[0]), int(coordinates[1]))
