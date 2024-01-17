#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_list = []
    if len(matrix) == 0:
        return squared_list
    squared_list = [[j * j for j in i] for i in matrix]
    return squared_list
