#!/usr/bin/python3
def all_combs():
    for i in range(10):
        for j in range(10):
            if i == j or i > j:
                continue
            if i == 8 and j == 9:
                print("{}{}".format(i, j))
                return
            print("{}{}".format(i, j), end=", ")
