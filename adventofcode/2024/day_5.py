input = open('input/day_5_input.txt', 'r')
rules = {}
updates = []
invalid = []
total_part_I = 0
total_part_II = 0

def reorder(vals):
    for i in range(len(vals) - 1):
        first, second = i, i + 1

        while vals[second] in rules and vals[first] in rules[vals[second]] and first >= 0:
            # switch the values
            temp = vals[second]
            vals[second] = vals[first]
            vals[first] = temp

            # update first and second
            first -= 1
            second -= 1

    return vals

def check_if_valid(vals):
    for i in range(len(vals) - 1):
        first, second = vals[i], vals[i + 1]

        # if the second is not allowed to come after the first
        if second in rules and first in rules[second]:
            return False

    return True

def get_middle(vals):
    middle_index = int(len(vals) / 2)
    return vals[middle_index]

# get the rules
for line in input:
    if line == '\n':
        break
    line = line.strip() # remove the newline
    x,y = line.split('|')
    x = int(x)
    y = int(y)

    if x not in rules:
        rules[x] = []
    rules[x].append(y)

# get the updates
for line in input:
    line = line.strip() # remove the newline
    vals = line.split(',')
    vals = [int(x) for x in vals]

    if check_if_valid(vals):
        total_part_I += get_middle(vals)
    else:
        invalid.append(vals)

print('Part I:', total_part_I)

# Part II
for vals in invalid:
    vals = reorder(vals)
    total_part_II += get_middle(vals)

print('Part II:', total_part_II)