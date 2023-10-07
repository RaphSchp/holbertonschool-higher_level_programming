#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for i in range(len(my_list)):
        if my_list[i] not in my_list[:i]:
            res += my_list[i]
    return (res)
