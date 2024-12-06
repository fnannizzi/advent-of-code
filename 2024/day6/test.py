from day6 import *
import unittest

class Test(unittest.TestCase):
  grid = convert_to_array_matrix(read_input(read_input('test_input.txt')))

  def test_good_update(self):
