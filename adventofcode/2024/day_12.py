#price = area X perimeter

file = open('input/day_12_input.txt', 'r')
input = []

# create a 2d array to represent the plots
for line in file:
    arr = [[x, False] for x in line if x != '\n']
    input.append(arr)

def find_cost(arr):
    total = 0

    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col][1] == False:
                area, perim = DFS(row, col, arr, arr[row][col][0], 0, 0)
                total += area * perim

    return total

def DFS(row, col, arr, val, area, perim):
    # already visited
    if arr[row][col][1]:
        return area, perim
    
    # mark visited
    arr[row][col][1] = True
    area += 1

    # initally a perimiter of 4
    p_add = 4

    if row + 1 < len(arr) and arr[row + 1][col][0] == val:
        p_add -= 1
        area, perim = DFS(row + 1, col, arr, val, area, perim)

    if row - 1 >= 0 and arr[row - 1][col][0] == val:
        p_add -= 1
        area, perim = DFS(row - 1, col, arr, val, area, perim)

    if col + 1 < len(arr[0]) and arr[row][col + 1][0] == val:
        p_add -= 1
        area, perim = DFS(row, col + 1, arr, val, area, perim)

    if col - 1 >= 0 and arr[row][col - 1][0] == val:
        p_add -= 1
        area, perim = DFS(row, col - 1, arr, val, area, perim)

    perim += p_add
    return area, perim


print(find_cost(input))