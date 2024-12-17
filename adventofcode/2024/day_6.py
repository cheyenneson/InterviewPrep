input = open('input/day_6_input.txt', 'r')

length = 0
curr_pos = None
curr_dir = None
directions = ['^','<','>','v']
grid = []
count = 1

move = {
    '^': lambda arr : [arr[0] - 1, arr[1]],
    'v': lambda arr : [arr[0] + 1, arr[1]],
    '<': lambda arr : [arr[0], arr[1] - 1],
    '>': lambda arr : [arr[0], arr[1] + 1]
}

def print_grid(grid):
    for i in range(len(grid)):
        str = ""
        for j in range(len(grid[0])):
            str += grid[i][j] + " "
        print(str)

def do_next(curr_pos, dir, grid, count):
    while 1:
        new_pos = move[dir](curr_pos)

        if new_pos[0] < 0 or new_pos[0] >= len(grid) or new_pos[1] < 0 or new_pos[1] >= len(grid[0]):
            break
        
        if grid[new_pos[0]][new_pos[1]] == '#':
            return True, count

        if grid[new_pos[0]][new_pos[1]] != 'X':
            grid[new_pos[0]][new_pos[1]] = 'X'
            count += 1

        curr_pos[0], curr_pos[1] = new_pos

    return False, count


def turn_right(dir):
    if dir == '^':
        return '>'
    if dir == '>':
        return 'v'
    if dir == 'v':
        return '<'
    if dir == '<':
        return '^'

for line in input:
    line = line.strip()
    arr = list(line)
    grid.append(arr)

    for char in directions:
        if char in line:
            curr_pos = [length, line.index(char)]
            curr_dir = char
            grid[length][line.index(char)] = 'X'

    length += 1

keep_going, count = do_next(curr_pos, curr_dir, grid, count)
while keep_going:
    curr_dir = turn_right(curr_dir)
    keep_going, count = do_next(curr_pos, curr_dir, grid, count)

print("Part I:", count)
print_grid(grid)

