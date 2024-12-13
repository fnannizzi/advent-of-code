from utils.my_io import read_input
from utils.grid_utils import *
from enum import Enum

class GuardMoves:
  class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

  GUARD_MOVES = {
    Direction.UP: [-1, 0],
    Direction.RIGHT: [0, 1],
    Direction.DOWN: [1, 0],
    Direction.LEFT: [0, -1]
  }

  @staticmethod
  def guard_move(direction: Direction, position: Position):
    move = GuardMoves.GUARD_MOVES[direction]
    return Position(position.row_i + move[0], position.col_i + move[1])

  @staticmethod
  def turn_guard(direction: Direction):
    return GuardMoves.Direction((direction.value % 4) + 1)

class GuardPathSolver:

  GUARD = '^'
  OBSTACLE = '#'
  EMPTY = '.'

  def __init__(self, map):
    self.map = map
    self.map_rows = len(map)
    self.map_cols = len(map[0])

  def locate_guard(self):
    for row_i, col_i in traverse_grid(num_rows=self.map_rows, num_cols=self.map_cols):
      if self.map[row_i][col_i] == self.GUARD:
        return Position(row_i=row_i, col_i=col_i)
    assert "There's no guard here!"

  def location_within_map(self, position):
    return 0 <= position.row_i < self.map_rows and 0 <= position.col_i < self.map_cols

  def advance_guard(self, direction: GuardMoves.Direction, position: Position):
    next_position = GuardMoves.guard_move(direction=direction, position=position)
    if self.location_within_map(next_position):
      # there's an obstacle in front of the guard, so turn without advancing
      if self.map[next_position.row_i][next_position.col_i] == self.OBSTACLE:
        direction = GuardMoves.turn_guard(direction)
        return direction, position

    return direction, next_position

  class GuardPosition(Position):
    def __init__(self, direction: GuardMoves.Direction, position: Position):
      super().__init__(position.row_i, position.col_i)
      self.direction = direction

    def to_string(self):
      return super().to_string() + " " + self.direction.name

  class GuardIsStuckInALoop(Exception):
    pass

  def solve(self):
    guard_position = self.locate_guard()
    direction = GuardMoves.Direction.UP
    locations = []
    locations_with_directions = set()

    while (self.location_within_map(guard_position)):
      # to be able to look up previous location and direction, create a hashable object
      guard_position_hashable = self.GuardPosition(direction, guard_position).to_string()
      if guard_position_hashable in locations_with_directions:
        raise self.GuardIsStuckInALoop("the guard is in a loop!")
      locations.append(guard_position.to_string())
      locations_with_directions.add(guard_position_hashable)
      direction, guard_position = self.advance_guard(direction=direction, position=guard_position)

    return locations

def part_one(map):
  unique_locations = set(GuardPathSolver(map).solve())

  print("unique locations:", len(unique_locations))
  return len(unique_locations)

def add_obstacle_to_map(map, obstacle_row_i, obstacle_col_i):
  map[obstacle_row_i][obstacle_col_i] = GuardPathSolver.OBSTACLE
  return map

def remove_obstacle_from_map(map, obstacle_row_i, obstacle_col_i):
  map[obstacle_row_i][obstacle_col_i] = GuardPathSolver.EMPTY
  return map

def part_two(map):
  # get the path of the guard with no obstacles
  locations = GuardPathSolver(map).solve()
  obstacle_locations = set()

  # on every point in the path that isn't the starting location, try adding an obstacle
  # and check if the guard gets stuck
  # it would be more efficient to start the solver over from the position immediately before
  # adding the obstacle, but to do so you need to retain the previous position (not hard)
  # and the direction the guard was facing (more refactoring than I have time for today)
  for location in locations[1:]:
    # we can't add an obstacle where the guard starts
    if location == locations[0]:
      continue
    position = Position.from_string(location)
    map_with_obstacle = add_obstacle_to_map(map, position.row_i, position.col_i)
    try:
      GuardPathSolver(map_with_obstacle).solve()
    except GuardPathSolver.GuardIsStuckInALoop:
      # this obstacle caused the guard to get stuck, so save the location
      obstacle_locations.add(location)
    map = remove_obstacle_from_map(map, position.row_i, position.col_i)
  print("obstacle locations:", len(obstacle_locations))
  return obstacle_locations

if __name__ == '__main__':
  map = convert_to_array_matrix(read_input('input.txt'))
  part_one(map)
  part_two(map)
