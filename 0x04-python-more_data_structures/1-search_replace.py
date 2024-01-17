#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if len(my_list) == 0:
        return new_list
    new_list = [replace if i == search else i for i in my_list]
    return new_list
