from day5 import *
import unittest

class Test(unittest.TestCase):
  rules, _ = parse_input(read_input('test_input.txt'))

  def test_good_update(self):
    update = ['75', '47', '61', '53', '29']
    self.assertTrue(validate_update(self.rules, update))

  def test_bad_update(self):
    update = ['75', '97', '47', '61', '53']
    self.assertFalse(validate_update(self.rules, update))

  def test_rectify_bad_update(self):
    update = ['75', '97', '47', '61', '53']
    self.assertEqual(rectify_update(self.rules, update), ['97', '75', '47', '61', '53'])
    update = ['61', '13', '29']
    self.assertEqual(rectify_update(self.rules, update), ['61', '29', '13'])
    update = ['97', '13', '75', '29', '47']
    self.assertEqual(rectify_update(self.rules, update), ['97', '75', '47', '29', '13'])
