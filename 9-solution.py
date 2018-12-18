from itertools import cycle
from collections import deque

class Player:
  def __init__(self):
    self.score = 0

def winning_points(n_players, max_points):
  players = [Player() for _ in range(n_players)]
  player_cycle = cycle(players)

  circle = deque([0])
  for marble in range(1, max_points + 1):
    player = next(player_cycle)
    if marble % 23 == 0:
      circle.rotate(7)
      player.score += marble + circle.pop()
      circle.rotate(-1)
    else:
      circle.rotate(-1)
      circle.append(marble)

  return max(player.score for player in players)

# Part 1
print(winning_points(416, 71617))

# Part 2
print(winning_points(416, 71617 * 100))
