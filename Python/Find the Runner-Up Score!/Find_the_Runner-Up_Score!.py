if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    temp = []
    if n >= 2 & n<=10:
        for a in arr:
            if a >= -100 & a <= 100:
                temp.append(a)
    print(sorted(list(set(temp)))[-2])
    