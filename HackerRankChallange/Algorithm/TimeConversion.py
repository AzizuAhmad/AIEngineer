#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ampm = s[-2:]
    if ampm == 'AM':
        time = s[:-2]
        if int(s[0:2]) == 12:
            temp = "00"
            time = temp+time[2:]
        else:
            time = s[:-2]
    else:
        time = s[:-2]
        if int(s[0:2]) == 12:
            time = s[:-2]
        else:
            add = s[0:2]
            temp = str(12+int(add))
            time = temp+time[2:]
    
    return time
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
