#!/usr/bin/python3
def no_c(my_string):
    table = str.maketrans("cC", "cC", "cC")
    my_string = my_string.translate(table)
    return my_string
