

def wrap(string, max_width):
    list_str = list(string)
    ret_list = []
    i = 0 
    for a in list_str:
        if i % max_width == 0:
            if i != 0:
                ret_list.append("\n")
            ret_list.append(a)
        else:
            ret_list.append(a)
        i = i + 1 
    return_str = "".join(ret_list)
    return return_str

