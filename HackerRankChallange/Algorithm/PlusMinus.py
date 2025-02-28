#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    n = len(arr)
    
    for i in range(n):
        if arr[i] > 0:
            pos = pos + 1
        if arr[i] < 0:
            neg = neg + 1
        elif arr[i] == 0:
            zero = zero + 1
    
    posRes = format(pos/n,".6f")
    negRes = format(neg/n,".6f")
    zeroRes = format(zero/n,".6f")
    
    print(f"{posRes}\n{negRes}\n{zeroRes}")
    # return posRes,negRes,zeroRes
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
