#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Calculate the squares of row entries in a matrix"""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
