"""Implement a Matrix class"""

# pylint: disable=missing-function-docstring

class Matrix:  # pylint: disable=missing-class-docstring
    def __init__(self, matrix_string):
        self._grid = [
            [int(num) for num in line.split(' ')]
            for line in matrix_string.split('\n')
        ]

    def row(self, index):
        return self._grid[index - 1]

    def column(self, index):
        transposed = [list(row) for row in zip(*self._grid)]
        return transposed[index - 1]
