#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    # s = begin range
    # t = end range
    # a = apple tree position
    # b = orange tree position
    # m = count of apple
    # n = count of orange
    # resApple = []
    # resOrange = []
    countApples = 0
    countOrange = 0
    
    for i in range(len(apples)):
        temp = a + apples[i]
        if temp >= s and temp <= t:
            # resApple.append(temp)
            countApples= countApples + 1
    
    for i in range(len(oranges)):
        temp = b + oranges[i]
        if temp >= s and temp <= t:
            # resOrange.append(temp)
            countOrange = countOrange + 1
    
    print(f"{countApples}\n{countOrange}")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
