#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cp_dict = a_dictionary.copy()
    for i in cp_dict.keys():
        cp_dict[i] *= 2
    return cp_dict
