import string
import re

polymer = open("5-input.txt").read().strip()

def can_react(units):
  return len(units) == 2 and abs(ord(units[0]) - ord(units[1])) == 32

def react(polymer):
  for i in range(len(polymer) - 2, -1, -1): 
    if can_react(polymer[i:i+2]):
      polymer = polymer[:i] + polymer[i+2:]
  return polymer

# Part 1
print(len(react(polymer)))

# Part 2
lengths = []
for unit_type in string.ascii_lowercase:
  remaining = re.sub(unit_type, "", polymer, flags=re.IGNORECASE)
  length = len(react(remaining))
  lengths.append(length)
print(min(lengths))
