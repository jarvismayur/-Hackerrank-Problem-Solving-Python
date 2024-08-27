# Python



## Alphabet Rangoli
## Arithmetic Operators
## Capitalize!
## Designer Door Mat
## Find a string
## Find the Runner-Up Score!
## Finding the percentage
## itertools.combinations()
## itertools.combinations_with_replacement()
## itertools.permutations()
## itertools.product()
## List Comprehensions
## Lists
## Loops
## Merge The Tools
My Frist code with only one test case passed 
```
    def merge_the_tools(string, k):
    new_str = []
    # your code goes here
    str_list = string.split()
    new_str_list = []
    for a in str_list:
        for b in a:
            new_str_list.append(b)
    count_str_list = len(new_str_list)
    parts = int(count_str_list/k)
    str_arr= []
    for i in range(1,len(new_str_list)+1):
        new_str.append(new_str_list[i-1])
        if i != 0:
            if i % parts == 0:
                str_arr.append("".join(new_str))
                new_str = []
        
    for s in str_arr:
        new_string = ""
        for char in s:
            if char not in new_string:
                new_string += char
```
my Last optimized code the all the test case pass
```
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
```
## Mutations
## Nested Lists
## No Idea!
## Print Function
## Python Division
## Python If-Else
## Say Hello World With Python
## Set .add()
## Set .discard(), .remove() & .pop()
## String Formatting
## String Split and Join
## String Validators
## sWAP cASE
## Symmetric Difference
## Text Alignment
## Text Wrap
## The Minion Game
## Tuples
## What's Your Name
## Write a function