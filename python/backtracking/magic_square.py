import math

# check if a grid is a magic square
def is_magic(grid):
    n = int(math.sqrt(len(grid)))
    # should be 15 for n = 3
    magic_sum = int(((n ** 3) + n) / 2)
    diag_l_to_r = 0
    diag_r_to_l = 0

    for i in range(n):
        # check the rows
        if sum(grid[i * n : (i * n) + n]) != magic_sum: # 0 - 3, 3 - 6, 6 - 9
            return False
        
        # check the columns
        sum_col = 0
        for j in range(0, n * n, n): # 0, 3, 6
            sum_col += grid[i + j] # 0, 3, 6, then 1, 4, 7, then 2, 5, 8
        if sum_col != magic_sum:
            return False
        
        # check the diagonals
        diag_l_to_r += grid[(i * n) + i] # 0, 4, 8
        diag_r_to_l += grid[(i * n) + n - 1 - i] # 2, 4, 6

    if diag_l_to_r != magic_sum or diag_r_to_l != magic_sum:
        return False

    return True


# backtrack through all n x n arrangements
def generate_magic_squares(grid, curr_num, magic_squares):
    if curr_num > 9:
        if is_magic(grid):
            magic_squares.append(grid[:])
    
    for i in range(len(grid)):
        cell = grid[i]
        if cell == None:
            grid[i] = curr_num
            generate_magic_squares(grid, curr_num + 1, magic_squares)
            grid[i] = None
    
# 3 x 3
n = 3
answers = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],  [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]

# my solution
grid = [None] * n * n
curr_num = 1
magic_squares = []
generate_magic_squares(grid, 1, magic_squares)

# check my solution
answers = sorted(answers)
magic_squares = sorted(magic_squares)
print("Passed!" if magic_squares == answers else 'Failed!')
