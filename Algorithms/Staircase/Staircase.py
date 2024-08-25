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
    # Write your code here
    i = 1
    while n >0:
        for a in range(n-1):
            print(" ", end="")
        for a in range(i):
            print("#" , end="")
        print("")
        n = n-1
        i = i +1
        
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
