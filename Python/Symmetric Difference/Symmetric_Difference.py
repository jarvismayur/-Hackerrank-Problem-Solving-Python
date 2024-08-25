# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    M = int(input())
    M = set(list(map(int, input().split()[:M])))
    N = int(input())
    N = set(list(map(int, input().split()[:N])))
    res_M = M.difference(N)
    res_N = N.difference(M)
    res = res_M.union(res_N)
    res= sorted(list(res))
    
    for a in res:
        print(a)
