import re
import string

class Coordinate():
  def __init__(self, line):
    nums = re.findall(r"\d+", line)
    self.x = int(nums[0])
    self.y = int(nums[1])
    self.area = 0
    self.finite = True

  def distance(self, x, y):
    return abs(self.x - x) + abs(self.y - y)

coordinates = [Coordinate(line) for line in open("6-input.txt")]

min_x = min(coord.x for coord in coordinates)
max_x = max(coord.x for coord in coordinates)
min_y = min(coord.y for coord in coordinates)
max_y = max(coord.y for coord in coordinates)

safe_area = 0
for x in range(min_x, max_x + 1):
  for y in range(min_y, max_y + 1):
    distances = [coord.distance(x, y) for coord in coordinates]
    if sum(distances) < 10000: safe_area += 1
    min_distance = min(distances)
    closest_coords = [c for c in coordinates if c.distance(x, y) == min_distance]
    if len(closest_coords) == 1:
      closest_coords[0].area += 1
      if x == min_x or x == max_x or y == min_y or y == max_y:
        closest_coords[0].finite = False

# Part 1
print(max(c.area for c in coordinates if c.finite == True))

# Part 2
print(safe_area)
