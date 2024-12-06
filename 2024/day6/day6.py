from my_io import read_input, convert_to_array_matrix

class GuardPath:

  GUARD = '^'
  OBSTACLE = '#'
  EMPTY = '.'

  def __init__(self, map):
    self.map = map
    self.map_rows = len(map)
    self.map_cols = len(map[0])

  def traverse_map(self, map):
    for row_i in range(self.map_rows):
      for col_i in range(self.map_cols):
        yield row_i, col_i

  def locate_guard(self, map):
    for row_i, col_i in self.traverse_map(map):
      if map[row_i][col_i] == self.GUARD:
        return row_i, col_i

    # nobody here!
    return -1, -1

  def 

def part_one(map):


def part_two():
  pass

if __name__ == '__main__':
  map = convert_to_array_matrix(read_input(read_input('input.txt')))
  part_one(map)
  # part_two(rules, updates)
