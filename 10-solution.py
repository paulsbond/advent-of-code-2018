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

def area(points, seconds):
  positions = [point.position_after(seconds) for point in points]
  min_x = min(position[0] for position in positions)
  max_x = max(position[0] for position in positions)
  min_y = min(position[1] for position in positions)
  max_y = max(position[1] for position in positions)
  return (max_x - min_x) * (max_y - min_y)

def seconds_between_points(point1, point2):
  x2 = (point1.position[0] - point2.position[0]) ** 2
  y2 = (point1.position[1] - point2.position[1]) ** 2
  distance = (x2 + y2) ** 0.5
  speed1 = (point1.velocity[0] ** 2 + point1.velocity[1] ** 2) ** 0.5
  speed2 = (point2.velocity[0] ** 2 + point2.velocity[1] ** 2) ** 0.5
  return distance / (speed1 + speed2)

def estimate_seconds(points):
  left = min(points, key=lambda point: point.position[0])
  right = max(points, key=lambda point: point.position[0])
  seconds1 = seconds_between_points(left, right)
  top = min(points, key=lambda point: point.position[1])
  bottom = max(points, key=lambda point: point.position[1])
  seconds2 = seconds_between_points(top, bottom)
  return int((seconds1 + seconds2) / 2)

points = [Point(line) for line in open("10-input.txt")]
estimate = estimate_seconds(points)
test_range = range(estimate - 20, estimate + 20)
seconds = min(test_range, key=lambda s: area(points, s))
positions = [point.position_after(seconds) for point in points]
print_grid(positions)
