# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement



data = input()
data = data.split(" ")

s =[]
for a in data[0]:
    s.append(a)
per = int(data[1])

s.sort()

for a in list(combinations_with_replacement(s, per)):
    print("".join(a))