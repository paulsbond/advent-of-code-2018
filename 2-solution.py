import string

box_ids = [line.strip() for line in open("2-input.txt")]
id_length = len(box_ids[0])

def letter_repeated(box_id, number_of_times):
  for letter in string.ascii_lowercase:
    if box_id.count(letter) == number_of_times:
      return True
  return False

def checksum(box_ids):
  count2 = len([x for x in box_ids if letter_repeated(x, 2)])
  count3 = len([x for x in box_ids if letter_repeated(x, 3)])
  return count2 * count3

def single_difference(id1, id2):
  difference_index = None
  for i in range(id_length):
    if id1[i] != id2[i]:
      if difference_index != None: return None
      difference_index = i
  return difference_index

def shared_letters_of_correct_box_ids(box_ids):
  for i in range(len(box_ids)):
    id1 = box_ids[i]
    for j in range(i + 1, len(box_ids)):
      id2 = box_ids[j]
      difference_index = single_difference(id1, id2)
      if difference_index != None:
        return id1[:difference_index] + id1[difference_index + 1:]

# Part 1
print(checksum(box_ids))

# Part 2
print(shared_letters_of_correct_box_ids(box_ids))
