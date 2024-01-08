#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if i % 3 == 0:
            print()
            print(matrix[i])
