class Node:
  def __init__(self, nums):
    self.n_children = nums.pop(0)
    self.n_metadata = nums.pop(0)
    self.children = [Node(nums) for _ in range(self.n_children)]
    self.metadata = [nums.pop(0) for _ in range(self.n_metadata)]

  def sum_metadata(self):
    return sum(self.metadata) + sum([c.sum_metadata() for c in self.children])

  def value(self):
    if self.n_children == 0: return sum(self.metadata)
    value = 0
    for i in self.metadata:
      if i == 0 or i > self.n_children: continue
      value += self.children[i-1].value()
    return value

nums = [int(n) for n in open("8-input.txt").read().split()]
root = Node(nums)

# Part 1
print(root.sum_metadata())

# Part 2
print(root.value())
