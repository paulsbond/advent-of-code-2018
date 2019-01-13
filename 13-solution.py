from copy import deepcopy

class Cart:
  def __init__(self, x, y, direction):
    self.x = x
    self.y = y
    self.direction = direction
    self.turn = "left"

  def move(self, track_map):
    if   self.direction == ">": self.x += 1
    elif self.direction == "<": self.x -= 1
    elif self.direction == "v": self.y += 1
    elif self.direction == "^": self.y -= 1
    track = track_map[self.y][self.x]
    if track == "\\":
      if   self.direction == ">": self.direction = "v"
      elif self.direction == "<": self.direction = "^"
      elif self.direction == "v": self.direction = ">"
      elif self.direction == "^": self.direction = "<"
    if track == "/":
      if   self.direction == ">": self.direction = "^"
      elif self.direction == "<": self.direction = "v"
      elif self.direction == "v": self.direction = "<"
      elif self.direction == "^": self.direction = ">"
    if track == "+":
      if self.turn == "left":
        if   self.direction == ">": self.direction = "^"
        elif self.direction == "<": self.direction = "v"
        elif self.direction == "v": self.direction = ">"
        elif self.direction == "^": self.direction = "<"
        self.turn = "straight"
      elif self.turn == "straight":
        self.turn = "right"
      elif self.turn == "right":
        if   self.direction == ">": self.direction = "v"
        elif self.direction == "<": self.direction = "^"
        elif self.direction == "v": self.direction = "<"
        elif self.direction == "^": self.direction = ">"
        self.turn = "left"

track_map = [[c for c in line.rstrip()] for line in open("13-input.txt")]

carts = []
for y in range(len(track_map)):
  for x in range(len(track_map[y])):
    icon = track_map[y][x]
    if icon in "^v<>":
      carts.append(Cart(x, y, icon))
      if icon in "^v": track_map[y][x] = "|"
      if icon in "<>": track_map[y][x] = "-"

# Part 1
while len(carts) > 1:
  carts.sort(key=lambda c: (c.y, c.x), reverse=True)
  i = len(carts) - 1
  while i >= 0:
    cart = carts[i]
    cart.move(track_map)
    for j in range(len(carts)):
      if i == j: continue
      other = carts[j]
      if other.x == cart.x and other.y == cart.y:
        print("Crash at %d,%d" % (cart.x, cart.y))
        carts.remove(cart)
        carts.remove(other)
        if j < i: i-= 1
        break
    i -= 1

# Part 2
print("Location of the last cart: %d,%d" % (carts[0].x, carts[0].y))
