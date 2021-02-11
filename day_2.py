""" Day 2 part 1 """
from pprint import pprint

def process_inputs(inputs):
    lines = []
    for line in inputs:
        components = line.strip().split()
        minim, maxim = components[0].split('-')
        minim, maxim = int(minim), int(maxim)
        char = components[1][0]
        lines.append({
            'minimum': minim,
            'maximum': maxim,
            'character': char,
            'password': components[-1]
        })
    return lines

# with open('input.txt') as inputs:
#      lines = process_inputs(inputs)

# pprint(lines)

def count(character, password):
  counts = 0
  for i in password:
    if i == character:
      counts += 1
  return counts    


def is_valid(lines):
  """check whether the password is valid.
  line:dict
  line contains minimum maximum character password
  return:True or False
  """
  c = lines["maximum"]
  b = lines["minimum"]
  d = count(line["character"],line["password"])
  print(d)
  if d >= b and d <= c:
    return True
  else:
      return False
  print(count(True))    

with open('tests.txt') as inputs:
       tests = process_inputs(inputs)

pprint(tests)
c = is_valid(lines)
print(c)


# tests = [{'character': 'a', 'maximum': 3, 'minimum': 1, 'password': 'abcde'},
#  {'character': 'b', 'maximum': 3, 'minimum': 1, 'password': 'cdefg'},
#  {'character': 'c', 'maximum': 9, 'minimum': 2, 'password': 'ccccccccc'}]

# # pprint(tests)
# assert is_valid(tests[0]) == True, f'Case 1: {tests[0]} Expected Valid'
# assert is_valid(tests[1]) == False, f'Case 1: {tests[0]} Expected Invalid'
# assert is_valid(tests[2]) == True, f'Case 1: {tests[0]} Expected Valid'

