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
    total  = len(arr)
    pos_count = 0 
    neg_count = 0 
    z_count = 0
    for a in arr:
        if a > 0:
            pos_count = pos_count +1 
        elif a < 0:
            neg_count = neg_count +1
        else:
            z_count = z_count +1 
    print("{:.6f}".format(pos_count/total));
    print("{:.6f}".format(neg_count/total));
    print("{:.6f}".format(z_count/total))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
