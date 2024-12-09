def read_input(filename):
  with open(filename, 'r', encoding="utf-8") as file:
    lines = file.readlines()
    return lines
