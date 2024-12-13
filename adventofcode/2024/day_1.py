def similarity_score(left, right):
    hashMap = {}
    sum = 0

    for val in right:
        if val in hashMap:
            hashMap[val] += 1
        else:
            hashMap[val] = 1

    for val in left:
        if val in hashMap:
            sum += hashMap[val] * val

    return sum


input = open('input/day_1_input.txt', 'r')
left = []
right = []
sum = 0

for line in input:
    l, r = line.split('   ')
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

for i in range(len(left)):
    sum += abs(right[i] - left[i])

print("Part I: ", sum)
print("Part II: ", similarity_score(left, right))

