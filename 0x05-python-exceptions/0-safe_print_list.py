#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_elements = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            num_of_elements += 1
        except IndexError:
            break
    print("")
    return num_of_elements
