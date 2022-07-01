#!/usr/bin/env python3
"""
Calculates the shape of a matrix
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix
    """
    if type(matrix) is list:
        return [len(matrix)] + matrix_shape(matrix[0])
    else:
        return []
