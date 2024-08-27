def merge_the_tools(string, k):
    for a in range(0, len(string), k):
        substring = string[a:a+k]
        seen = ""
        for b in substring:
            if b not in seen:
                seen= seen+ b
        print(seen)
    
    
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)