input = open('input/day_7_input.txt', 'r')
hash_map = {}
solution_1, solution_2 = 0, 0

def concat(x, y):
    return int(str(x) + str(y))

def valid_1(val, arr, curr_sol, pos):
    # if we're at the end, don't call valid again
    if pos == len(arr) - 1:
        return val == curr_sol

    # do addition, then call valid for the rest (if the curr solution isn't bigger than val)
    if valid_1(val, arr, curr_sol + arr[pos + 1], pos + 1):
        return True

    # do multiplication, then ''
    if valid_1(val, arr, curr_sol * arr[pos + 1], pos + 1):
        return True

def valid_2(val, arr, curr_sol, pos):
    # if we're at the end, don't call valid again
    if pos == len(arr) - 1:
        return val == curr_sol

    # do addition, then call valid for the rest (if the curr solution isn't bigger than val)
    if valid_2(val, arr, curr_sol + arr[pos + 1], pos + 1):
        return True

    # do multiplication, then ''
    if valid_2(val, arr, curr_sol * arr[pos + 1], pos + 1):
        return True
    
    if valid_2(val, arr, concat(curr_sol, arr[pos + 1]), pos + 1):
        return True

for line in input:
    nums = line.split(':')
    nums[1] = nums[1].strip()
    arr = nums[1].split(' ')
    arr = [int(x) for x in arr]
    hash_map[int(nums[0])] = arr

for val in hash_map:
    if valid_1(val, hash_map[val], hash_map[val][0], 0):
        solution_1 += val
    if valid_2(val, hash_map[val], hash_map[val][0], 0):
        solution_2 += val

print("Part I:", solution_1)
print("Part II:", solution_2)