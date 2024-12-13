from day2 import *

class Test(unittest.TestCase):
  reports = read_reports()

  def test_part_1(self):
    self.assertEqual(part_one(self.reports), 463)

  def test_safe_increasing(self):
    self.assertTrue(report_is_safe([50, 52, 54, 56, 59, 61, 64]))

  def test_safe_decreasing(self):
    self.assertTrue(report_is_safe([84, 82, 79, 78, 75, 74, 71, 68]))

  def test_increasing_too_fast(self):
    self.assertFalse(report_is_safe([3, 10]))

  def test_decreasing_too_fast(self):
    self.assertFalse(report_is_safe([3, -1]))

  def test_repeated(self):
    self.assertFalse(report_is_safe([3, 3]))

  def test_drop_index(self):
    report = [0, 1, 2, 3]
    self.assertEqual(drop_index(report, 0), [1, 2, 3])
    self.assertEqual(drop_index(report, 1), [0, 2, 3])
    self.assertEqual(drop_index(report, 2), [0, 1, 3])
    self.assertEqual(drop_index(report, 3), [0, 1, 2])

  def test_get_subreports(self):
    report = [0, 1, 2, 3]
    self.assertEqual(get_all_subreports(report), [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]])

  def test_dampened_increasing_too_fast(self):
    report = [33, 37, 40, 43, 46, 49]
    self.assertEqual(get_problematic_index(report), 1)
    self.assertEqual(drop_bad_index(report, 1), [[37, 40, 43, 46, 49], [33, 40, 43, 46, 49]])
    self.assertTrue(passes_problem_dampener(report))

  def test_dampened_increasing_too_fast_end_index(self):
    report = [34, 37, 40, 43, 46, 50]
    self.assertEqual(get_problematic_index(report), 5)
    self.assertEqual(drop_bad_index(report, 5), [[34, 37, 40, 43, 50], [34, 37, 40, 43, 46]])
    self.assertTrue(passes_problem_dampener(report))

  def test_dampened_increasing_too_fast_two(self):
    self.assertFalse(passes_problem_dampener([33, 37, 41, 43, 46, 49]))

  def test_dampened_decreasing_too_fast(self):
    self.assertTrue(passes_problem_dampener([90, 92, 88, 85, 83, 80, 78]))

  def test_dampened_decreasing_too_fast_two(self):
    self.assertFalse(passes_problem_dampener([90, 92, 88, 84, 83, 80, 78]))

  def test_problematic_case_one(self):
    report = [92, 93, 92, 89, 86]
    self.assertTrue(passes_problem_dampener_brute_force(report))

  def test_problematic_case_two(self):
    report = [68, 66, 67, 69, 72, 73, 76]
    self.assertTrue(passes_problem_dampener_brute_force(report))

  def test_part_2(self):
    self.assertEqual(part_two(self.reports), 514)
