#!/usr/bin/python3
"""matrix divided module"""


def matrix_checker(matrix, div):
    """matrix_checker function"""
    div_number_error = "div must be a number"
    div_zero_error = "division by zero"
    matrix_list_error = "matrix must be a matrix "
    matrix_list_error += "(list of lists) of integers/floats"
    row_size_error = "Each row of the matrix must have the same size"

    if ((type(div) != int and type(div) != float)
            or type(div) is None or type(div) == bool):
        raise TypeError(div_number_error)
    if div == 0:
        raise ZeroDivisionError(div_zero_error)
    if not isinstance(matrix, list):
        raise TypeError(matrix_list_error)

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError(row_size_error)
        if not isinstance(i, list):
            raise TypeError(matrix_list_error)
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError(matrix_list_error)


def matrix_divided(matrix, div):
    """matrix_divided function"""
    matrix_checker(matrix, div)
    new_matrix = list()
    for i in matrix:
        new_list = list()
        for j in i:
            new_list.append(round(j / div, 2))
        new_matrix.append(new_list)
        del(new_list)
    return(new_matrix)
