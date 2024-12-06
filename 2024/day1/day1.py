from my_io import read_input

list_left  = []
list_right = []

def read_lists():
  lines = read_input('input.txt')
  for line in lines:
    parts = line.split("   ")
    list_left.append(int(parts[0]))
    list_right.append(int(parts[1]))

def part_one():
  sorted_list_left = sorted(list_left)
  sorted_list_right = sorted(list_right)

  difference = 0
  for i in range(len(sorted_list_left)):
    print("i: ", i, " left: ", sorted_list_left[i], " right: ", sorted_list_right[i])
    difference += abs(sorted_list_left[i] - sorted_list_right[i])

  print("difference: ", difference)

def part_two():
  distribution_right = {}

  for i in list_right:
    if i in distribution_right:
      distribution_right[i] += 1
    else:
      distribution_right[i] = 1

  similarity_score = 0
  for i in list_left:
    if i in distribution_right:
      print("i: ", i, " num appearances: ", distribution_right[i], " adding: ", distribution_right[i] * i)
      similarity_score += distribution_right[i] * i

  print("similarity score: ", similarity_score)

if __name__ == '__main__':
  read_lists()
  part_one()
  part_two()
