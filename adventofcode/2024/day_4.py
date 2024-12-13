# lambda functions representing the 8 directions
top_left = lambda x, y : (x - 1, y - 1)
top = lambda x, y : (x - 1, y)
top_right = lambda x, y : (x - 1, y + 1)
left = lambda x, y : (x, y - 1)
right = lambda x, y : (x, y + 1)
bottom_left = lambda x, y : (x + 1, y - 1)
bottom = lambda x, y : (x + 1, y)
bottom_right = lambda x, y : (x + 1, y + 1)
directions = [top_left, top, top_right, left, right, bottom_left, bottom, bottom_right]
diagonals = [top_left, top_right, bottom_left, bottom_right]

def check_all_directions(grid, row, col):
    count = 0
    letters = ['M', 'A', 'S']

    for direction in directions:
        x, y = row, col
        for letter in letters:
            x, y = direction(x, y)
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == letter):
                break
            elif letter == 'S':
                count += 1

    return count

input = open('input/day_4_input.txt', 'r')
grid = []

for line in input:
    arr = []
    for letter in line:
        if letter != '\n':
            arr.append(letter)
    grid.append(arr)

visited = [[False] * len(grid[0])] * len(grid)

count = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'X':
            count += check_all_directions(grid, row, col)

print("Part I:", count)

# Part II:
def check_for_X(grid, row, col):
    [t_l, t_r, b_l, b_r] = [diagonal(row,col) for diagonal in diagonals]

    if t_l[0] < 0 or t_l[1] < 0 or b_r[0] >= len(grid) or b_r[1] >= len(grid[0]):
        return 0
    
    t_l = grid[t_l[0]][t_l[1]]
    t_r = grid[t_r[0]][t_r[1]]
    b_l = grid[b_l[0]][b_l[1]]
    b_r = grid[b_r[0]][b_r[1]]
    
    if (t_l == 'M' and b_r == 'S') or (t_l == 'S' and b_r == 'M'):
        if (t_r == 'M' and b_l == 'S') or (t_r == 'S' and b_l == 'M'):
            return 1
        
    return 0

count = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'A':
            count += check_for_X(grid, row, col)

print("Part II:", count)