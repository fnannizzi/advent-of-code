def pair_is_safe(increasing, first, second):
  diff = second - first
  # print("increasing?:", increasing, " first:", first, "second:", second, "diff:", diff)
  if increasing and (diff > 3 or diff <= 0):
    return False
  elif not increasing and (diff < -3 or diff >= 0):
    return False

  return True

def report_is_safe(report):
  increasing = True
  if report[0] - report[1] > 0:
    increasing = False

  for n in range(1, len(report)):
    if not pair_is_safe(increasing, report[n - 1], report[n]):
      return n

  return -1

def is_safe(report):
  num_allowed_errors = 1
  found_errors = 0

  bad_index = report_is_safe(report)
  if bad_index != -1:
    found_errors += 1

    report_without_left = report[:bad_index - 1] + report[bad_index:]
    report_without_right = report[:bad_index] + report[bad_index + 1:]
    bad_index_left = report_is_safe(report_without_left)
    print("trying without level", bad_index - 1, ":", report_without_left)
    bad_index_right = report_is_safe(report_without_right)
    print("trying without level", bad_index, ":", report_without_right)

    if bad_index_left != -1 and bad_index_right != -1:
      found_errors += 1


  # if found_errors <= num_allowed_errors:
  #   print("report:", report)
  #   print("safe with", found_errors, "errors")
  #   print("-----------------")
  if found_errors > num_allowed_errors:
    print("report:", report)
    print("unsafe with", found_errors, "errors")
    print("-----------------")
  return found_errors <= num_allowed_errors

def convert_to_ints(report):
  nums = []
  for n in report.split(" "):
    nums.append(int(n))

  return nums

reports = []
num_safe_reports = 0

with open('input.txt', 'r', encoding="utf-8") as file:
  print("opened")
  reports = file.readlines()
  for report in reports:
    if is_safe(convert_to_ints(report)):
      num_safe_reports += 1

  print("num safe reports: ", num_safe_reports)
