#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 1
    while i <= len(my_list):
        print("this is i: {}".format(i))
        print("{:d}".format(my_list[(i*-1)]))
        i += 1
