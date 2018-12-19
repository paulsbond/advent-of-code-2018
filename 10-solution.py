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

def print_grid(points, seconds):
  min_x = min(p.position_after(seconds)[0] for p in points)
  max_x = max(p.position_after(seconds)[0] for p in points)
  min_y = min(p.position_after(seconds)[1] for p in points)
  max_y = max(p.position_after(seconds)[1] for p in points)
  grid = [["." for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]
  for point in points:
    x = point.position_after(seconds)[0] - min_x
    y = point.position_after(seconds)[1] - min_y
    grid[y][x] = "X"
  for i in range(len(grid)):
    print("".join(grid[i]))

points = [Point(line) for line in open("10-test.txt")]

for seconds in range(5):
  print("#" * 30)
  print_grid(points, seconds)
  print("#" * 30)
