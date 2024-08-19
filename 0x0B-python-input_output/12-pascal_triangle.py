#!/usr/bin/python3
"""Implements pascal's triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s
    triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        # Compute the values in between
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle
