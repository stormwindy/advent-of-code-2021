def read_file():
  lines = open("input").read().splitlines()
  return lines

def create_board():
  return [[0] * 999 for i in range(999)]
  
def process_input_part_2(lines):
  board = create_board()
  total_doubles = 0
  for line in lines:
    (start_pos, end_pos) = line.split(" -> ")
    (start_x, start_y) = start_pos.split(",")
    (end_x, end_y) = end_pos.split(",")
    current_x = min(int(start_x), int(end_x))
    target_x = max(int(start_x), int(end_x))
    companion_x, companion_x_target = (int(start_y), int(end_y)) if start_x == current_x else (int(end_y), int(start_y))

    current_y = min(int(start_y), int(end_y))
    target_y = max(int(start_y), int(end_y))
    companion_y, companion_y_target = (int(start_x), int(end_x)) if start_y == current_y else (int(end_x), int(start_x))
    if current_x != target_x and current_y != target_y and abs(current_x - target_x) != abs(current_y - target_y):
      continue
    if target_x != current_x:
      while current_x <= target_x:
        board[current_x][companion_x] += 1
        if board[current_x][companion_x] == 2:
          total_doubles += 1
        if companion_x < companion_x_target:
          companion_x += 1
        elif companion_x > companion_x_target:
          companion_x -= 1
        current_x += 1
    else:
      while current_y <= target_y:
        board[companion_y][current_y] += 1
        if board[current_x][current_y] == 2:
          total_doubles += 1
        if companion_y < companion_y_target:
          print("should never be here")
          companion_y += 1
        elif companion_y > companion_y_target:
          print("should never be here 2")
          companion_y -= 1
        current_y += 1
  return total_doubles

def process_input_part_1(lines):
  board = create_board()
  total_doubles = 0
  for line in lines:
    (start_pos, end_pos) = line.split(" -> ")
    (start_x, start_y) = start_pos.split(",")
    (end_x, end_y) = end_pos.split(",")
    current_x = min(int(start_x), int(end_x))
    target_x = max(int(start_x), int(end_x))

    current_y = min(int(start_y), int(end_y))
    target_y = max(int(start_y), int(end_y))
    if current_x != target_x and current_y != target_y:
      continue
    if target_x != current_x:
      while current_x <= target_x:
        board[current_x][current_y] += 1
        if board[current_x][current_y] == 2:
          total_doubles += 1
        current_x += 1
    else:
      while current_y <= target_y:
        board[current_x][current_y] += 1
        if board[current_x][current_y] == 2:
          total_doubles += 1
        current_y += 1
  return total_doubles

input = read_file()
print(process_input_part_2(input))
      
    