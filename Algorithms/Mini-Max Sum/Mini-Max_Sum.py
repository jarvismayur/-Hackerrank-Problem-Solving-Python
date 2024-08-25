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
    # Write your code here
    arr_len = len(arr)
    arr_data = []
    for a in range(arr_len):
        res = sum(arr)
        res = res - arr[a]
        arr_data.append(res)
    arr_min = min(arr_data)
    arr_max = max(arr_data)
    print("{} {}".format(arr_min, arr_max))
        
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
