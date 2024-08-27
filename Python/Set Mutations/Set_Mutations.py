# Enter your code here. Read input from STDIN. Print output to STDOUT

num_of_elements = int(input())
elements = set(list(map(int, input().split())))
iter_num = int(input())
for a in range(0, iter_num):
    func, num = list(map(str,input().split()))
    num = int(num)
    elements_process = set(list(map(int, input().split())))
    if func == "intersection_update":
        elements.intersection_update(elements_process)
    elif func == "update":
        elements.update(elements_process)
    elif func == "symmetric_difference_update":
        elements.symmetric_difference_update(elements_process)
    elif func == "difference_update":
        elements.difference_update(elements_process)
print(sum(elements))