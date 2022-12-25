#!/usr/bin/env python3
"""
Add the components of two arrays together
"""


def add_arrays(arr1, arr2):
    """
    Add arrays of the same length
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[x] + arr2[x] for x in range(len(arr1))]
