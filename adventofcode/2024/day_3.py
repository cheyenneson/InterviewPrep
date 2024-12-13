import re

def caclulate(str):
    pattern_mul = "mul\\([0-9]+,[0-9]+\\)"
    matches = re.findall(pattern_mul, str)
    solution = 0
    
    for match in matches:
        a, b = match[4:-1].split(',')
        solution += int(a) * int(b)

    return solution

#initialize solution to 0
solution = 0

# retrieve input from input file
input = open('day_3_input.txt', 'r')
str = ""
for line in input:
    str += line

# constants
str_do = "do()"
str_dont = "don't()"

# remove the beginning if it starts with don't()
if str[0:7] == "don't()":
    index = str.find(str_do)
    str = str[index + 4:]

# split up the don't()s
matches_dont = str.split(str_dont)

# calulate the first one
solution += caclulate(matches_dont[0])
matches_dont = matches_dont[1:]

for match in matches_dont:
    #find a do(), then calculate everything after that, add to solution
    index = match.find(str_do)
    if index != -1:
        solution += caclulate(match[index:])

print(solution)
