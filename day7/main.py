import statistics

def read_input():
  return [int(x) for x in open("input").read().split(",")]

def solve_part_1(input):
  med = statistics.median(input)
  fuel = 0
  for submarine in input:
    fuel += abs(submarine - med)
  return fuel

def solve_part_2(input):
  avg = sum(input) // len(input)
  fuel = 0
  for submarine in input:
    fuel += abs(submarine - avg) * (abs(submarine - avg) + 1) // 2
  return fuel

input = read_input()
print(solve_part_2(input))