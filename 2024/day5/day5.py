from my_io import *
from enum import Enum
import math
class Rule:

  class Instruction(Enum):
    BEFORE = 1
    AFTER = 2

  def __init__(self):
    self.before = set({})
    self.after = set({})

  def add_to_rule(self, instruction: Instruction, page):
    if instruction == self.Instruction.BEFORE:
      self.before.add(page)
    else:
      self.after.add(page)

def validate_update(rules, update):
  seen = set({})

  for page in update:
    if len(rules[page].before & seen) > 0:
      return False

    seen.add(page)

  return True

def relocate_page(goes_before, goes_after, update, problematic_page):
  corrected_update = []
  holding_pen = []
  while(len(update) > 0):
    page = update[0]
    # all the pages that we need this page to go after have already been inserted
    if page == problematic_page:
      if len(goes_after) == 0:
        corrected_update.append(page)
        update.pop(0)
        break
      else:
        # there are still pages that need to go before this page, so put it at the front
        # of the holding pen for now
        holding_pen.insert(0, page)

    if page not in goes_before:
      if page in goes_after:
        goes_after.remove(page)
      corrected_update.append(page)
    else:
      # the problematic page needs to go before this page, so hold it until the problematic page is found
      holding_pen.append(page)
    update.pop(0)

  return corrected_update + holding_pen + update

def rectify_update(rules, update):
  seen = set({})

  for page in update:
    goes_before = rules[page].before & seen
    if len(goes_before) > 0:
      # this page is out of order
      goes_after = rules[page].after & seen
      update = relocate_page(goes_before, goes_after, update, page)
      break


    seen.add(page)
  if not validate_update(rules, update):
    return rectify_update(rules, update)
  return update

def add_up_middle(correct_updates):
  sum = 0
  for update in correct_updates:
    assert len(update) % 2 != 0
    sum += int(update[math.floor(len(update)/2)])
  return sum

def part_one(rules, updates):
  correct_updates = []
  for update in updates:
    if validate_update(rules, update):
      correct_updates.append(update)

  print("sum:", add_up_middle(correct_updates))

def part_two(rules, updates):
  incorrect_updates = []
  for update in updates:
    if not validate_update(rules, update):
      incorrect_updates.append(update)

  corrected_updates = []
  for update in incorrect_updates:
    # this algorithm assumes no duplicate pages
    assert len(set(update)) == len(update)
    corrected_updates.append(rectify_update(rules, update))

  print("sum:", add_up_middle(corrected_updates))

def parse_input(input):
  parsing_rules = True
  rules = {}
  updates = []
  for line in input:
    if line.isspace():
      parsing_rules = False
      continue

    line = line.strip("\n")
    if parsing_rules:
      pages = line.split("|")
      if pages[0] not in rules:
        rules[pages[0]] = Rule()
      rules[pages[0]].add_to_rule(instruction=Rule.Instruction.BEFORE, page=pages[1])
      if pages[1] not in rules:
        rules[pages[1]] = Rule()
      rules[pages[1]].add_to_rule(instruction=Rule.Instruction.AFTER, page=pages[0])
    else:
      updates.append(line.split(","))

  return rules, updates

if __name__ == '__main__':
  rules, updates = parse_input(read_input('input.txt'))
  part_one(rules, updates)
  part_two(rules, updates)
