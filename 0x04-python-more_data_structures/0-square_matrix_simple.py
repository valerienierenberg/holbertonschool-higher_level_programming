#!/usr/bin/python3

## 20:56 

def square_matrix_simple(matrix=[]):

    newmatrix = matrix[:]

    for x in newmatrix:
        b = [y*y for y in x]

    return b
