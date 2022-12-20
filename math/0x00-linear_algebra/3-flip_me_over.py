#!/usr/bin/env python3
"""
Transpose a matrix by using python
"""


def matrix_transpose(matrix):
    """
    Transpose a matrix
    """
    row_range, column_range = (range(len(matrix[0])), range(len(matrix)))
    if column_range.stop > row_range.stop:
        row_range, column_range = column_range, row_range
    transposed_matrix = [[matrix[j][i] for j in row_range] for i in column_range]
    return transposed_matrix
