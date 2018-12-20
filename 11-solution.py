import copy

grid_serial_number = 9810

def power(x, y):
  rackId = x + 10
  power = rackId * y
  power += grid_serial_number
  power *= rackId
  power = int(str(power)[-3])
  return power - 5

def summed_area_table(grid):
  grid = copy.deepcopy(grid)
  for x in range(len(grid)):
    for y in range(len(grid)):
      if x != 0: grid[x][y] += grid[x-1][y]
      if y != 0: grid[x][y] += grid[x][y-1]
      if y != 0 and x != 0: grid[x][y] -= grid[x-1][y-1]
  return grid

grid = [[power(x, y) for y in range(301)] for x in range(301)]
summed_area = summed_area_table(grid)

def total_power(cell, size):
  x_min = cell[0] - 1
  x_max = cell[0] - 1 + size
  y_min = cell[1] - 1
  y_max = cell[1] - 1 + size
  a = summed_area[x_min][y_min]
  b = summed_area[x_max][y_min]
  c = summed_area[x_min][y_max]
  d = summed_area[x_max][y_max]
  return d + a - b - c

# Part 1
cells = [(x, y) for x in range(1, 299) for y in range(1, 299)]
x, y = max(cells, key=lambda cell: total_power(cell, 3))
print("%d,%d" % (x, y))

# Part 2
max_power = 0
max_x = None
max_y = None
max_size = None
for size in range(3, 30):
  cells = [(x, y) for x in range(1, 302 - size) for y in range(1, 302 - size)]
  x, y = max(cells, key=lambda cell: total_power(cell, size))
  power = total_power((x, y), size)
  if power > max_power:
    max_power = power
    max_x = x
    max_y = y
    max_size = size
print("%d,%d,%d" % (max_x, max_y, max_size))
