import re

class Claim():
  def __init__(self, line):
    nums = [int(n) for n in re.findall(r"\d+", line)]
    self.id = nums[0]
    self.squares = []
    for i in range(nums[2], nums[2] + nums[4]):
      for j in range(nums[1], nums[1] + nums[3]):
        self.squares.append((i, j))

size = 1000
fabric = [[[] for i in range(size)] for j in range(size)]

claims = [Claim(line) for line in open("3-input.txt")]
for claim in claims:
  for i, j in claim.squares:
    fabric[i][j].append(claim.id)

# Part 1
multiple_claims = 0
for i in range(size):
  for j in range(size):
    if len(fabric[i][j]) > 1:
      multiple_claims += 1
print(multiple_claims)

# Part 2
for claim in claims:
  if not any(len(fabric[i][j]) > 1 for i, j in claim.squares):
    print(claim.id)
