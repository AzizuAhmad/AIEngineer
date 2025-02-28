#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    arr.sort()
    minn = arr.copy()
    arr.sort(reverse = True)
    maxx = arr.copy()
    sumMin = 0
    sumMax = 0
    
    for i in range(len(arr)-1):
        sumMin = sumMin + minn[i]
        sumMax = sumMax + maxx[i]
    
    print(sumMin,sumMax)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
