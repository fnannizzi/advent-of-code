from my_io import read_input

def pair_is_safe(increasing, first, second):
  diff = second - first
  # print("increasing?:", increasing, " first:", first, "second:", second, "diff:", diff)
  if increasing and (diff > 3 or diff <= 0):
    return False
  elif not increasing and (diff < -3 or diff >= 0):
    return False

  return True

def get_problematic_index(report):
  increasing = True
  if report[0] - report[1] > 0:
    increasing = False

  for n in range(1, len(report)):
    if not pair_is_safe(increasing, report[n - 1], report[n]):
      return n

  return -1

def report_is_safe(report):
  return get_problematic_index(report) == -1


def part_one(reports):
  num_safe_reports = 0
  for report in reports:
    if report_is_safe(report):
      num_safe_reports += 1

  print("num safe reports: ", num_safe_reports)
  return num_safe_reports

def drop_index(report, index):
  return report[:index] + report[index + 1:]

def get_all_subreports(report):
  subreports = []
  for i in range(0, len(report)):
    subreports.append(drop_index(report, i))
  return subreports

def drop_bad_index(report, bad_index):
  report_without_left = drop_index(report, bad_index - 1)
  report_without_right = drop_index(report, bad_index)
  return [report_without_left, report_without_right]

def passes_problem_dampener(report):
  num_allowed_errors = 1
  found_errors = 0

  bad_index = get_problematic_index(report)
  if bad_index != -1:
    found_errors += 1

    dropped = drop_bad_index(report, bad_index)
    report_without_left = dropped[0]
    report_without_right = dropped[1]
    bad_index_left = get_problematic_index(report_without_left)
    print("trying without level", bad_index - 1, ":", report_without_left)
    bad_index_right = get_problematic_index(report_without_right)
    print("trying without level", bad_index, ":", report_without_right)

    if bad_index_left != -1 and bad_index_right != -1:
      found_errors += 1

  if found_errors <= num_allowed_errors:
    print("report:", report)
    print("safe with", found_errors, "errors")
    print("-----------------")
  if found_errors > num_allowed_errors:
    print("report:", report)
    print("unsafe with", found_errors, "errors")
    print("-----------------")

  return found_errors <= num_allowed_errors

def passes_problem_dampener_brute_force(report):
  found_errors = 0

  if report_is_safe(report):
    print("report:", report)
    print("safe with", found_errors, "errors")
    print("-----------------")
    return True

  subreports = get_all_subreports(report)
  for subreport in subreports:
    if report_is_safe(subreport):
      return True

  return False

  if found_errors <= num_allowed_errors:
    print("report:", report)
    print("safe with", found_errors, "errors")
    print("-----------------")
  if found_errors > num_allowed_errors:
    print("report:", report)
    print("unsafe with", found_errors, "errors")
    print("-----------------")

  return found_errors <= num_allowed_errors


def part_two(reports):
  num_safe_reports = 0
  for report in reports:
    if passes_problem_dampener_brute_force(report):
      num_safe_reports += 1
      if not passes_problem_dampener(report):
        print("problematic case:", report)

  print("num safe reports: ", num_safe_reports)
  return num_safe_reports

def convert_to_ints(report):
  nums = []
  for n in report.split(" "):
    nums.append(int(n))
  return nums


def read_reports():
  reports = []
  lines = read_input('input.txt')
  for line in lines:
    reports.append(convert_to_ints(line))
  return reports


if __name__ == '__main__':
  reports = read_reports()
  part_one(reports)
  part_two(reports)
