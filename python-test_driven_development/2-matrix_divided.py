#!/usr/bin/python3

"""
Creating a funtion that divides the matrix

"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Parameters:
    matrix: matrix being divided
    div: number the matrix is divided by.

    Returns: a new divided matrix

    Raises:
    TypeError: If matrix is not a list of integers or floats.
    TypeError: If each row of the matrix does not have the same size.
    TypeError: If div is not a number (integer or float).
    ZeroDivisionError: If div is equal to 0.
    """

    # Validate matrix

    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Validate RowSize

    RowSize = len(matrix[0])
    if not all(len(row) == RowSize for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding

    NewMatrix = []
    for row in matrix:
        NewRow = [round(element / div, 2) for element in row]
        NewMatrix.append(NewRow)

    return NewMatrix
