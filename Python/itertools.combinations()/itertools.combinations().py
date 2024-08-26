# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations



data = input()
data = data.split(" ")

s =[]
for a in data[0]:
    s.append(a)
per = int(data[1])




for a in range(1, per+1):
    words =  []

    for a in list(combinations(s, a)):
        a = ("".join(a))
        main_str= [] 
        for i in a:
            str = ''
            for j in i:
                str = str + j
            main_str.append(str)
        main_str.sort()
        words.append("".join(main_str))

    
    words.sort()
    
    for a in words:
        print(a)