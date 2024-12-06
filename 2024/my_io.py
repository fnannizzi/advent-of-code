def convert_to_array_matrix(input):
  matrix = []
  for line in input:
    # drop the newline characters before appending to matrix
    matrix.append(list(line[:-1]))

  return matrix

def read_input(filename):
  with open(filename, 'r', encoding="utf-8") as file:
    lines = file.readlines()
    return lines
