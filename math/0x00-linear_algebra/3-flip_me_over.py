#!/usr/bin/env python3
"""
Transpose a matrix by using python
"""


def matrix_transpose(matrix):
    """
    Transpose a matrix
    """
    if not matrix:
        return None
    row_range, col_range = (range(len(matrix[0])), range(len(matrix)))
    if col_range.stop > row_range.stop:
        row_range, col_range = col_range, row_range
    transposed_matrix = [[matrix[x][y] for x in row_range] for y in col_range]
    return transposed_matrix
