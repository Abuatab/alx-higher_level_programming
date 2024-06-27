#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and returns the result as a new matrix.

    Args:
        matrix (list of lists of int/float): The matrix to be divided. Each row must be of the same length.
        div (int/float): The divisor by which all elements of the matrix will be divided.

    Returns:
        list of lists of float: A new matrix with all elements divided by the given divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If div is not a number (integer or float).
        TypeError: If any row in the matrix is not of the same size.
        TypeError: If any element in the matrix is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    for i in matrix:
        temp_list = []
        for j in i:
            temp_list.append(round(j/div, 2))
        new_matrix.append(temp_list)

    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.py")
