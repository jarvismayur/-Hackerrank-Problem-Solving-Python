if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        temp = []
        name = input()
        score = float(input())
        temp.append(name)
        temp.append(score)
        arr.append(temp)
    score_list = []
    for a  in arr:
        score_list.append(a[1])
    res = (sorted(list(set(score_list)),reverse=True)[-2])
    final_list = []
    for a in arr:
        if a[1] == res:
            final_list.append(a[0])
    sorted_final_list = sorted(list(set(final_list)))
    for a in sorted_final_list:
        print(a)