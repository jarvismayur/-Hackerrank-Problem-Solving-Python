

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n , m = input().split()
    n = int(n)
    m = int(m)
    if n >= 1 and n <=10**5 and m >=1 and m<= 10**5:
        n = list(map(int, input().split()[:n]))
        A = set(list(map(int, input().split()[:m])))
        B = set(list(map(int, input().split()[:m])))
    temp = []
    for a in A:
        if a >= 1 and a <= 10**9:
            temp.append(a)
    A = set(temp)
    temp = []
    for a in B:
        if a >= 1 and a <= 10**9:
            temp.append(a)
    B = set(temp)
    res = 0

    for a in n:
        if a in A:
            res = res + 1
            


    for a in n:
        if a in B:
            res = res - 1


    print(res)
