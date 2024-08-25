#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if n >= 1 & n <=100 :
        if n%2 !=0 :
            print("Weird")
        else:
            if n in range(2,5):
                print("Not Weird")
            elif n in range(6,21):
                print("Weird")
            elif n >= 20:
                print("Not Weird")
                
