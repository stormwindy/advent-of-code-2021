def read_input():
  line = open("input").read()
  return line.split(",")

def solve(input, days):
  bucket = [0] * 9
  for initial_fish in input:
    bucket[int(initial_fish)] += 1
  
  for i in range(days):
    new_bucket = [0] * 9
    for idx in range(8):
      new_bucket[idx] = bucket[idx+1]
    
    new_bucket[8] = bucket[0]
    new_bucket[6] += bucket[0]
    bucket = new_bucket
  return sum(bucket)

input = read_input()
print(solve(input, 80))
print(solve(input, 256))