from itertools import cycle

class Player:
  def __init__(self):
    self.score = 0

# TODO: Improve speed
def winning_points(n_players, n_marbles):
  players = [Player() for _ in range(n_players)]
  queue = cycle(players)

  circle = [0]
  current = 0
  for marble in range(1, n_marbles + 1):
    player = next(queue)
    if marble % 23 != 0:
      index = current + 2
      while index > len(circle): index -= len(circle)
      while index < 0: index += len(circle)
      circle.insert(index, marble)
      current = index
    else:
      player.score += marble
      index = current - 7
      while index > len(circle): index -= len(circle)
      while index < 0: index += len(circle)
      player.score += circle.pop(index)
      while index > len(circle): index -= len(circle)
      while index < 0: index += len(circle)
      current = index

  return max(player.score for player in players)

# Part 1
print(winning_points(416, 71617))

# Part 2
# print(winning_points(416, 71617 * 100))
