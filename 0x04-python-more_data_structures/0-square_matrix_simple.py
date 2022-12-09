#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = []
    for x in matrix:
        matrix_square.append(list(map(lambda x: x**2, x)))
    return (matrix_square)
