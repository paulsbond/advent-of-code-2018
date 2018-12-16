import re

log = [line.strip() for line in open("4-input.txt")]
log.sort()

class Guard:
  def __init__(self, guard_id):
    self.id = guard_id
    self.shifts = []
    self.time_alseep = 0
  
  def add_shift(self, shift):
    self.shifts.append(shift)
    self.time_alseep += shift.count("#")

  def times_asleep(self, time):
    return len([1 for shift in self.shifts if shift[time] == "#"])

  def sleepiest_time(self):
    times = [(self.times_asleep(time), time) for time in range(60)]
    return max(times)

guards = {}
for entry in log:
  if "Guard" in entry:
    if "shift" in locals():
      if guard_id not in guards: guards[guard_id] = Guard(guard_id)
      guards[guard_id].add_shift(shift)
    guard_id = int(re.findall(r"\d+", entry)[-1])
    shift = "." * 60
  elif "falls asleep" in entry:
    time1 = int(re.findall(r"\d+", entry)[-1])
  else:
    time2 = int(re.findall(r"\d+", entry)[-1])
    shift = shift[:time1] + "#" * (time2 - time1) + shift[time2:]
if guard_id not in guards: guards[guard_id] = Guard(guard_id)
guards[guard_id].add_shift(shift)

# Part 1
guard = max(guards.itervalues(), key=lambda guard: guard.time_alseep)
print(guard.id * guard.sleepiest_time()[1])

# Part 2
guard = max(guards.itervalues(), key=lambda guard: guard.sleepiest_time())
print(guard.id * guard.sleepiest_time()[1])
