#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    i = 0
    while i < len(matrix):
        element = []
        j = 0
        while j < len(matrix[i]):
            element.append(matrix[i][j] ** 2)
            j += 1
        new_matrix.append(element)
        i += 1
    return (new_matrix)
