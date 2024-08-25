def mutate_string(string, position, character):
    lis_str = list(string)
    lis_str[position] = character 
    return_string = ''.join(lis_str)
    return return_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)