"""Transpose text"""

# pylint: disable=missing-function-docstring

from itertools import zip_longest

def transpose(text):
    def transpose_row(row):
        last = max(
            (index for index, char in enumerate(row) if char is not None),
            default=-1
        )
        return ''.join(' ' if char is None else char for char in row[:last + 1])
    
    return '\n'.join(
        transpose_row(row)
        for row in zip_longest(*text.split('\n'), fillvalue=None)
    )
