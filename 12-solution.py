import re

pots = re.findall(r"[\.#]+", open("12-input.txt").read())
initial = pots[0]
rules = {pots[i]: pots[i+1] for i in range(1, len(pots) - 1, 2)}

def pot_number_sum(state, rules, generations):
  for _ in range(generations):
    state = "....%s...." % state
    state = "".join(rules[state[i:i+5]] for i in range(len(state) - 5))
  return sum(i - 2 * generations for i in range(len(state)) if state[i] == "#")

# Part 1
print(pot_number_sum(initial, rules, 20))

# Part 2
print(pot_number_sum(initial, rules, 5000))
