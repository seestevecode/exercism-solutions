"""Implement Conway's Game of Life"""

def neighbours(target_row, target_column, matrix):
    """Returns the number of live neighbours of a cell"""
    height, width = len(matrix), len(matrix[0])
    return sum(
        matrix[row][column]
        for row in range(max(0, target_row - 1), min(height, target_row + 2))
        for column in range(max(0, target_column - 1), min(width, target_column + 2))
        if (row, column) != (target_row, target_column)
    )


def tick_cell(cell, neighbour_count):
    """Returns the new state of a single cell, given its neighbour count"""
    return int(neighbour_count == 3 or (cell == 1 and neighbour_count == 2))


def tick(matrix):
    """Returns the new state of the entire matrix after one tick"""
    return [
        [
            tick_cell(matrix[row][column], neighbours(row, column, matrix))
            for column in range(len(matrix[row]))
        ]
        for row in range(len(matrix))
    ]
    