"""Return a square matrix with numbers spiralled"""

# pylint: disable=missing-function-docstring

def spiral_matrix(size):
    spiral = [[0] * size for _row in range(size)]
    top, right, bottom, left = 0, size - 1, size - 1, 0
    value = 1

    while top <= bottom and left <= right:
        # right along the top
        for col in range(left, right + 1):
            spiral[top][col] = value
            value += 1
        top += 1

        # down the right
        for row in range(top, bottom + 1):
            spiral[row][right] = value
            value += 1
        right -= 1

        # left along the bottom
        if top <= bottom:
            for col in range(right, left - 1, -1):
                spiral[bottom][col] = value
                value += 1
            bottom -= 1

        # up the left
        if left <= right:
            for row in range(bottom, top - 1, -1):
                spiral[row][left] = value
                value += 1
            left += 1

    return spiral        
