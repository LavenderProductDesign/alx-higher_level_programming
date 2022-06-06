#!/usr/bin/python3

#function that prints all integers of a list
#prototype def print_list_integer(my_list=[]):
#use str.format()

def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))
