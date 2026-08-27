"""Determine the saddle points of a matrix"""

# pylint: disable=missing-function-docstring

def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('irregular matrix')

    row_maxes = [max(row) for row in matrix]
    col_mins = [min(col) for col in zip(*matrix)]

    return [
        {'row': row + 1, 'column': col + 1}
        for row in range(len(matrix))
        for col in range(len(matrix[0]))
        if matrix[row][col] == row_maxes[row]
            and matrix[row][col] == col_mins[col]
    ]
