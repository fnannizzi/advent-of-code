from day9 import *
import unittest

class Test(unittest.TestCase):
  disk_map = parse_input('test_input.txt')

  def test_get_file_sizes(self):
    file_sizes = get_file_sizes(self.disk_map)
    self.assertEqual(len(file_sizes), 10)
    self.assertEqual(file_sizes[0], 2)
    self.assertEqual(file_sizes[5], 4)
    self.assertEqual(file_sizes[9], 2)

  def test_decompress_disk_map(self):
    self.assertEqual(decompress_and_get_checksum(self.disk_map), 1928)
