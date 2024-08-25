if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    arr = []
    
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                res = i + j + k 
                if res != n:
                    arr_1 = []
                    arr_1.append(i)
                    arr_1.append(j)
                    arr_1.append(k)
                    arr.append(arr_1)              
    print(arr)
    
