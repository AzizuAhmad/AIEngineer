#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    lr = 0
    rl = 0
    help1 = len(arr) - 1
    help2 = 0
    
    
    for i in range(len(arr[0])):
        for j in range(len(arr[1])):
            if j == help2:
                lr = lr + arr[i][j]
                
            
            if j == help1:
                rl = rl + arr[i][j]
                
        help2 = help2 + 1
        help1 = help1 - 1
                
    return abs(lr-rl)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
