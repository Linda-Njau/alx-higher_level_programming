#!/usr/bin/python3
"""defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide elements of matrix by div constant.

    Args:
        matrix: of type list
        div: constant to divide matrix
    """
    div_matrix = []
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if (len(row) != len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            div_matrix.append(list(map(lambda x: round (x / div, 2), row)))
    return div_matrix
