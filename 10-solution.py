import re

class Point:
  def __init__(self, line):
    nums = re.findall(r"-?\d+", line)
    self.position = [int(nums[0]), int(nums[1])]
    self.velocity = [int(nums[2]), int(nums[3])]
  
  def position_after(self, seconds):
    x = self.position[0] + seconds * self.velocity[0]
    y = self.position[1] + seconds * self.velocity[1]
    return [x, y]

def print_grid(positions):
  min_x = min(position[0] for position in positions)
  max_x = max(position[0] for position in positions)
  min_y = min(position[1] for position in positions)
  max_y = max(position[1] for position in positions)
  grid = [["." for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]
  for position in positions:
    x = position[0] - min_x
    y = position[1] - min_y
    grid[y][x] = "X"
  for i in range(len(grid)):
    print("".join(grid[i]))

def get_area(positions):
  min_x = min(position[0] for position in positions)
  max_x = max(position[0] for position in positions)
  min_y = min(position[1] for position in positions)
  max_y = max(position[1] for position in positions)
  return (max_x - min_x) * (max_y - min_y)

points = [Point(line) for line in open("10-test.txt")]
positions = [point.position for point in points]
min_area = get_area(positions)
min_area_seconds = 0

for seconds in range(1, 5):
  positions = [point.position_after(seconds) for point in points]
  area = get_area(positions)
  if area < min_area:
    min_area = area
    min_area_seconds = seconds

positions = [point.position_after(min_area_seconds) for point in points]
print_grid(positions)
