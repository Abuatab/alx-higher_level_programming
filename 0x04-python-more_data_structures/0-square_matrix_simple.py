#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for i in matrix:
        for j in i:
            squared.append(j * j)
    return(squared)
