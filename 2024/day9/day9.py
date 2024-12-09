from utils.my_io import read_input

def get_file_sizes(map: []) -> {}:
  file_sizes = {}
  file_id = 0
  for file_size in map[::2]:
    file_sizes[file_id] = file_size
    file_id += 1
  return file_sizes

def get_empty_block_sizes(map: []) -> []:
  return map[1::2]

def decompress_disk_map(map):
  file_sizes = get_file_sizes(map)
  empty_block_sizes = get_empty_block_sizes(map)
  decompressed_length = sum(file_sizes.values())
  decompressed = [-1 for i in range(decompressed_length)]
  report_i_left = 0
  report_i_right = len(file_sizes.values()) - 1
  decompressed_i = 0

  while decompressed_i < decompressed_length:
    if file_sizes[report_i_left] != 0:
      decompressed[decompressed_i] = report_i_left
      file_sizes[report_i_left] -= 1
      decompressed_i += 1
    elif empty_block_sizes[report_i_left] != 0:
      decompressed[decompressed_i] = report_i_right
      empty_block_sizes[report_i_left] -= 1
      file_sizes[report_i_right] -= 1
      if file_sizes[report_i_right] == 0:
        report_i_right -= 1
      decompressed_i += 1
    else:
      report_i_left += 1
  return decompressed

def decompress_and_get_checksum(map):
  decompressed = decompress_disk_map(map)
  sum = 0
  for i in range(len(decompressed)):
    sum += i * decompressed[i]
  return sum

def parse_input(filename):
  return [int(i) for i in read_input(filename)[0][:-1]]

if __name__ == '__main__':
  disk_map = parse_input('input.txt')
  print("checksum: " + str(decompress_and_get_checksum(disk_map)))
