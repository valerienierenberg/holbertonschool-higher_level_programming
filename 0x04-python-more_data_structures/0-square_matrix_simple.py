#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix:
        return [list(map(lambda x: x**2, x)) for x in matrix]

# newmatrix = matrix[:]

# for x in newmatrix:
# newmatrix = [y*y for y in x]
# return newmatrix
