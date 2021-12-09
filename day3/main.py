def read_file():
  lines = open("input").read().splitlines()
  return lines

def part2(input):
  oxy = set()
  carbon = set()
  one_count = zero_count = 0
  for line in input:
    if line[0] == '1':
      one_count += 1
      oxy.add(line)
    else:
      zero_count += 1
      carbon.add(line)
  
  if zero_count > one_count:
    tmp = oxy
    oxy = carbon
    carbon = tmp
  
  oxy_removal_set = set()
  oxy_one_count = oxy_zero_count = 0
  carbon_removal_set = set()
  carbon_one_count = carbon_zero_count = 0
  
  oxy_idx = 1

  while(len(oxy) != 1):
    oxy_zero = oxy_one = 0
    oxy_tmp = set()
    for line in oxy:
      char = line[oxy_idx]
      if char == '1':
        oxy_one += 1
      else:
        oxy_zero += 1
        oxy_tmp.add(line)
    if oxy_one < oxy_zero:
      oxy = oxy_tmp
    else:
      oxy = oxy - oxy_tmp
    oxy_idx += 1
  print(oxy)

  car_idx = 1

  while(len(carbon) != 1):
    car_zero = car_one = 0
    car_tmp = set()
    for line in carbon:
      char = line[car_idx]
      if char == '1':
        car_one += 1
      else:
        car_zero += 1
        car_tmp.add(line)
    if car_one >= car_zero:
      carbon = car_tmp
    else:
      carbon = carbon - car_tmp
    car_idx += 1
  print(carbon)
  return int(list(oxy)[0], 2) * int(list(carbon)[0], 2)
print(part2(read_file()))

  
