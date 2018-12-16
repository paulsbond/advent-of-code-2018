import re
import string

instructions = [line for line in open("7-input.txt")]

def parse(instructions):
  requirements = {}
  for instruction in instructions:
    steps = re.findall("step [A-Z]", instruction, re.IGNORECASE)
    step1 = steps[0][-1]
    step2 = steps[1][-1]
    if step1 not in requirements: requirements[step1] = set()
    if step2 not in requirements: requirements[step2] = set()
    requirements[step2].add(step1)
  return requirements

def construct(instructions, workers, times):
  requirements = parse(instructions)
  order = ""
  finish_times = {}
  second = 0
  while len(requirements) > 0:
    available = [step for step in requirements if len(requirements[step]) == 0]
    for step in sorted(available):
      if step in finish_times: continue
      if len(finish_times) < workers:
        finish_times[step] = second + times[step]
    second += 1
    finishing = [step for step in finish_times if finish_times[step] == second]
    for step in finishing:
      order += step
      finish_times.pop(step)
      requirements.pop(step)
      for other_step in requirements: requirements[other_step].discard(step)
  return order, second

# Part 1
times = {string.ascii_uppercase[i]: 1 for i in range(26)}
order, seconds = construct(instructions, 1, times)
print(order)

# Part 2
times = {string.ascii_uppercase[i]: 61 + i for i in range(26)}
order, seconds = construct(instructions, 5, times)
print(seconds)
