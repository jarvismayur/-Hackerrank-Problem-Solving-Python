def switch_case(command,s,q =0):
    if command == "pop":
        s.pop()
        return s
    elif command == "remove":
        s.remove(q)
        return s
    elif command == "discard":
        s.discard(q)
        return s
        
n = int(input())
if n >=0 & n<=20:
    s = set(list(map(int, input().split()[:n])))
N  = int(input())
for a in range(N):
    command, *q = input().split()
    if command=="pop":
        a = 0
        switch_case(command,s,a)
    q = list(map(int, q))
    for a in q:
        s = switch_case(command,s,a)
res = 0
for a in s:
    res = res + a

print(res)


    
