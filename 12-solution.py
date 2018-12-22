import re

pots = re.findall(r"[\.#]+", open("12-input.txt").read())
initial = pots[0]
rules = {pots[i]: pots[i+1] for i in range(1, len(pots) - 1, 2)}

def pot_number_sum(state, rules, generations):
  offset = 0
  for _ in range(generations):
    state = "....%s...." % state
    state = "".join(rules[state[i:i+5]] for i in range(len(state) - 5))
    offset -= state.find("#") - 2
    state = state.strip(".")
  return sum(i - offset for i in range(len(state)) if state[i] == "#")

# Part 1
print(pot_number_sum(initial, rules, 20))

# Part 2
sum_1000 = pot_number_sum(initial, rules, 1000)
sum_1001 = pot_number_sum(initial, rules, 1001)
diff = sum_1001 - sum_1000
answer = (50000000000 - 1000) * diff + sum_1000
print(answer)
