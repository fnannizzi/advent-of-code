def is_safe(report):
  increasing = True
  # print("first: ", report[0], " second: ", report[1], " diff: ", report[0] - report[1])
  if report[0] - report[1] > 0:
    # print("decreasing")
    increasing = False

  for n in range(1, len(report)):
    diff = report[n] - report[n - 1]
    # print("first: ", report[n-1], " second: ", report[n], " diff: ", diff)
    if increasing and (diff > 3 or diff <= 0):
      # print("not safe: ", report)
      return False
    elif not increasing and (diff < -3 or diff >= 0):
      return False
      # print("not safe: ", report)

  print("safe: ", report)
  return True

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
