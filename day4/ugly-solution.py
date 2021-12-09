
def read_file():
  lines = open("input").read().splitlines()
  return lines

def split_input(input):
  random_machine = input[0].split(",")
  value_sets = []
  vertical_set = [set(), set(), set(), set(), set()]
  for i in range(2, len(input)):
    line = input[i].split()
    if line is None or line == [''] or line == []:
      value_sets.extend(vertical_set)
      vertical_set = [set(), set(), set(), set(), set()]
      continue
    value_sets.append(set(line))
    for x in range(0, 5):
      vertical_set[x].add(line[x])
  return (random_machine, value_sets)

def get_card_total(input, set_index, winning_set):
  card_number = (set_index // 10) + 1
  start_line = 6 * card_number - 4
  print(start_line)
  total = 0
  for i in range(start_line, start_line + 5):
    line = input[i]
    number_list = [int(x) if x not in winning_set else 0 for x in line.split()]
    total += sum(number_list)
  return total

#Part 1
def search_for_winner():
  input_file = read_file()
  (randomized_number, sets) = split_input(input_file)
  for i in range(5, len(randomized_number)):
    cur_selection = set(randomized_number[0:i])
    for idx in range(len(sets)):
      element = sets[idx]
      if element <= cur_selection:
        total = get_card_total(input_file, idx, cur_selection)
        return total * int(randomized_number[i-1])

#Part 2
def search_for_last():
  input_file = read_file()
  last_to_win = -1
  won_cards = set()
  (randomized_number, sets) = split_input(input_file)
  for i in range(5, len(randomized_number)):
    cur_selection = set(randomized_number[0:i])
    for idx in range(len(sets)):
      element = sets[idx]
      if element <= cur_selection:
        card_number = (idx // 10) + 1
        start_line = 6 * card_number - 4
        if start_line not in won_cards:
          last_to_win = idx
          last_selection_index = i
          won_cards.add(start_line)
  total = get_card_total(input_file, last_to_win, set(randomized_number[0:last_selection_index]))
  return total * int(randomized_number[last_selection_index-1])


print(search_for_last())
