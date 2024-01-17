#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j * j)
            squared.append(row)
        return(squared)
