from collections import deque

# 0 to 6
# x is distance from left and y is distance from right
# need to reach 6,6 (or 70, 70)
# simulate the first 1024, or 12
import sys

input = open('input/day_18_input.txt', 'r')
dimension = 7
max = 6
count = 0
grid = [['.'] * dimension for _ in range(dimension)]

directions = [
    # up
    lambda row, col: (row - 1, col),
    # down
    lambda row, col: (row + 1, col),
    # left
    lambda row, col: (row, col - 1),
    # right
    lambda row, col: (row, col + 1)
]

def print_grid(grid):
    for x in range(len(grid)):
        print(''.join(grid[x]))

for line in input:
    if count >= max:
        break
    x, y = map(int, line.strip().split(','))
    grid[y][x] = '#'
    count += 1

# my initial, really slow solution
def backtrack(row, col, grid, steps):
    # base case: reached bottom right corner
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return steps
    
    positions = []
    for direction in directions:
        pos = direction(row, col)
        # off the edge
        if pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0]):
        # if not (0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])):
            continue
        # already visited or blocked
        if grid[pos[0]][pos[1]] == 'X' or grid[pos[0]][pos[1]] == '#':
            continue
        positions.append(pos)

    # dead end
    if len(positions) == 0:
        return sys.maxsize

    # for every adjacent node that isn't corrupted or already visited
    #   find the min distance from there to end
    solutions = []
    for pos in positions:
        grid[pos[0]][pos[1]] = 'X'
        solutions.append(backtrack(pos[0], pos[1], grid, steps + 1))
        grid[pos[0]][pos[1]] = '.' # backtrack: unmark the visited spot

    return min(solutions)

# grid[0][0] = 'X'
# print(backtrack(0, 0, grid, 0))


def bfs(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0, 1)]) # row, col, steps
    visited = set()
    visited.add((0,0))

    while queue:
        row, col, steps = queue.popleft()

        # if we've reached the target
        if row == rows - 1 and col == cols - 1:
            return steps
        
        for direction in directions:
            nr, nc = direction(row, col)

            # check bounds and blocks and visited
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != '#':
                queue.append((nr, nc, steps + 1))
                visited.add((nr, nc))

    return -1

result = bfs(grid)
print('Part I:', result)


