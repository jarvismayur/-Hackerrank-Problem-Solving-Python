from statistics import mean
def Average(lst):
    return mean(lst)
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if n >= 2 & n <= 10:
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            score_list =[]
            for a in scores:
                if a >= 0 and a <=100:
                    score_list.append(a)
            student_marks[name] = score_list
    query_name = input()
    print("{:0.2f}".format((Average(student_marks[query_name]))))
    
