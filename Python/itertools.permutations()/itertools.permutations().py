# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

data = input()
data = data.split(" ")

s =[]
for a in data[0]:
    s.append(a)
per = int(data[1])



words =  []

for a in list(permutations(s, per)):
    words.append("".join(a))

words.sort()

for a in words:
    print(a)