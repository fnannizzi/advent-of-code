from day7 import *
import unittest

class Test(unittest.TestCase):
  eqns = parse_input(read_input('test_input.txt'))

  def test_part_one(self):
    self.assertEqual(get_sum_of_valid_eqns(self.eqns, with_concat=False), 3749)

  def test_eqn_is_valid_with_concat(self):
    eqn = [7290, 6, 8, 6, 15]
    operators = [Operator.MULTIPLICATION, Operator.CONCATENATION, Operator.MULTIPLICATION]
    self.assertEqual(calculate_result_from_nums_and_operators(eqn[1:], operators), 7290)
    self.assertEqual(eqn_is_valid(eqn, with_concat=True), True)
  def test_part_two(self):
    self.assertEqual(get_sum_of_valid_eqns(self.eqns, with_concat=True), 11387)
