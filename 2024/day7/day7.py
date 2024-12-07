from my_io import read_input
from enum import Enum
import re
import itertools

class Operator(Enum):
  ADDITION = 1
  MULTIPLICATION = 2

def generate_all_operator_combinations(num_operators: int):
  # n-choose-k with repetition to get all possible operator combinations
  operator_types = [Operator.MULTIPLICATION, Operator.ADDITION]
  return [p for p in itertools.product(operator_types, repeat=num_operators)]

def calculate_result_from_nums_and_operators(nums: [], operators: []):
  result = nums[0]

  for i in range(len(nums[1:])):
    if operators[i] == Operator.ADDITION:
      result += nums[i + 1]
    elif operators[i] == Operator.MULTIPLICATION:
      result *= nums[i + 1]
    else:
      assert "Invalid operator type:" + operators[i]

  return result


def eqn_is_valid(nums: []):
  result = nums[0]
  # for n numbers, there will be n-1 operators
  num_operators = len(nums[1:]) - 1
  operator_combos = generate_all_operator_combinations(num_operators)

  for combo in operator_combos:
    if calculate_result_from_nums_and_operators(nums[1:], combo) == result:
      return True
  return False

def part_one(eqns):
  sum = 0
  for eqn in eqns:
    if eqn_is_valid(eqn):
      sum += eqn[0]
  return sum

def parse_input(input):
  eqns = []
  for line in input:
    eqns.append([int(s) for s in re.findall(r'\d+', line)])
  return eqns

if __name__ == '__main__':
  eqns = parse_input(read_input('input.txt'))
  print("sum of valid equations:" + str(part_one(eqns)))
  # part_two(map)

