#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    temp = n - 1
    
    for i in range(n):
        for j in range(n):
            if j>=temp:
                print("#",end='')
            elif j<temp:
                print(" ",end="")
        
        print("")
        temp-=1
            

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
