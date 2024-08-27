# Enter your code here. Read input from STDIN. Print output to STDOUT

s = set(map(int, input().split()))
inp = int(input())
res = True 

while(inp):
    a = set(map(int, input().split()))
    if len(s) <= len(a):
        res = False
        print(res)
        sys.exit()
    if len(s) > len(a):
        res = s.issuperset(a)
        if not res:
            break
    
    inp -= 1
print(res)