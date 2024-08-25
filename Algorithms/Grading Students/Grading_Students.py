#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    final_grades= []
    for a in grades:
        check = ((a/5)*5)+(5-(a%5))-a
        if check < 3:
            if int((a/5)*5)+(5-(a%5)) >= 40:
                final_grades.append(int(((a/5)*5)+(5-(a%5))))
            else:
                final_grades.append(a)
        else:
            final_grades.append(a)
    for a in final_grades:
        print(a)
            
    return final_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
