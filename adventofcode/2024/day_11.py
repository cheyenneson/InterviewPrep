import math
import sys

file = open('day_11_input.txt', 'r')
input = file.readline().split(' ')
input_arr = [int(x) for x in input]

convert_cache = {}
get_num_cache = {}

def convert(val): # 12
    if val in convert_cache:
        return convert_cache[val]

    if val == 0:
        return [1]
    
    digits = len(str(val))

    if digits % 2 == 0:
        temp = 10 ** int(digits / 2) # 10 
        right = val % temp # 2
        left = int(val / temp) # 1
        convert_cache[val] = [left, right]
        return [left, right]

    convert_cache[val] = [val * 2024]
    return [val * 2024]

def get_num(val, blinks):
    if (val, blinks) in get_num_cache:
        return get_num_cache[(val, blinks)]

    if blinks == 1:
        result = len(convert(val))
    else:
        result = sum(get_num(result, blinks - 1) for result in convert(val))

    get_num_cache[(val, blinks)] = result
    return result

blinks = 25
result = sum(get_num(val, blinks) for val in input_arr)
print(result)
