#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda int: int * int, row)) for row in matrix])
