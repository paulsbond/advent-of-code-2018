changes = [int(line) for line in open("1-input.txt")]

# Part 1
print(sum(changes))

# Part 2
frequency = 0
frequencies_reached = {0}
i = 0
for _ in range(1000000):
  frequency += changes[i]
  if frequency in frequencies_reached: break
  frequencies_reached.add(frequency)
  i += 1
  if i == len(changes): i = 0
print(frequency)
