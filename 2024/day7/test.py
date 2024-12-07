from day7 import *
import unittest

class Test(unittest.TestCase):
  eqns = parse_input(read_input('test_input.txt'))

  def test_part_one(self):
    self.assertEqual(part_one(self.eqns), 3749)
