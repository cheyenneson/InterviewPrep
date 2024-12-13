def diff_safe(a, b):
    return (1 <= abs(a - b) <= 3)

def inc_safe(a, b, inc):
    return (inc and a <= b) or (not inc and a >= b)

def safe(a, b, inc):
    return (inc_safe(a, b, inc)) and diff_safe(a, b)

input = open('input/day_2_input.txt', 'r')
data = []
num_safe = 0
damp_safe = 0

for line in input:
    nums = line.split(' ')
    nums = [int(num) for num in nums]
    data.append(nums)
    inc = nums[0] < nums[1]

    for i in range(1, len(nums)):
        if not safe(nums[i - 1], nums[i], inc):
            break
        if i == len(nums) - 1:
            num_safe += 1

print("Part I: ", num_safe)

for nums in data:
    l_ptr = 0
    r_ptr = 1
    chances = 1 # you only get one chance
    inc = nums[0] < nums[1]

    while r_ptr < len(nums):
        print('a: ', nums[l_ptr], ' b: ', nums[r_ptr])

        if not inc_safe(nums[l_ptr], nums[r_ptr], inc):
            if chances < 1:
                break
            else:
                chances -= 1
                inc = not inc
                r_ptr += 1
                continue
        
        if not diff_safe(nums[l_ptr], nums[r_ptr]):
            if chances < 1:
                break
            else:
                chances -= 1
                r_ptr += 1
                continue

        if safe(nums[l_ptr], nums[r_ptr], inc) and r_ptr == len(nums) - 1:
            damp_safe += 1
            print('safe')

        l_ptr += 1
        r_ptr += 1

    print()

print("Part II: ", damp_safe) # 4

