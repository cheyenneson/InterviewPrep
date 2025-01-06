import re
input = open('input/day_13_input.txt', 'r')
input_vals = []
solution = 0

# a is 3 tokens, b is 1 token

def solve_machine(input):
    A = input[0]
    B = input[1]
    [X, Y] = input[2]

    # base case
    if X - A[0] == 0 and Y - A[1] == 0:
        return 3
    if X - B[0] == 0 and Y - B[1] == 0:
        return 1

    return 0

for line in input:
    # get A
    line = line.strip()
    strs = line.split("+")
    A = [int(strs[1].split(',')[0]), int(strs[2])]

    # get B
    line = input.readline().strip()
    strs = line.split("+")
    B = [int(strs[1].split(',')[0]), int(strs[2])]

    # get prize
    line = input.readline().strip()
    x = int(re.search('X=(.*),', line).group(1))
    y = int(re.search('Y=(.*)$', line).group(1))
    prize = [x, y]

    # add to input_vals and skip the blank line
    input_vals.append([A, B, prize])
    input.readline()

for machine in input_vals:
    solution += solve_machine(machine)

print('Part I:', solution)