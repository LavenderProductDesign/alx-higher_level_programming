#!usr/bin/python3
# function replaces element of a list at a specific position
# prototype def replace_in_list(my_list, idx, element):


def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        return (my_list[idx])
