input = open('input/day_9_input.txt', 'r')
input_str = input.readline().strip()

# if the last number just represents '.' chars, we don't care about it
if len(input_str) % 2 == 0:
    input_str = input_str[0:-1]

checksum_total = 0
left = 0
right = len(input_str) - 1
ID = 0
right_val = int(input_str[right])

while left < right:
    checksum_vals = []
    right_ID = int(right / 2)
    left_ID = int(left / 2)
    
    checksum_vals += [left_ID] * int(input_str[left])

    # for every dot
    for i in range(int(input_str[left + 1])):
        if right_val == 0:
            right -= 2
            right_val = int(input_str[right])
            right_ID = int(right / 2)
        checksum_vals += [right_ID]
        right_val -= 1

    # after we're finished with the dots, increment left
    left += 2

    for val in checksum_vals:
        checksum_total += ID * val
        ID += 1

for i in range(right_val):
    checksum_total += ID * right_ID
    ID += 1
    
print('Part I:', checksum_total)


# PART II
left = 0
right = len(input_str) - 1
checksum_vals = []
ID = 0
checksum_total = 0

while left < right:
    # add 00...
    checksum_vals += [int(left / 2)] * int(input_str[left])
    checksum_vals += [None] * int(input_str[left + 1]) # None represents '.'

    # get the 99
    length = int(input_str[right])

    for i in range(len(checksum_vals)):
        if checksum_vals[i] == None and checksum_vals[i:length] == [None] * length:
            checksum_vals[i:length] = [int(right /2)] * length
            input_str[right] = 'X'
            left += 2
            right -= 2
            continue

    left += 2

print(checksum_vals)
print(input_str)

# # add up the checksum of everything in the array
# for val in checksum_vals:
#     if val != None:
#         checksum_total += ID * val
#     ID += 1

# # then add that to the checksum of the rest of the input_str (right to end)
# for i in range(right, len(input_str), 2):
#     # FIXME - check that we're not counting the same thing twice, we might need to inc right by 2 first
#     if input_str[i] != 'X':
#         for j in range(int(input_str[i])):
#             checksum_total += int(i / 2) * ID
#             ID += 1
#     # FIXME - we can't use X's cause we need to know the number of dots, OR we add that number to the prev in the string
#     ID += int(input_str[i + 1])

# print('Part II:', checksum_total)