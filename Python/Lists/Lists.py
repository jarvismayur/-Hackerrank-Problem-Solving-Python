if __name__ == '__main__':
    N = int(input())
    li = []
    
    for n in range(0, N):
        a = input()
        res = a.split()
        if len(res) == 2:
            num = int(res[1])
        if len(res) == 3:
            num = int(res[2])
            pos = int(res[1])
        
        command = res[0]
        if (command == "print"):
            print(li)
        if(command == "insert"):
            li.insert(pos, num)
        if(command == "remove"):
            li.remove(num)
        if(command == "append"):
            li.append(num)
        if(command == "sort"):
            li.sort()
        if(command == "pop"):
            li.pop()
        if(command == "reverse"):
            li.reverse()
            
