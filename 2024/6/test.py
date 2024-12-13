from day6 import *
import unittest

class Test(unittest.TestCase):
  grid = convert_to_array_matrix(read_input('test_input.txt'))

  def test_turn_guard(self):
    self.assertEqual(GuardMoves.turn_guard(GuardMoves.Direction.UP), GuardMoves.Direction.RIGHT)
    self.assertEqual(GuardMoves.turn_guard(GuardMoves.Direction.RIGHT), GuardMoves.Direction.DOWN)
    self.assertEqual(GuardMoves.turn_guard(GuardMoves.Direction.DOWN), GuardMoves.Direction.LEFT)
    self.assertEqual(GuardMoves.turn_guard(GuardMoves.Direction.LEFT), GuardMoves.Direction.UP)

  def test_part_one(self):
    self.assertEqual(part_one(self.grid), 41)

  def test_part_two(self):
    obstacle_locations = part_two(self.grid)
    self.assertTrue(Position(6, 3).to_string() in obstacle_locations) # good
    self.assertTrue(Position(7, 6).to_string() in obstacle_locations) # good
    self.assertTrue(Position(7,7).to_string() in obstacle_locations) # good
    self.assertTrue(Position(8, 1).to_string() in obstacle_locations)
    self.assertTrue(Position(8, 3).to_string() in obstacle_locations)
    self.assertTrue(Position(9, 7).to_string() in obstacle_locations)

    self.assertEqual(len(obstacle_locations), 6)
