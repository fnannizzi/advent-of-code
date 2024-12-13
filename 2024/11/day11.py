from utils.my_io import read_input
import re

def blink_helper(stone) -> []:
  if stone == 0:
    return [1]
  elif len(str(stone)) % 2 == 0:
    stone_str = str(stone)
    num_digits_per_half = int(len(stone_str) / 2)
    return [int(stone_str[:num_digits_per_half]), int(stone_str[num_digits_per_half:])]
  else:
    return [stone * 2024]

def blink(stones: [], num_blinks: int) -> []:
  previous_results = {}
  for i in range(num_blinks):
    print("on iteration:", i)
    new_stones = []
    for stone in stones:
      if stone in previous_results:
        new_stones += previous_results[stone]
      else:
        new = blink_helper(stone)
        new_stones += new
        previous_results[stone] = new
    stones = new_stones
  return stones
def part_one(stones: []) -> []:
  return blink(stones, 25)

def part_two(stones: []) -> []:
  return blink(stones, 75)

def parse_input(filename):
  return [int(i) for i in re.findall(r'\d+',read_input(filename)[0][:-1])]

if __name__ == '__main__':
  stones = parse_input('input.txt')
  print("part one: ", str(len(part_one(stones))))
  print("part two: ", str(len(part_two(stones))))
