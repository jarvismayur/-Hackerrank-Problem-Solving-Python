# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N =int(input())
    if N >= 0 & N <= 1000:
        temp = []
        for a in range(N):
            temp.append(input())
        N = set(list(temp))
    len = 0
    for a in N:
        len = len + 1
    print(len)