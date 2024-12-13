import unittest
from day4 import *

class Test(unittest.TestCase):
  input = convert_to_array_matrix(read_input('input.txt'))

  def test_search_horizontal(self):
    # backwards and forwards
    self.assertEqual(search_horizontal(self.input, 19, 85), 2)
    # backwards only
    self.assertEqual(search_horizontal(self.input, 7, 25), 1)
    # forwards only
    self.assertEqual(search_horizontal(self.input, 0, 37), 1)

  def test_search_vertical(self):
    # downwards and upwards
    self.assertEqual(search_vertical(self.input, 17, 50), 2)
    # downwards only
    self.assertEqual(search_vertical(self.input, 9, 51), 1)
    # upwards only
    self.assertEqual(search_vertical(self.input, 21, 65), 1)

  def test_search_diagonal(self):
    # downleft and downright
    self.assertEqual(search_diagonal(self.input, 18, 56), 2)
    # upright and downleft
    self.assertEqual(search_diagonal(self.input, 19, 15), 2)
    # upleft
    self.assertEqual(search_diagonal(self.input, 4, 18), 1)

