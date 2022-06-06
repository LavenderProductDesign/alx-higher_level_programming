#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = []
    for i in range(len(my_list)):
        a.append(my_list[i])
    if idx < 0:
        return a
    elif idx >= len(my_list):
        return a
    else:
        a[idx] = element
        return a
