#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    if len(matrix) == 0:
        return squared
    for i in matrix:
        for j in i:
            squared.append(j * j)
    return(squared)
