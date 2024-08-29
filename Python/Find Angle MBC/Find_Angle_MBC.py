# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = float(input())
BC = float(input())
res = round(math.degrees(math.atan(AB/ BC)))
if res > 90:
    res = (res/90) *100
elif res < 0:
    res = (res/90) *100

print(str(res) +"\u00b0")