#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# must remain sorted backwards
PIECES = [5, 2, 1]

def getSteps(n):
    steps = 0
    leftover = n

    for piece in PIECES:
        if leftover / piece >= 1:
            steps += int(leftover / piece)
            leftover %= piece

    return steps

def equal(arr):
    if len(arr) == 1:
        return 0
    
    arr = sorted(arr)
    count = 0
    last_num = arr[0]
    
    for i in range(1, len(arr)):
        diff = arr[i] - last_num

        # get the count from diff steps or calculate (without adding to the arr yet)
        count += getSteps(diff)
        # then add to array
        for j in range(i + 1, len(arr)):
            arr[j] += diff
                
        last_num = arr[i]
                
    return count

# record start time
start = time.time()
 
# do work
file = open('input.txt', 'r')
num_cases = int(file.readline())

for i in range(num_cases):
    size_arr = int(file.readline())
    arr = [int(x) for x in file.readline().split(' ')]
    print(equal(arr)) # should be 3, 7, 6

# record end time
end = time.time()
 
# print the difference between start 
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms") # was about a minute