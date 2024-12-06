from my_io import read_input, convert_to_array_matrix

search_length_xmas = 4
XMAS = ['X', 'M', 'A', 'S']

def search_horizontal(wordsearch, x_col_i, x_row_i):
  assert wordsearch[x_col_i][x_row_i] == 'X'
  backwards_xmas = True
  forwards_xmas = True
  for i in range(1, search_length_xmas):
    if (x_row_i - i < 0) or (backwards_xmas and wordsearch[x_col_i][x_row_i - i] != XMAS[i]):
      backwards_xmas = False
    if (x_row_i + i >= len(wordsearch[x_col_i])) or (forwards_xmas and wordsearch[x_col_i][x_row_i + i] != XMAS[i]):
      forwards_xmas = False

    if not backwards_xmas and not forwards_xmas:
      return 0

  return sum([backwards_xmas, forwards_xmas])

def search_vertical(wordsearch, x_col_i, x_row_i):
  assert wordsearch[x_col_i][x_row_i] == 'X'
  downwards_xmas = True
  upwards_xmas = True
  for i in range(1, search_length_xmas):
    if (x_col_i - i < 0) or (downwards_xmas and wordsearch[x_col_i - i][x_row_i] != XMAS[i]):
      downwards_xmas = False
    if (x_col_i + i >= len(wordsearch)) or (upwards_xmas and wordsearch[x_col_i + i][x_row_i] != XMAS[i]):
      upwards_xmas = False

    if not downwards_xmas and not upwards_xmas:
      return 0

  return sum([downwards_xmas, upwards_xmas])

def search_diagonal(wordsearch, x_col_i, x_row_i):
  assert wordsearch[x_col_i][x_row_i] == 'X'
  upleft_xmas = True
  upright_xmas = True
  downleft_xmas = True
  downright_xmas = True
  for i in range(1, search_length_xmas):
    if x_col_i - i < 0:
      upleft_xmas = False
      upright_xmas = False
    if x_row_i - i < 0:
      upleft_xmas = False
      downleft_xmas = False
    if x_col_i + i >= len(wordsearch):
      downleft_xmas = False
      downright_xmas = False
    if x_row_i + i >= len(wordsearch[x_col_i]):
      upright_xmas = False
      downright_xmas = False

    if upleft_xmas and wordsearch[x_col_i - i][x_row_i - i] != XMAS[i]:
      upleft_xmas = False
    if upright_xmas and wordsearch[x_col_i - i][x_row_i + i] != XMAS[i]:
      upright_xmas = False
    if downleft_xmas and wordsearch[x_col_i + i][x_row_i - i] != XMAS[i]:
      downleft_xmas = False
    if downright_xmas and wordsearch[x_col_i + i][x_row_i + i] != XMAS[i]:
      downright_xmas = False


    if sum([upleft_xmas, upright_xmas, downleft_xmas, downright_xmas]) == 0:
      return 0

  return sum([upleft_xmas, upright_xmas, downleft_xmas, downright_xmas])

def search_for_xmas(wordsearch):
  num_xmas = 0
  num_rows = len(wordsearch)
  num_cols = len(wordsearch[0])
  for row_i in range(num_rows):
    for col_i in range(num_cols):
      if wordsearch[col_i][row_i] == "X":
        num_xmas += search_horizontal(wordsearch, col_i, row_i)
        num_xmas += search_vertical(wordsearch, col_i, row_i)
        num_xmas += search_diagonal(wordsearch, col_i, row_i)

  return num_xmas

def search_for_x_mas(wordsearch):
  num_xmas = 0
  num_rows = len(wordsearch)
  num_cols = len(wordsearch[0])
  for row_i in range(1, num_rows - 1):
    for col_i in range(1, num_cols - 1):
      if wordsearch[col_i][row_i] == "A":

        # left diagonal
        if (((wordsearch[col_i - 1][row_i - 1] == "M" and wordsearch[col_i + 1][row_i + 1] == "S") or
           (wordsearch[col_i - 1][row_i - 1] == "S" and wordsearch[col_i + 1][row_i + 1] == "M")) and
        # right diagonal
           ((wordsearch[col_i - 1][row_i + 1] == "M" and wordsearch[col_i + 1][row_i - 1] == "S") or
           (wordsearch[col_i - 1][row_i + 1] == "S" and wordsearch[col_i + 1][row_i - 1] == "M"))):
          num_xmas += 1

  return num_xmas

def part_one(input):
  num_xmas = search_for_xmas(input)
  print("num xmas:", num_xmas)

def part_two(input):
  num_xmas = search_for_x_mas(input)
  print("num x-mas:", num_xmas)

if __name__ == '__main__':
  input = convert_to_array_matrix(read_input('input.txt'))
  part_one(input)
  part_two(input)

