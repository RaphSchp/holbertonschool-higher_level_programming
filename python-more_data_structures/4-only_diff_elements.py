#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for i in set_1:
        for j in set_2:
            if i not in set_2 and j not in set_1:
                new_set.add(j)
                new_set.add(i)
    return (new_set)
