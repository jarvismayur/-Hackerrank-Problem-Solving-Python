# Enter your code here. Read input from STDIN. Print output to STDOUT

test_case = int(input())
for a in range(test_case):
    set_a_num = int(input())
    set_a_elements = set(list(map(int, input().split())))
    set_b_num = int(input())
    set_b_elements = set(list(map(int, input().split())))
    if set_a_elements.difference(set_b_elements):
        print(False)
    else:
        print(True)