#!/usr/bin/python3
"""This is a module that contains a function

This function is going to be used to make the project of TDD
"""


def matrix_divided(matrix, div):
    """Divide all elements of a list


    Args:
        matrix (list): List of lists of integers or floats
        div (int, float): The number to be divided

    Returns:
        A new matrix

    """

    if type(matrix) != list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix[0])
    for lista in matrix:
        if len(lista) != length:
            raise TypeError("Each row of the matrix must have the same size")
        elif type(lista) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    else:
        temp = [num for lista in matrix for num in lista]
        error = None
        for num in temp:
            if type(num) != int and type(num) != float:
                error = num
                break
        if error:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in lista] for lista in matrix]
    return new_matrix
