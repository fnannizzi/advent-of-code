import re
from utils.my_io import read_input

def get_mul_operations(input):
  return re.findall("mul\(\d+,\d+\)", input)

def perform_multiply(operation):
  operands = re.findall("\d+", operation)
  return int(operands[0])*int(operands[1])

def part_one(input):
  matches = get_mul_operations(input)

  sum = 0
  for match in matches:
    sum += perform_multiply(match)

  print("sum:", sum)

def drop_conditional_segments(input):
  return re.sub("(?<=don't\(\)).*?(?=do\(\))", "", input)

def part_two(input):
  input = drop_conditional_segments(input)
  part_one(input)

if __name__ == '__main__':
  input = re.sub('\n', '', ''.join(read_input('input.txt')))
  part_one(input)
  part_two(input)
